# Playbook

## Decision This Skill Supports

Decide whether a feature store is needed and design features to avoid training-serving skew, staleness, and reuse confusion.

## Evidence Checklist

- feature list
- training data flow
- serving flow
- latency needs
- reuse demand
- ownership model

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Assess whether features need online serving, reuse, point-in-time correctness, or shared governance.
2. Check training-serving skew, freshness, TTL, backfill, and ownership risks.
3. Recommend no store, lightweight registry, batch feature table, or full feature store.
4. Define feature contracts and lineage requirements.
5. Return a readiness decision and migration plan.

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

- same feature computed differently online
- freshness unknown
- no point-in-time join
- feature owner unclear
- feature store proposed without reuse

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
