# Clean Fixture: `metric-design-review-board`

Prompt:

```text
Use $metric-design-review-board on this clean request: Review whether a chosen data science metric actually supports the decision, user outcome, risk, and cost tradeoff. The project provides decision context, candidate metrics, stakeholders, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/metric_guardrail_check.py path/to/metric_spec.json
```

Expected decision: `go` (with documented assumptions and next action).
