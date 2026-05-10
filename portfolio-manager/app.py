from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from flask import Flask, render_template, request

from generate_portfolio_sql import build_sql

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_SQL = BASE_DIR / "output" / "RUNTHIS.SQL"

FILE_MAP = {
    "cc": INPUT_DIR / "cc.json",
    "hs": INPUT_DIR / "hs.json",
    "ir": INPUT_DIR / "ir.json",
}


app = Flask(__name__)

CC_FIELDS = ["BITCOIN", "ETHEREUM", "CASH"]
HS_FIELDS = ["HSA"]
IR_FIELDS = [
    "MGI",
    "SGI",
    "FIDELITY_TS",
    "SCHWAB",
    "ANNUITY_PE10",
    "ANNUITY_A10",
    "FIDELITY_IG",
]

CATEGORIES = {
    "cc": "CRYPTOCURRENCY",
    "hs": "HEALTHSAVINGS",
    "ir": "INDIVIDUALRETIREMENT",
}


def _read_records(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON array in {path}")
    return data


def _write_records(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(records, handle, indent=2)
        handle.write("\n")


def _parse_amount(raw: str, label: str, field_name: str) -> int | float:
    text = raw.strip()
    if not text:
        raise ValueError(f"{label}: {field_name} must be provided")

    try:
        if "." in text:
            return float(text)
        return int(text)
    except ValueError as exc:
        raise ValueError(f"{label}: {field_name} must be numeric") from exc


def _validate_entered_on(entered_on: str, label: str) -> str:
    date_text = entered_on.strip()
    if not date_text:
        raise ValueError(f"{label}: ENTEREDON is required")

    try:
        parsed = datetime.strptime(date_text, "%m/%d/%Y")
    except ValueError as exc:
        raise ValueError(
            f"{label}: ENTEREDON must be a valid date in MM/DD/YYYY format"
        ) from exc

    normalized = parsed.strftime("%m/%d/%Y")
    if normalized != date_text:
        raise ValueError(
            f"{label}: ENTEREDON must be in MM/DD/YYYY format (example: 05/09/2026)"
        )

    return date_text


def _build_record_from_form(
    form: Any,
    prefix: str,
    label: str,
    category: str,
    amount_fields: list[str],
) -> dict[str, Any]:
    entered_on_raw = form.get(f"{prefix}_enteredon", "") or ""
    entered_on = _validate_entered_on(str(entered_on_raw), label)

    record: dict[str, Any] = {
        "ENTEREDON": entered_on,
        "CATEGORY": category,
    }
    for field_name in amount_fields:
        raw_value = form.get(f"{prefix}_{field_name.lower()}", "") or ""
        record[field_name] = _parse_amount(raw_value, label, field_name)

    return record


def _validate_keys(
    new_record: dict[str, Any], existing_record: dict[str, Any], label: str
) -> None:
    expected = set(existing_record.keys())
    actual = set(new_record.keys())
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        details = []
        if missing:
            details.append(f"missing keys: {', '.join(missing)}")
        if extra:
            details.append(f"extra keys: {', '.join(extra)}")
        detail_text = "; ".join(details)
        raise ValueError(f"{label}: keys must match existing schema ({detail_text})")


def _append_record(path: Path, new_record: dict[str, Any], label: str) -> None:
    records = _read_records(path)
    if not records:
        raise ValueError(f"{label}: source file is empty")

    sample = records[0]
    if not isinstance(sample, dict):
        raise ValueError(f"{label}: source records are not valid objects")

    _validate_keys(new_record, sample, label)

    new_entered_on = new_record["ENTEREDON"]
    existing_entered_on = {
        item["ENTEREDON"].strip()
        for item in records
        if isinstance(item, dict) and isinstance(item.get("ENTEREDON"), str)
    }
    if new_entered_on in existing_entered_on:
        raise ValueError(
            f"{label}: ENTEREDON '{new_entered_on}' already exists in the file"
        )

    records.append(new_record)
    _write_records(path, records)


def _last_record(path: Path) -> dict[str, Any]:
    records = _read_records(path)
    if not records:
        return {}
    last = records[-1]
    if not isinstance(last, dict):
        raise ValueError(f"Expected object records in {path}")
    return last


def _form_state_from_last_records() -> dict[str, dict[str, str]]:
    cc = _last_record(FILE_MAP["cc"])
    hs = _last_record(FILE_MAP["hs"])
    ir = _last_record(FILE_MAP["ir"])

    return {
        "cc": {
            "enteredon": str(cc.get("ENTEREDON", "")),
            "category": CATEGORIES["cc"],
            "bitcoin": str(cc.get("BITCOIN", "")),
            "ethereum": str(cc.get("ETHEREUM", "")),
            "cash": str(cc.get("CASH", "")),
        },
        "hs": {
            "enteredon": str(hs.get("ENTEREDON", "")),
            "category": CATEGORIES["hs"],
            "hsa": str(hs.get("HSA", "")),
        },
        "ir": {
            "enteredon": str(ir.get("ENTEREDON", "")),
            "category": CATEGORIES["ir"],
            "mgi": str(ir.get("MGI", "")),
            "sgi": str(ir.get("SGI", "")),
            "fidelity_ts": str(ir.get("FIDELITY_TS", "")),
            "schwab": str(ir.get("SCHWAB", "")),
            "annuity_pe10": str(ir.get("ANNUITY_PE10", "")),
            "annuity_a10": str(ir.get("ANNUITY_A10", "")),
            "fidelity_ig": str(ir.get("FIDELITY_IG", "")),
        },
    }


def _form_state_from_request(form: Any) -> dict[str, dict[str, str]]:
    return {
        "cc": {
            "enteredon": (form.get("cc_enteredon", "") or "").strip(),
            "category": CATEGORIES["cc"],
            "bitcoin": (form.get("cc_bitcoin", "") or "").strip(),
            "ethereum": (form.get("cc_ethereum", "") or "").strip(),
            "cash": (form.get("cc_cash", "") or "").strip(),
        },
        "hs": {
            "enteredon": (form.get("hs_enteredon", "") or "").strip(),
            "category": CATEGORIES["hs"],
            "hsa": (form.get("hs_hsa", "") or "").strip(),
        },
        "ir": {
            "enteredon": (form.get("ir_enteredon", "") or "").strip(),
            "category": CATEGORIES["ir"],
            "mgi": (form.get("ir_mgi", "") or "").strip(),
            "sgi": (form.get("ir_sgi", "") or "").strip(),
            "fidelity_ts": (form.get("ir_fidelity_ts", "") or "").strip(),
            "schwab": (form.get("ir_schwab", "") or "").strip(),
            "annuity_pe10": (form.get("ir_annuity_pe10", "") or "").strip(),
            "annuity_a10": (form.get("ir_annuity_a10", "") or "").strip(),
            "fidelity_ig": (form.get("ir_fidelity_ig", "") or "").strip(),
        },
    }


@app.get("/")
def index() -> str:
    form_values = _form_state_from_last_records()
    return render_template(
        "index.html",
        form_values=form_values,
        message=None,
        error=None,
    )


@app.post("/generate")
def generate() -> str:
    submitted_form_values = _form_state_from_request(request.form)

    try:
        cc_record = _build_record_from_form(
            request.form,
            prefix="cc",
            label=CATEGORIES["cc"],
            category=CATEGORIES["cc"],
            amount_fields=CC_FIELDS,
        )
        hs_record = _build_record_from_form(
            request.form,
            prefix="hs",
            label=CATEGORIES["hs"],
            category=CATEGORIES["hs"],
            amount_fields=HS_FIELDS,
        )
        ir_record = _build_record_from_form(
            request.form,
            prefix="ir",
            label=CATEGORIES["ir"],
            category=CATEGORIES["ir"],
            amount_fields=IR_FIELDS,
        )

        _append_record(FILE_MAP["cc"], cc_record, CATEGORIES["cc"])
        _append_record(FILE_MAP["hs"], hs_record, CATEGORIES["hs"])
        _append_record(FILE_MAP["ir"], ir_record, CATEGORIES["ir"])

        sql_text = build_sql(FILE_MAP["cc"], FILE_MAP["hs"], FILE_MAP["ir"])
        OUTPUT_SQL.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_SQL.write_text(sql_text, encoding="utf-8")

        success_form_values = _form_state_from_last_records()

        return render_template(
            "index.html",
            form_values=success_form_values,
            message=f"Records added and SQL generated at {OUTPUT_SQL}",
            error=None,
        )
    except ValueError as exc:
        return render_template(
            "index.html",
            form_values=submitted_form_values,
            message=None,
            error=str(exc),
        )
    except OSError as exc:
        return render_template(
            "index.html",
            form_values=submitted_form_values,
            message=None,
            error=f"Unable to read or write portfolio files: {exc}",
        )


if __name__ == "__main__":
    app.run(debug=False)
