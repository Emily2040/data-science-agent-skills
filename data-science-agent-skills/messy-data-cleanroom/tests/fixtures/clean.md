# Clean Fixture: `messy-data-cleanroom`

Prompt:

```text
Use $messy-data-cleanroom on this clean request: Design transparent, reversible cleaning plans for messy datasets without silently mutating evidence. The project provides raw dataset, data dictionary if available, analysis goal, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/raw_extract.csv --max-rows 10000
```

Expected decision: `go` (with documented assumptions and next action).
