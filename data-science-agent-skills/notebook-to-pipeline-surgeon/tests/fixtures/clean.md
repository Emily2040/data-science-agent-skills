# Clean Fixture: `notebook-to-pipeline-surgeon`

Prompt:

```text
Use $notebook-to-pipeline-surgeon on this clean request: Convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks. The project provides notebook, target runtime, data locations, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/notebook_repro_audit.py path/to/notebook.ipynb
```

Expected decision: `go` (with documented assumptions and next action).
