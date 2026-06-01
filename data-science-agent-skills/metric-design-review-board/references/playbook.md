# Playbook

## Decision This Skill Supports

Review whether a chosen data science metric actually supports the decision, user outcome, risk, and cost tradeoff.

## Evidence Checklist

- decision context
- candidate metrics
- stakeholders
- false positive and false negative costs
- guardrails

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Map metrics to the real decision and affected user or entity.
2. Separate primary, diagnostic, fairness, reliability, and guardrail metrics.
3. Review threshold effects, class imbalance, cost asymmetry, and gaming risk.
4. Check offline-online and proxy-outcome mismatch.
5. Return a metric board decision with acceptance and monitoring criteria.

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

- metric not tied to action
- proxy metric can be gamed
- threshold chosen after results
- guardrails missing
- average hides subgroup harm

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
