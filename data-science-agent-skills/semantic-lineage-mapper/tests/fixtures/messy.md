# Messy Fixture: `semantic-lineage-mapper`

Prompt:

```text
Use $semantic-lineage-mapper on a messy project where SQL files, notebooks are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: dashboard-only metric logic.
```

Expected deterministic check:

```bash
python scripts/extract_lineage_tokens.py sql/ pipelines/ notebooks/
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `dashboard-only metric logic` in `Findings` and `Risks`).
