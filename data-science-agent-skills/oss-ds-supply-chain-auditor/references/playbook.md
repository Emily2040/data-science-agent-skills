# OSS Data Science Supply Chain Auditor Playbook

## Core Checklist

- [ ] Inventory Python, R, system, notebook, model, and dataset dependencies.
- [ ] Flag unknown sources, unsafe install patterns, large binary artifacts, and license uncertainty.
- [ ] Review notebooks for shell execution, remote downloads, credential exposure, and hidden outputs.
- [ ] Create a DS SBOM-style summary with risk levels and remediation priorities.
- [ ] Return a supply-chain risk report and minimum cleanup plan.

## Expected Deliverables

- DS dependency inventory
- model and dataset provenance table
- license risk list
- notebook risk findings
- remediation plan

## Red Flags

- pip install from unpinned URL
- unknown model weights
- dataset license absent
- notebook output leaks secrets
- native binary dependency unreviewed

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
