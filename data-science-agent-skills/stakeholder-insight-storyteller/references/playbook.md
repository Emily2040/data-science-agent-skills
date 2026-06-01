# Playbook

## Decision This Skill Supports

Convert analysis into stakeholder-ready insight narratives that state decisions, evidence, uncertainty, and recommended action without overclaiming.

## Evidence Checklist

- analysis results
- stakeholder audience
- decision needed
- uncertainties
- charts or tables
- recommended action

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Identify the single decision or belief update the audience needs.
2. Separate finding, implication, action, confidence, and caveat.
3. Choose chart and narrative order based on stakeholder task, not analyst chronology.
4. Remove unsupported causal, universal, or precision claims.
5. Return an executive memo or slide narrative with caveats and next actions.

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

- chart has no action
- claim exceeds design
- too many caveats with no priority
- audience not named
- uncertainty hidden

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
