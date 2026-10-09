# Clean Fixture: `missingness-mechanism-investigator`

Prompt:

```text
Use $missingness-mechanism-investigator on this clean request: Diagnose missing-data mechanisms and design imputation, exclusion, or sensitivity plans. The project provides dataset, analysis goal, column meanings, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/dataset.csv --max-rows 10000
```

Expected decision: `go` (with documented assumptions and next action).
