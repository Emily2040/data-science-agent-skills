# Playbook

## Decision This Skill Supports

Design honest baselines and ablations before complex models are accepted.

## Evidence Checklist

- task type
- dataset summary
- candidate model
- metric
- deployment constraints
- cost constraints

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Select task-appropriate naive, rule-based, statistical, and simple ML baselines.
2. Define ablations for features, model components, preprocessing, data volume, and inference cost.
3. Set metric and uncertainty reporting before running comparisons.
4. Identify complexity penalties: latency, maintainability, explainability, and monitoring burden.
5. Return a baseline and ablation matrix with accept/reject criteria.

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

- no naive baseline
- single random seed
- improvement below uncertainty
- cost ignored
- feature ablations missing

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
