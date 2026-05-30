# Playbook

## Decision This Skill Supports

Reconstruct practical lineage across SQL, notebooks, scripts, dashboards, model artifacts, and pipeline configs.

## Evidence Checklist

- SQL files
- notebooks
- pipeline configs
- dashboard definitions
- model feature lists

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Extract table, column, file, feature, model, and artifact references.
2. Group references into sources, transforms, outputs, and decision surfaces.
3. Mark unknown or manually managed dependencies instead of dropping them.
4. Identify high-risk nodes: ownerless, PII, stale, reused, or weakly documented.
5. Return a lineage map, risk register, and confirmation checklist.

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

- dashboard-only metric logic
- manual spreadsheet hop
- feature generated outside pipeline
- PII source unclear
- ownerless table

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
