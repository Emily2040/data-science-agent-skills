# Clean Fixture: `feature-store-readiness`

Prompt:

```text
Use $feature-store-readiness on this clean request: Decide whether a feature store is needed and design features to avoid training-serving skew, staleness, and reuse confusion. The project provides feature list, training data flow, serving flow, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/online_offline_skew_check.py path/to/offline.csv path/to/online.csv --key entity_id
```

Expected decision: `go` (with documented assumptions and next action).
