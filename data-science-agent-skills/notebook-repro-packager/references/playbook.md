# Notebook Repro Packager Playbook

## Core Checklist

- [ ] Audit execution order, hidden state, hard-coded paths, missing seeds, and external dependencies.
- [ ] Capture environment, data manifest, run command, and expected output checks.
- [ ] Separate exploratory cells from required run path.
- [ ] Add smoke-test guidance and failure messages.
- [ ] Return a reproducibility package checklist and patch plan.

## Expected Deliverables

- notebook audit
- environment manifest
- data manifest
- run instructions
- smoke-test plan

## Red Flags

- out-of-order execution
- local absolute paths
- unseeded randomness
- implicit data downloads
- manual cell edits required

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
