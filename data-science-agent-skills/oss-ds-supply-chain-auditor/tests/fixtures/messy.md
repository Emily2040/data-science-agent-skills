# Messy Fixture: `oss-ds-supply-chain-auditor`

Prompt:

```text
Use $oss-ds-supply-chain-auditor on a messy project where repo path, environment files are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: pip install from unpinned URL.
```

Expected deterministic check:

```bash
python scripts/dependency_surface.py .
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `pip install from unpinned URL` in `Findings` and `Risks`).
