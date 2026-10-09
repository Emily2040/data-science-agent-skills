# Messy Fixture: `domain-expert-collaboration-loop`

Prompt:

```text
Use $domain-expert-collaboration-loop on a messy project where analysis or model plan, domain experts are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: SME asked to rubber-stamp.
```

Expected deterministic check:

```bash
python scripts/sme_label_agreement.py path/to/sme_labels.csv --rater-a sme_a --rater-b sme_b
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `SME asked to rubber-stamp` in `Findings` and `Risks`).
