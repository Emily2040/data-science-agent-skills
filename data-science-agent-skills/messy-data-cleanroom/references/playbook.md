# Messy Data Cleanroom Playbook

## Core Checklist

- [ ] Profile missingness, duplicates, outliers, types, formats, units, and conflicting records.
- [ ] Separate factual corrections, normalization, exclusions, imputations, and unresolved anomalies.
- [ ] For each proposed transformation, record rationale, affected rows, risk, and reversal method.
- [ ] Prefer derived clean columns or versioned outputs over overwriting raw evidence.
- [ ] Return a cleaning ledger and transformed-data acceptance criteria.

## Expected Deliverables

- cleaning ledger
- transformation plan
- row impact summary
- reversal plan
- review questions

## Red Flags

- overwriting raw data
- dropping rows without impact analysis
- unit conversion not documented
- outlier removal tied to desired result

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
