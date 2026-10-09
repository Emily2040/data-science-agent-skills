# Clean Fixture: `data-question-framing`

Prompt:

```text
Use $data-question-framing on this clean request: Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements. The project provides raw stakeholder request, available decision or business context, known data sources or constraints, a named decision owner, and a clear action threshold.
```

Expected deterministic check:

```bash
python scripts/decision_canvas_validator.py path/to/decision_canvas.json
```

Expected decision: `go` (with documented assumptions and next action).
