# Clean Fixture: `causal-assumption-scout`

Prompt:

```text
Use $causal-assumption-scout on this clean request: Clarify when a data science request needs causal reasoning, what assumptions are required, and what evidence is missing. The project provides proposed claim, treatment or intervention, outcome, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/confounder_backdoor_check.py path/to/causal_spec.json
```

Expected decision: `go` (with documented assumptions and next action).
