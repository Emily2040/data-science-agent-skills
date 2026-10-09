# Messy Fixture: `causal-assumption-scout`

Prompt:

```text
Use $causal-assumption-scout on a messy project where proposed claim, treatment or intervention are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: no intervention.
```

Expected deterministic check:

```bash
python scripts/confounder_backdoor_check.py path/to/causal_spec.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `no intervention` in `Findings` and `Risks`).
