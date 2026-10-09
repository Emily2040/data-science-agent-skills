# Messy Fixture: `production-ml-handoff`

Prompt:

```text
Use $production-ml-handoff on a messy project where prototype repo or notebook, model artifact are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: notebook is only artifact.
```

Expected deterministic check:

```bash
python scripts/handoff_readiness_audit.py path/to/handoff_bundle.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `notebook is only artifact` in `Findings` and `Risks`).
