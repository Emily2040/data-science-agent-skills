# Clean Fixture: `baseline-ablation-lab`

Prompt:

```text
Use $baseline-ablation-lab on this clean request: Design honest baselines and ablations before complex models are accepted. The project provides task type, dataset summary, candidate model, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/ablation_delta_audit.py path/to/comparison.json
```

Expected decision: `go` (with documented assumptions and next action).
