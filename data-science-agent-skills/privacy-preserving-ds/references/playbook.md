# Playbook

## Decision This Skill Supports

Guide data science work on sensitive data using minimization, local-first analysis, de-identification, synthetic data, or privacy-preserving methods.

## Evidence Checklist

- data schema or sample
- sensitive fields
- analysis goal
- approved environment
- sharing constraints

Also inspect any relevant schemas, notebooks, SQL, pipelines, configs, reports, model cards, experiment logs, tickets, dashboards, or incident notes.

## Execution Checklist

1. Identify direct identifiers, quasi-identifiers, sensitive attributes, and linkage risks.
2. Minimize fields and rows to the decision need.
3. Choose local-first, aggregated, redacted, synthetic, federated, differential privacy, or secure enclave path.
4. Define what can be exported, logged, cached, or shared.
5. Return a privacy-safe analysis plan and residual risk note.

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

- raw PII in notebook output
- unapproved cloud copy
- identifier kept for convenience
- synthetic data claimed risk-free
- exports not reviewed

## Senior Review Questions

- What would make this recommendation wrong?
- What evidence is missing but decision-critical?
- What has to be true at decision time, not just at analysis time?
- Which artifact lets another reviewer reproduce the check?
- Which stakeholder owns the risk?
