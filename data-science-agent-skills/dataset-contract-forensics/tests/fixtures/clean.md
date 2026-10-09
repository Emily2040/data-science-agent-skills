# Clean Fixture: `dataset-contract-forensics`

Prompt:

```text
Use $dataset-contract-forensics on this clean request: Infer practical data contracts, schema expectations, and validation tests from messy real datasets. The project provides CSV, Parquet, JSONL, SQL schema, or sample extracts, downstream use case, known business rules, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/extract.csv --max-rows 10000
```

Expected decision: `go` (with documented assumptions and next action).
