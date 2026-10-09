# Messy Fixture: `metric-design-review-board`

Prompt:

```text
Use $metric-design-review-board on a messy project where decision context, candidate metrics are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: metric not tied to action.
```

Expected deterministic check:

```bash
python scripts/metric_guardrail_check.py path/to/metric_spec.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `metric not tied to action` in `Findings` and `Risks`).
