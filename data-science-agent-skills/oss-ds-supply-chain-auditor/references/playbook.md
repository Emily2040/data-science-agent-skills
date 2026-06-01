# Playbook

## Decision This Skill Supports

Audit open-source packages, notebooks, model weights, datasets, licenses, and provenance used in data science work.

## Evidence Checklist

- repo path
- environment files
- notebooks
- model artifact paths
- dataset sources
- license expectations

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Inventory Python, R, system, notebook, model, and dataset dependencies.
2. Flag unknown sources, unsafe install patterns, large binary artifacts, and license uncertainty.
3. Review notebooks for shell execution, remote downloads, credential exposure, and hidden outputs.
4. Create a DS SBOM-style summary with risk levels and remediation priorities.
5. Return a supply-chain risk report and minimum cleanup plan.

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

- pip install from unpinned URL
- unknown model weights
- dataset license absent
- notebook output leaks secrets
- native binary dependency unreviewed

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
