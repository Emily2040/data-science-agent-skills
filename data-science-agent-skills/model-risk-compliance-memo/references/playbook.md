# Playbook

## Decision This Skill Supports

Create concise model risk and compliance memos for review, audit, launch, or executive approval.

## Evidence Checklist

- model purpose
- data sources
- users affected
- evaluation evidence
- privacy and fairness concerns
- monitoring plan

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Define model purpose, non-goals, user impact, and decision authority.
2. Summarize data, training, evaluation, fairness, privacy, explainability, and limitations.
3. Classify risks by severity, likelihood, detectability, and owner.
4. Document controls, monitoring, rollback, and approval conditions.
5. Return a memo with open blockers and required signoffs.

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

- affected users undefined
- no rollback owner
- fairness not evaluated where relevant
- privacy basis unclear
- monitoring absent

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
