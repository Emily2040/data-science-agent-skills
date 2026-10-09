# Clean Fixture: `domain-expert-collaboration-loop`

Prompt:

```text
Use $domain-expert-collaboration-loop on this clean request: Structure collaboration between data scientists, AI agents, and domain experts when domain judgment is required. The project provides analysis or model plan, domain experts, known constraints, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/sme_label_agreement.py path/to/sme_labels.csv --rater-a sme_a --rater-b sme_b
```

Expected decision: `go` (with documented assumptions and next action).
