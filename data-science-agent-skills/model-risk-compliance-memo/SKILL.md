---
name: model-risk-compliance-memo
description: Create concise model risk and compliance memos for review, audit, launch, or executive approval. Use when Codex needs to handle data science workflows involving create governance-ready model risk memos, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Model Risk Compliance Memo

## Mission

Create concise model risk and compliance memos for review, audit, launch, or executive approval.

Current pain point: Data science teams often lack a crisp artifact that explains model purpose, risk, evidence, limits, and controls.

Why this skill exists: A standard memo turns model risk from scattered notes into an approval-ready record.


## What This Skill Must Do

- Convert the request into an explicit Model Risk Compliance Memo decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: model purpose, data sources, users affected, evaluation evidence.
- Separate mechanical checks from judgment calls so another reviewer can audit the result.
- Return a decision-ready artifact with risks, owner questions, and the smallest next action.
- Refuse to hide uncertainty. Mark unknown, not applicable, and needs human owner review as separate states.

## Detailed Execution Rules

- Start by restating the decision this skill is meant to support.
- Inspect local artifacts before asking the user for missing context.
- Treat script output as evidence, not as the full answer.
- Preserve raw evidence and avoid silent mutation.
- Classify each blocker as stop, fix-first, monitor, accepted risk, or owner decision.
- Produce an artifact that another agent or human can review without hidden context.

## Red Flags

- affected users undefined
- no rollback owner
- fairness not evaluated where relevant
- privacy basis unclear
- monitoring absent

## Required Inputs

- model purpose
- data sources
- users affected
- evaluation evidence
- privacy and fairness concerns
- monitoring plan

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Define model purpose, non-goals, user impact, and decision authority.
2. Summarize data, training, evaluation, fairness, privacy, explainability, and limitations.
3. Classify risks by severity, likelihood, detectability, and owner.
4. Document controls, monitoring, rollback, and approval conditions.
5. Return a memo with open blockers and required signoffs.

## Resources

- Read `references/playbook.md` for the skill-specific checklist, decision rules, and failure modes.
- Read `references/acceptance-tests.md` when validating or forward-testing the skill.
- Read `references/infographic-spec.md` when creating the Reddit visual or social post.
- Use scripts in `scripts/` only on local files or explicit user-provided artifacts. Do not upload private data to external services.

## Output Contract

Return these sections unless the user requests another format:

- `Problem`: the decision, artifact, or workflow being handled.
- `Inputs`: files, data, assumptions, and missing context used.
- `Checks performed`: concrete inspections, scripts, and reasoning checks.
- `Findings`: prioritized observations with evidence.
- `Decision`: go, fix-first, stop, or proceed-with-risk recommendation.
- `Risks`: unresolved blockers, caveats, and owner decisions.
- `Next actions`: smallest useful follow-up steps.
- `Artifacts`: generated files, specs, or scripts.

## Final Checks

- Do not overclaim beyond available evidence.
- Mark assumptions explicitly instead of hiding them in prose.
- Prefer simple, auditable recommendations over impressive but fragile tooling.
- Preserve raw data and original artifacts unless the user explicitly asks for mutation.
- Keep the final answer short enough for a decision owner to act on.
