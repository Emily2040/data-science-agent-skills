# Playbook

## Decision This Skill Supports

Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order.

## Evidence Checklist

- notebook files
- data dependencies
- environment files
- expected outputs
- runtime constraints

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Audit execution order, hidden state, hard-coded paths, missing seeds, and external dependencies.
2. Capture environment, data manifest, run command, and expected output checks.
3. Separate exploratory cells from required run path.
4. Add smoke-test guidance and failure messages.
5. Return a reproducibility package checklist and patch plan.

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

- out-of-order execution
- local absolute paths
- unseeded randomness
- implicit data downloads
- manual cell edits required

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
