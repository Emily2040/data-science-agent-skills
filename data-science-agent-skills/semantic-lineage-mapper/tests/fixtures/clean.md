# Clean Fixture: `semantic-lineage-mapper`

Prompt:

```text
Use $semantic-lineage-mapper on this clean request: Reconstruct practical lineage across SQL, notebooks, scripts, dashboards, model artifacts, and pipeline configs. The project provides SQL files, notebooks, pipeline configs, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/extract_lineage_tokens.py sql/ pipelines/ notebooks/
```

Expected decision: `go` (with documented assumptions and next action).
