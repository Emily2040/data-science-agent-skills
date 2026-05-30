# Playbook

## Decision This Skill Supports

Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements.

## Evidence Checklist

- raw stakeholder request
- available decision or business context
- known data sources or constraints
- deadline and decision owner

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Extract the decision, action, and user or entity affected.
2. Define the analysis unit, target, time horizon, and comparison baseline.
3. Separate prediction, causal, descriptive, and operational questions.
4. Choose success, guardrail, and decision metrics before any modeling plan.
5. Return a decision canvas with assumptions and unresolved questions.

## Decision Ladder

- `go`: evidence is sufficient and red flags are absent or accepted by the owner.
- `fix-first`: a concrete blocker can be remediated before continuing.
- `stop`: the work would be misleading, unsafe, unlawful, or untestable.
- `proceed-with-risk`: the owner accepts named risks and monitoring is specified.
- `needs-owner-review`: the agent cannot decide without a human owner.

## Evidence Table Template

| Finding | Evidence | Confidence | Owner action |
| --- | --- | --- | --- |
| Fill this row | File, query, metric, or observation | high/medium/low | go/fix/stop/review |

## Red Flags

- no decision owner
- target unavailable at decision time
- metric can improve while user outcome worsens
- causal claim hidden inside prediction wording

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
