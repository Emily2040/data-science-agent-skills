# Messy Fixture: `missingness-mechanism-investigator`

Prompt:

```text
Use $missingness-mechanism-investigator on a messy project where dataset, analysis goal are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: target-dependent missingness.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/dataset.csv --max-rows 10000
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `target-dependent missingness` in `Findings` and `Risks`).
