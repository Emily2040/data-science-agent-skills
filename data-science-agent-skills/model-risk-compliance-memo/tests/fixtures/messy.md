# Messy Fixture: `model-risk-compliance-memo`

Prompt:

```text
Use $model-risk-compliance-memo on a messy project where model purpose, data sources are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: affected users undefined.
```

Expected deterministic check:

```bash
python scripts/risk_tier_gate.py path/to/risk_memo.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `affected users undefined` in `Findings` and `Risks`).
