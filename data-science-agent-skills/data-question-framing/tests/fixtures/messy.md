# Messy Fixture: `data-question-framing`

Prompt:

```text
Use $data-question-framing on a messy project where raw stakeholder request, available decision or business context are incomplete, ownership is ambiguous, and local inspection reveals a critical red flag: no decision owner.
```

Expected deterministic check:

```bash
python scripts/decision_canvas_validator.py path/to/decision_canvas.json
```

Expected decision: `fix-first` or `needs-owner-review` (must surface `no decision owner` in `Findings` and `Risks`).
