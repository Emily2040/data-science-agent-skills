# Messy Fixture: `baseline-ablation-lab`

Prompt:

```text
Use $baseline-ablation-lab on a messy project where task type, dataset summary are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: no naive baseline.
```

Expected deterministic check:

```bash
python scripts/ablation_delta_audit.py path/to/comparison.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `no naive baseline` in `Findings` and `Risks`).
