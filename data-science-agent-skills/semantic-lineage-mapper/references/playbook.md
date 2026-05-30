# Semantic Lineage Mapper Playbook

## Core Checklist

- [ ] Extract table, column, file, feature, model, and artifact references.
- [ ] Group references into sources, transforms, outputs, and decision surfaces.
- [ ] Mark unknown or manually managed dependencies instead of dropping them.
- [ ] Identify high-risk nodes: ownerless, PII, stale, reused, or weakly documented.
- [ ] Return a lineage map, risk register, and confirmation checklist.

## Expected Deliverables

- lineage graph outline
- risk nodes
- owner questions
- unknown dependency list
- audit narrative

## Red Flags

- dashboard-only metric logic
- manual spreadsheet hop
- feature generated outside pipeline
- PII source unclear
- ownerless table

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
