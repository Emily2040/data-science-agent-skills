# Playbook

## Decision This Skill Supports

Actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage.

## Evidence Checklist

- training data
- target definition
- split logic
- feature list
- pipeline code or notebook

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Restate what information is available at decision time.
2. Probe features, joins, encoders, aggregations, and preprocessing for post-outcome information.
3. Check split logic for temporal bleed, group overlap, duplicated entities, and near-duplicates.
4. Review suspiciously strong features and validation performance jumps.
5. Return leakage findings with severity, evidence, and safer split or feature alternatives.

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

- feature timestamp after target
- same user in train and test
- global preprocessing before split
- leaky aggregate
- near-perfect simple model

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
