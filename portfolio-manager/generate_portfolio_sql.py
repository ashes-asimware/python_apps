from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _escape_sql_string(value: str) -> str:
    return value.replace("'", "''")


def _load_json_records(file_path: Path) -> list[dict[str, Any]]:
    with file_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {file_path}")

    records: list[dict[str, Any]] = []
    for idx, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Expected object at index {idx} in {file_path}")
        records.append(item)
    return records


def _to_portfolio_rows(
    records: list[dict[str, Any]],
) -> list[tuple[str, str, str, int | float]]:
    rows: list[tuple[str, str, str, int | float]] = []
    for record in records:
        entered_on = record.get("ENTEREDON")
        category_raw = record.get("CATEGORY")

        if not isinstance(entered_on, str) or not entered_on.strip():
            raise ValueError("Each record must include a non-empty ENTEREDON string")
        if not isinstance(category_raw, str) or not category_raw.strip():
            raise ValueError("Each record must include a non-empty CATEGORY string")

        category = category_raw.strip()
        for key, value in record.items():
            if key in {"ENTEREDON", "CATEGORY"}:
                continue
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"Amount field '{key}' for date {entered_on} in category {category} must be numeric"
                )
            rows.append((entered_on, category, key, value))
    return rows


def _format_value_tuple(row: tuple[str, str, str, int | float]) -> str:
    entered_on, category, name, amount = row
    entered_on_sql = _escape_sql_string(entered_on)
    category_sql = _escape_sql_string(category)
    name_sql = _escape_sql_string(name)

    if isinstance(amount, bool):
        # bool is a subclass of int; treat it as invalid for money-like fields.
        raise ValueError(f"Boolean amount is not allowed: {row}")

    amount_sql = f"{amount:g}" if isinstance(amount, float) else str(amount)
    return f"('{entered_on_sql}','{category_sql}','{name_sql}',{amount_sql})"


def build_sql(cc_path: Path, hs_path: Path, ir_path: Path) -> str:
    all_rows: list[tuple[str, str, str, int | float]] = []
    for source in (cc_path, hs_path, ir_path):
        all_rows.extend(_to_portfolio_rows(_load_json_records(source)))

    if not all_rows:
        raise ValueError(
            "No portfolio rows were generated from the provided input files"
        )

    value_lines = []
    for idx, row in enumerate(all_rows):
        suffix = "," if idx < len(all_rows) - 1 else ";"
        value_lines.append(f"{_format_value_tuple(row)}{suffix}")

    sql_lines = [
        "TRUNCATE TABLE [PORTFOLIO];",
        "INSERT INTO [PORTFOLIO]([ENTEREDON],[CATEGORY],[NAME],[AMOUNT]) VALUES",
        *value_lines,
        "SELECT * FROM [PORTFOLIO] ORDER BY [ENTEREDON] DESC, [CATEGORY];",
    ]
    return "\n".join(sql_lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate output SQL from cc.json, hs.json, and ir.json portfolio files."
    )
    parser.add_argument("cc", type=Path, help="Path to cc.json")
    parser.add_argument("hs", type=Path, help="Path to hs.json")
    parser.add_argument("ir", type=Path, help="Path to ir.json")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("output") / "RUNTHIS.SQL",
        help="Output SQL file path (default: output/RUNTHIS.SQL)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sql_text = build_sql(args.cc, args.hs, args.ir)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(sql_text, encoding="utf-8")

    print(f"Wrote SQL to {args.output}")


if __name__ == "__main__":
    main()
