# Messy Fixture: `feature-store-readiness`

Prompt:

```text
Use $feature-store-readiness on a messy project where feature list, training data flow are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: same feature computed differently online.
```

Expected deterministic check:

```bash
python scripts/online_offline_skew_check.py path/to/offline.csv path/to/online.csv --key entity_id
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `same feature computed differently online` in `Findings` and `Risks`).
