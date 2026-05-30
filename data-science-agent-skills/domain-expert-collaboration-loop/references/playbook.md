# Domain Expert Collaboration Loop Playbook

## Core Checklist

- [ ] List assumptions that require domain validation.
- [ ] Prepare SME questions tied to decisions, not generic review.
- [ ] Capture evidence, objections, corrections, and unresolved uncertainty.
- [ ] Update analysis plan or model design based on review.
- [ ] Return an assumption ledger and signoff record.

## Expected Deliverables

- SME interview guide
- assumption ledger
- challenge-question list
- evidence log
- signoff and open-risk record

## Red Flags

- SME asked to rubber-stamp
- domain constraints undocumented
- agent inference treated as fact
- feedback not linked to changes
- signoff missing

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
