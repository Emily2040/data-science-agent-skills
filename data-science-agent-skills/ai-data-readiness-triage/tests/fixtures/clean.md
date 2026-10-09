# Clean Fixture: `ai-data-readiness-triage`

Prompt:

```text
Use $ai-data-readiness-triage on this clean request: Assess whether a dataset or data domain is ready for AI, analytics, or modeling before a project commits time and budget. The project provides dataset paths or schemas, data owner, intended use case, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/dataset.csv --max-rows 10000
```

Expected decision: `go` (with documented assumptions and next action).
