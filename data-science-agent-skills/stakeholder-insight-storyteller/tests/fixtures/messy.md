# Messy Fixture: `stakeholder-insight-storyteller`

Prompt:

```text
Use $stakeholder-insight-storyteller on a messy project where analysis results, stakeholder audience are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: chart has no action.
```

Expected deterministic check:

```bash
python scripts/memo_claim_evidence_check.py path/to/executive_memo.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `chart has no action` in `Findings` and `Risks`).
