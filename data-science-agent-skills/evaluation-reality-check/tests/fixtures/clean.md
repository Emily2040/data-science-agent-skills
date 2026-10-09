# Clean Fixture: `evaluation-reality-check`

Prompt:

```text
Use $evaluation-reality-check on this clean request: Design evaluation strategies that match task type, deployment setting, time, groups, and decision risk. The project provides task type, data generation process, deployment use, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/slice_error_auditor.py path/to/predictions.csv --max-slice-gap 0.10
```

Expected decision: `go` (with documented assumptions and next action).
