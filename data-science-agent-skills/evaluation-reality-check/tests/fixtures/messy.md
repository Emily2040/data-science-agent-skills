# Messy Fixture: `evaluation-reality-check`

Prompt:

```text
Use $evaluation-reality-check on a messy project where task type, data generation process are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: random split for temporal deployment.
```

Expected deterministic check:

```bash
python scripts/slice_error_auditor.py path/to/predictions.csv --max-slice-gap 0.10
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `random split for temporal deployment` in `Findings` and `Risks`).
