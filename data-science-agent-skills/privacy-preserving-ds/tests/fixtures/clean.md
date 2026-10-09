# Clean Fixture: `privacy-preserving-ds`

Prompt:

```text
Use $privacy-preserving-ds on this clean request: Guide data science work on sensitive data using minimization, local-first analysis, de-identification, synthetic data, or privacy-preserving methods. The project provides data schema or sample, sensitive fields, analysis goal, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/profile_table.py path/to/sensitive_extract.csv --max-rows 10000
```

Expected decision: `go` (with documented assumptions and next action).
