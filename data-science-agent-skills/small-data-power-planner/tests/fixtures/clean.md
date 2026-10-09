# Clean Fixture: `small-data-power-planner`

Prompt:

```text
Use $small-data-power-planner on this clean request: Help teams decide what can be learned responsibly from small, imbalanced, expensive, or scarce datasets. The project provides sample size, outcome rate, candidate features, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/power_sample_size.py --n-per-arm 120 --baseline-std 1.0 --features 6 --events 90
```

Expected decision: `go` (with documented assumptions and next action).
