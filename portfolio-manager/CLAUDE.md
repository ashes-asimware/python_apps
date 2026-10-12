# CLAUDE.md

Guidance for working in the `portfolio-manager` project.

## Overview

A small Flask app for recording periodic portfolio balance snapshots. The web form appends one dated record to each of three JSON files (`input/cc.json`, `input/hs.json`, `input/ir.json`), and a generator turns those files into a SQL Server script (`output/RUNTHIS.SQL`) that truncates and reloads the `[PORTFOLIO]` table.

## Commands

```powershell
# Setup (only dependency is Flask>=3.0.0)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Run the web app (debug=False, http://127.0.0.1:5000)
python app.py

# Generate SQL from the command line
python generate_portfolio_sql.py input/cc.json input/hs.json input/ir.json -o output/RUNTHIS.SQL
```

There are no tests, linter or build step.

## Layout

- `app.py`: Flask app. Routes are `GET /`, `POST /save` and `POST /generate`. Also holds the validation and JSON read/write helpers.
- `generate_portfolio_sql.py`: `build_sql(cc_path, hs_path, ir_path)` plus an argparse CLI. `app.py` imports `build_sql`.
- `templates/index.html`: the single form page.
- `input/{cc,hs,ir}.json`: source-of-truth data, tracked in git.
- `output/`: generated SQL, gitignored.

## Data model

| Prefix | CATEGORY | Amount fields |
| --- | --- | --- |
| `cc` | CRYPTOCURRENCY | BITCOIN, ETHEREUM, CASH |
| `hs` | HEALTHSAVINGS | OPTUM, HEALTHEQUITY |
| `ir` | INDIVIDUALRETIREMENT | MGI, SGI, FIDELITY_TS, SCHWAB, ANNUITY_PE10, ANNUITY_A10, FIDELITY_IG, AONPEP_TS |

- Each JSON file is an array of records: `ENTEREDON`, `CATEGORY`, plus numeric amount fields.
- `ENTEREDON` must be strictly `MM/DD/YYYY` (for example `05/09/2026`) and unique within its file.
- A new record must have exactly the same key set as the file's first record.
- Each amount field becomes one SQL row: `(ENTEREDON, CATEGORY, NAME, AMOUNT)`.
- Form field names are `<prefix>_<field name lowercased>`, for example `ir_fidelity_ts`.

## Adding or renaming an account field

Update all of these together, or saves will fail key validation:

1. The field list in `app.py` (`CC_FIELDS`, `HS_FIELDS` or `IR_FIELDS`).
2. `_form_state_from_last_records` and `_form_state_from_request` in `app.py`.
3. `templates/index.html`.
4. Existing records in the matching `input/*.json` file.

## Code style

- Start modules with `from __future__ import annotations`. Use full type hints and `pathlib.Path`.
- Internal helpers are prefixed with `_`.
- Validation raises `ValueError` with messages shaped like `"<LABEL>: ..."`.
- Routes catch `ValueError` and `OSError` and re-render `index.html` with `error`. Success re-renders with `message`.

## Gotchas

- `/save` writes the three files one after another and is not atomic. A failure on `hs` or `ir` after `cc` succeeds leaves a partial update.
- SQL is built by string formatting with single-quote escaping (`_escape_sql_string`). Keep that escaping if you touch the generator.
- The generated SQL begins with `TRUNCATE TABLE [PORTFOLIO];`. Review it before running it against a database.
- `input/*.json` contains real financial data. Don't print, log or share its contents unnecessarily.
