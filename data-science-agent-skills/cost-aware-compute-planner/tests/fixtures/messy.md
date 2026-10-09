# Messy Fixture: `cost-aware-compute-planner`

Prompt:

```text
Use $cost-aware-compute-planner on a messy project where task type, data size are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: full-data first run.
```

Expected deterministic check:

```bash
python scripts/compute_budget_estimator.py --hours 4 --hourly-rate 3.5 --runs 6 --failure-rate 0.15 --budget 100
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `full-data first run` in `Findings` and `Risks`).
