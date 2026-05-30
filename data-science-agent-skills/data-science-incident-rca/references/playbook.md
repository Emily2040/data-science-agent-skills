# Playbook

## Decision This Skill Supports

Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions.

## Evidence Checklist

- incident symptom
- time first observed
- affected outputs
- recent changes
- logs or metrics
- owners

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Define symptom, detection path, start time, severity, and affected users or decisions.
2. Build timeline across data sources, pipelines, code, model, dashboard, and human changes.
3. Separate root cause, contributing factors, detection gaps, and impact.
4. Recommend immediate mitigation, durable prevention, monitoring, and ownership updates.
5. Return an RCA memo with evidence and countermeasures.

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

- no timestamped evidence
- only one layer investigated
- impact not quantified
- human process omitted
- countermeasure lacks owner

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
