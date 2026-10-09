# Messy Fixture: `drift-monitor-designer`

Prompt:

```text
Use $drift-monitor-designer on a messy project where model purpose, features are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: alerts with no owner.
```

Expected deterministic check:

```bash
python scripts/drift_probe.py path/to/baseline.csv path/to/current.csv
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `alerts with no owner` in `Findings` and `Risks`).
