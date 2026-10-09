# Clean Fixture: `stakeholder-insight-storyteller`

Prompt:

```text
Use $stakeholder-insight-storyteller on this clean request: Convert analysis into stakeholder-ready insight narratives that state decisions, evidence, uncertainty, and recommended action without overclaiming. The project provides analysis results, stakeholder audience, decision needed, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/memo_claim_evidence_check.py path/to/executive_memo.json
```

Expected decision: `go` (with documented assumptions and next action).
