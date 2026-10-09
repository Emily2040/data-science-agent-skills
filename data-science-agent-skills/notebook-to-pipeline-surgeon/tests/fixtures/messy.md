# Messy Fixture: `notebook-to-pipeline-surgeon`

Prompt:

```text
Use $notebook-to-pipeline-surgeon on a messy project where notebook, target runtime are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: global mutable state.
```

Expected deterministic check:

```bash
python scripts/notebook_repro_audit.py path/to/notebook.ipynb
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `global mutable state` in `Findings` and `Risks`).
