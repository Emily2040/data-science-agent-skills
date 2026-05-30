# Evaluation Reality Check Playbook

## Core Checklist

- [ ] Identify whether the problem is tabular, time series, NLP, CV, ranking, recommendation, or anomaly detection.
- [ ] Choose split strategy: temporal, grouped, stratified, rolling, external validation, or benchmark holdout.
- [ ] Check leakage, label delay, distribution shift, uncertainty, and subgroup coverage.
- [ ] Define confidence intervals, calibration, threshold testing, and failure slices.
- [ ] Return an evaluation protocol and minimum launch evidence.

## Expected Deliverables

- evaluation protocol
- split recommendation
- failure-slice plan
- uncertainty report
- launch evidence checklist

## Red Flags

- random split for temporal deployment
- test set reused for tuning
- no external validation for domain shift
- single aggregate metric
- label delay ignored

## Decision Rules

- `go`: critical evidence is available, risks are owned, and the next action is reversible or monitored.
- `fix-first`: the work is valuable but at least one blocker must be remediated before modeling, launch, or stakeholder use.
- `stop`: the request is misframed, unsafe, untestable, or materially misleading with available evidence.
- `proceed-with-risk`: the user accepts named risks and the report includes monitoring or rollback conditions.

## Evidence Discipline

- Tie every recommendation to a file, metric, stakeholder claim, or explicit assumption.
- Separate mechanically observed facts from expert judgment.
- Use uncertainty language when the evidence is partial.
- Record unresolved owner questions rather than filling gaps with confident guesses.
