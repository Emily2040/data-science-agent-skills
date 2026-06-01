# Playbook

## Decision This Skill Supports

Plan compute use so data science experiments, model training, and inference stay within budget and latency constraints.

## Evidence Checklist

- task type
- data size
- model candidates
- cloud or local options
- budget
- deadline
- latency needs

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Estimate minimum useful experiment scale and define sample-first gates.
2. Compare local CPU, local GPU, cloud CPU, cloud GPU, batch, and spot options.
3. Plan caching, early stopping, checkpointing, and parallelism.
4. Set budget guardrails and cost per experiment or inference unit.
5. Return a compute plan with stop rules and escalation thresholds.

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

- full-data first run
- no budget owner
- idle GPU notebooks
- inference cost ignored
- training cheaper than monitoring is assumed

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
