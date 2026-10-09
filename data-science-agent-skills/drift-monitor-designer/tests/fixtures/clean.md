# Clean Fixture: `drift-monitor-designer`

Prompt:

```text
Use $drift-monitor-designer on this clean request: Design drift monitoring for production models and data products across data, concept, performance, and operational signals. The project provides model purpose, features, prediction logs, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/drift_probe.py path/to/baseline.csv path/to/current.csv
```

Expected decision: `go` (with documented assumptions and next action).
