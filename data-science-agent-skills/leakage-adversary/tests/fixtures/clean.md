# Clean Fixture: `leakage-adversary`

Prompt:

```text
Use $leakage-adversary on this clean request: Actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage. The project provides training data, target definition, split logic, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/split_leakage_probe.py path/to/train.csv path/to/eval.csv --key entity_id --target label
```

Expected decision: `go` (with documented assumptions and next action).
