# Data Question Framing Playbook

## Core Checklist

- [ ] Extract the decision, action, and user or entity affected.
- [ ] Define the analysis unit, target, time horizon, and comparison baseline.
- [ ] Separate prediction, causal, descriptive, and operational questions.
- [ ] Choose success, guardrail, and decision metrics before any modeling plan.
- [ ] Return a decision canvas with assumptions and unresolved questions.

## Expected Deliverables

- decision canvas
- metric tree
- assumption log
- scope boundaries
- next evidence needed

## Red Flags

- no decision owner
- target unavailable at decision time
- metric can improve while user outcome worsens
- causal claim hidden inside prediction wording

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
