# Messy Fixture: `small-data-power-planner`

Prompt:

```text
Use $small-data-power-planner on a messy project where sample size, outcome rate are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: more features than observations.
```

Expected deterministic check:

```bash
python scripts/power_sample_size.py --n-per-arm 120 --baseline-std 1.0 --features 6 --events 90
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `more features than observations` in `Findings` and `Risks`).
