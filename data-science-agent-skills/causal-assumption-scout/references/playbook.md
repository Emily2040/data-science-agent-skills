# Playbook

## Decision This Skill Supports

Clarify when a data science request needs causal reasoning, what assumptions are required, and what evidence is missing.

## Evidence Checklist

- proposed claim
- treatment or intervention
- outcome
- population
- available covariates
- study design

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Rewrite the claim as prediction, association, or causal effect.
2. Define treatment, outcome, population, time window, and estimand.
3. Draft a DAG-level assumption map and confounder inventory.
4. Recommend experiment, quasi-experiment, matching, weighting, regression, or do-not-claim-causality.
5. Return language that is safe for stakeholders and a sensitivity plan.

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

- no intervention
- post-treatment controls
- selection bias
- unmeasured confounders
- effect framed after seeing results

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
