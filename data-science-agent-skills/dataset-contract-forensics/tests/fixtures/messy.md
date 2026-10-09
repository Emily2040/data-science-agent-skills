# Messy Fixture: `dataset-contract-forensics`

Prompt:

```text
Use $dataset-contract-forensics on a messy project where CSV, Parquet, JSONL, SQL schema, or sample extracts, downstream use case are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: sample too small.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/extract.csv --max-rows 10000
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `sample too small` in `Findings` and `Risks`).
