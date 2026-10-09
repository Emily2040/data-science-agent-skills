# Messy Fixture: `leakage-adversary`

Prompt:

```text
Use $leakage-adversary on a messy project where training data, target definition are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: feature timestamp after target.
```

Expected deterministic check:

```bash
python scripts/split_leakage_probe.py path/to/train.csv path/to/eval.csv --key entity_id --target label
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `feature timestamp after target` in `Findings` and `Risks`).
