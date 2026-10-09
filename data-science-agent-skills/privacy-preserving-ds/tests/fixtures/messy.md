# Messy Fixture: `privacy-preserving-ds`

Prompt:

```text
Use $privacy-preserving-ds on a messy project where data schema or sample, sensitive fields are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: raw PII in notebook output.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/sensitive_extract.csv --max-rows 10000
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `raw PII in notebook output` in `Findings` and `Risks`).
