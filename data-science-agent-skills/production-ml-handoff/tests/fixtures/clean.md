# Clean Fixture: `production-ml-handoff`

Prompt:

```text
Use $production-ml-handoff on this clean request: Convert data science prototypes into engineering-ready ML handoffs with contracts, artifacts, SLOs, monitoring, and ownership. The project provides prototype repo or notebook, model artifact, feature inputs, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/handoff_readiness_audit.py path/to/handoff_bundle.json
```

Expected decision: `go` (with documented assumptions and next action).
