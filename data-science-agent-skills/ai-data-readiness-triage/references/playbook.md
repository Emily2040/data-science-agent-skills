# Playbook

## Decision This Skill Supports

Assess whether a dataset or data domain is ready for AI, analytics, or modeling before a project commits time and budget.

## Evidence Checklist

- dataset paths or schemas
- data owner
- intended use case
- privacy or compliance constraints
- label or ground-truth plan

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Inventory access, ownership, lineage, refresh cadence, privacy, and retention constraints.
2. Profile quality, missingness, duplication, outliers, type drift, and label coverage.
3. Score readiness across governance, quality, representativeness, reproducibility, and operational fit.
4. Classify blockers as stop, fix-first, monitor, or accepted risk.
5. Return a readiness scorecard with the smallest credible next action.

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

- unknown owner
- no label source
- PII without approved use
- high missingness in core fields
- freshness mismatched to decision cycle

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
