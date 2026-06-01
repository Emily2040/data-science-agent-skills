# Playbook

## Decision This Skill Supports

Preserve experiment provenance across code, data, environment, parameters, metrics, artifacts, and human decisions.

## Evidence Checklist

- repo path
- dataset identifiers
- environment files
- training command
- metrics
- artifact paths
- decision notes

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Capture code version, dirty state, environment, data references, parameters, seeds, and runtime.
2. Record metrics and artifacts with owner, purpose, and retention expectation.
3. Link human decisions, exclusions, and model-selection rationale.
4. Map entries to MLflow, DVC, W&B, or plain JSON depending on the stack.
5. Return a ledger and missing-provenance risk list.

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

- unversioned dataset
- dirty code used for final metric
- missing seed
- manual artifact rename
- model chosen without logged rationale

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
