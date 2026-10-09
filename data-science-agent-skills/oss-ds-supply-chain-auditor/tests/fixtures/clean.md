# Clean Fixture: `oss-ds-supply-chain-auditor`

Prompt:

```text
Use $oss-ds-supply-chain-auditor on this clean request: Audit open-source packages, notebooks, model weights, datasets, licenses, and provenance used in data science work. The project provides repo path, environment files, notebooks, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/dependency_surface.py .
```

Expected decision: `go` (with documented assumptions and next action).
