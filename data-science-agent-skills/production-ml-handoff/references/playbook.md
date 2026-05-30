# Playbook

## Decision This Skill Supports

Convert data science prototypes into engineering-ready ML handoffs with contracts, artifacts, SLOs, monitoring, and ownership.

## Evidence Checklist

- prototype repo or notebook
- model artifact
- feature inputs
- serving pattern
- SLOs
- owners
- monitoring needs

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Define inference contract: inputs, outputs, types, thresholds, errors, latency, and privacy constraints.
2. Package artifacts, versioning, environment, and reproducibility evidence.
3. Specify deployment path, rollback, monitoring, alerting, and ownership.
4. Identify engineering blockers and unresolved research assumptions.
5. Return a handoff brief and acceptance checklist.

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

- notebook is only artifact
- feature definitions ambiguous
- no rollback plan
- latency unknown
- owner unclear after launch

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
