# Playbook

## Decision This Skill Supports

Structure collaboration between data scientists, AI agents, and domain experts when domain judgment is required.

## Evidence Checklist

- analysis or model plan
- domain experts
- known constraints
- critical assumptions
- review deadline
- decision owner

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. List assumptions that require domain validation.
2. Prepare SME questions tied to decisions, not generic review.
3. Capture evidence, objections, corrections, and unresolved uncertainty.
4. Update analysis plan or model design based on review.
5. Return an assumption ledger and signoff record.

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

- SME asked to rubber-stamp
- domain constraints undocumented
- agent inference treated as fact
- feedback not linked to changes
- signoff missing

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
