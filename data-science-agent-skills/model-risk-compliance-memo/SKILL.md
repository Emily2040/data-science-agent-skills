---
name: model-risk-compliance-memo
description: Create concise model risk and compliance memos for review, audit, launch, or executive approval. Use when Codex needs to handle data science workflows involving create governance-ready model risk memos, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Model Risk Compliance Memo

## Mission

Create concise model risk and compliance memos for review, audit, launch, or executive approval.

Current pain point: Data science teams often lack a crisp artifact that explains model purpose, risk, evidence, limits, and controls.

Why this skill exists: A standard memo turns model risk from scattered notes into an approval-ready record.

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
