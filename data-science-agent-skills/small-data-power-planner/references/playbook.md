# Playbook

## Decision This Skill Supports

Help teams decide what can be learned responsibly from small, imbalanced, expensive, or scarce datasets.

## Evidence Checklist

- sample size
- outcome rate
- candidate features
- effect size of interest
- cost of errors
- collection options

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Identify the decision and minimum useful effect size.
2. Estimate signal limits, imbalance, uncertainty, and variance risks.
3. Recommend descriptive, Bayesian, resampling, regularized, or data-collection paths.
4. Define validation limits and language for uncertainty.
5. Return a do-model, simplify, or collect-more recommendation.

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

- more features than observations
- rare outcome with random split
- single holdout set only
- unreported uncertainty
- high-stakes decision from tiny sample

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
