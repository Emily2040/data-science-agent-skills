# Messy Fixture: `notebook-repro-packager`

Prompt:

```text
Use $notebook-repro-packager on a messy project where notebook files, data dependencies are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: out-of-order execution.
```

Expected deterministic check:

```bash
python scripts/notebook_repro_audit.py path/to/notebook.ipynb
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `out-of-order execution` in `Findings` and `Risks`).
