# Playbook

## Decision This Skill Supports

Design evaluation strategies that match task type, deployment setting, time, groups, and decision risk.

## Evidence Checklist

- task type
- data generation process
- deployment use
- target and features
- metric
- risk level

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Identify whether the problem is tabular, time series, NLP, CV, ranking, recommendation, or anomaly detection.
2. Choose split strategy: temporal, grouped, stratified, rolling, external validation, or benchmark holdout.
3. Check leakage, label delay, distribution shift, uncertainty, and subgroup coverage.
4. Define confidence intervals, calibration, threshold testing, and failure slices.
5. Return an evaluation protocol and minimum launch evidence.

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

- random split for temporal deployment
- test set reused for tuning
- no external validation for domain shift
- single aggregate metric
- label delay ignored

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
