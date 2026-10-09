# Clean Fixture: `notebook-repro-packager`

Prompt:

```text
Use $notebook-repro-packager on this clean request: Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order. The project provides notebook files, data dependencies, environment files, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/notebook_repro_audit.py path/to/notebook.ipynb
```

Expected decision: `go` (with documented assumptions and next action).
