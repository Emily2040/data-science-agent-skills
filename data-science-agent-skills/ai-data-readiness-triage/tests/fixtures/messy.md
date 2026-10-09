# Messy Fixture: `ai-data-readiness-triage`

Prompt:

```text
Use $ai-data-readiness-triage on a messy project where dataset paths or schemas, data owner are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: unknown owner.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/dataset.csv --max-rows 10000
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `unknown owner` in `Findings` and `Risks`).
