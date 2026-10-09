# Messy Fixture: `experiment-provenance-ledger`

Prompt:

```text
Use $experiment-provenance-ledger on a messy project where repo path, dataset identifiers are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: unversioned dataset.
```

Expected deterministic check:

```bash
python scripts/capture_provenance.py path/to/train.csv path/to/config.yaml --seed 42
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `unversioned dataset` in `Findings` and `Risks`).
