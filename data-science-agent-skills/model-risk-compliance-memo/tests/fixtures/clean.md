# Clean Fixture: `model-risk-compliance-memo`

Prompt:

```text
Use $model-risk-compliance-memo on this clean request: Create concise model risk and compliance memos for review, audit, launch, or executive approval. The project provides model purpose, data sources, users affected, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/risk_tier_gate.py path/to/risk_memo.json
```

Expected decision: `go` (with documented assumptions and next action).
