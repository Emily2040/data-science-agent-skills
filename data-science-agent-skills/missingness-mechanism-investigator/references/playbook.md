# Playbook

## Decision This Skill Supports

Diagnose missing-data mechanisms and design imputation, exclusion, or sensitivity plans.

## Evidence Checklist

- dataset
- analysis goal
- column meanings
- collection process
- known reasons for missingness

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Profile missingness by column, row, group, time, and target relationship.
2. Classify likely mechanisms as MCAR, MAR, MNAR, structural missing, or unknown.
3. Identify whether missingness itself should be a feature, exclusion reason, or bias warning.
4. Recommend complete-case, imputation, indicator, model-based, or sensitivity strategy.
5. Return a missingness report with assumptions and impact on claims.

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

- target-dependent missingness
- structural missing treated as random
- imputed identifiers
- dropped rows change population
- no collection-process explanation

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
