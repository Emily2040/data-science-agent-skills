# Clean Fixture: `experiment-provenance-ledger`

Prompt:

```text
Use $experiment-provenance-ledger on this clean request: Preserve experiment provenance across code, data, environment, parameters, metrics, artifacts, and human decisions. The project provides repo path, dataset identifiers, environment files, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/capture_provenance.py path/to/train.csv path/to/config.yaml --seed 42
```

Expected decision: `go` (with documented assumptions and next action).
