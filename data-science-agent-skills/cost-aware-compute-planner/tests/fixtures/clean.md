# Clean Fixture: `cost-aware-compute-planner`

Prompt:

```text
Use $cost-aware-compute-planner on this clean request: Plan compute use so data science experiments, model training, and inference stay within budget and latency constraints. The project provides task type, data size, model candidates, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/compute_budget_estimator.py --hours 4 --hourly-rate 3.5 --runs 6 --failure-rate 0.15 --budget 100
```

Expected decision: `go` (with documented assumptions and next action).
