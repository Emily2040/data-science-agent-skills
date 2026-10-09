# Messy Fixture: `messy-data-cleanroom`

Prompt:

```text
Use $messy-data-cleanroom on a messy project where raw dataset, data dictionary if available are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: overwriting raw data.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/raw_extract.csv --max-rows 10000
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `overwriting raw data` in `Findings` and `Risks`).
