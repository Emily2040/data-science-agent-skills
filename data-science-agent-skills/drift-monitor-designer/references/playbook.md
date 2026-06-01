# Playbook

## Decision This Skill Supports

Design drift monitoring for production models and data products across data, concept, performance, and operational signals.

## Evidence Checklist

- model purpose
- features
- prediction logs
- label availability
- risk tolerance
- owners
- retrain process

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Classify drift risks: schema, distribution, relationship, concept, performance, and operational drift.
2. Choose monitors based on data type, label delay, and actionability.
3. Set thresholds, baselines, alert routing, and suppression rules.
4. Define retrain, rollback, investigation, or no-action playbooks.
5. Return a monitor design and incident response path.

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

- alerts with no owner
- thresholds copied from defaults
- label delay ignored
- no baseline window
- retrain triggered without evaluation

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
