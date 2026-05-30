---
name: privacy-preserving-ds
description: Guide data science work on sensitive data using minimization, local-first analysis, de-identification, synthetic data, or privacy-preserving methods. Use when Codex needs to handle data science workflows involving choose safe analysis patterns for sensitive data, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Privacy Preserving Data Science

## Mission

Guide data science work on sensitive data using minimization, local-first analysis, de-identification, synthetic data, or privacy-preserving methods.

Current pain point: Teams copy sensitive data into notebooks and tools without a minimization or privacy strategy.

Why this skill exists: Privacy-preserving analysis is a design choice, not a cleanup step after exposure.

## Required Inputs

- data schema or sample
- sensitive fields
- analysis goal
- approved environment
- sharing constraints

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Identify direct identifiers, quasi-identifiers, sensitive attributes, and linkage risks.
2. Minimize fields and rows to the decision need.
3. Choose local-first, aggregated, redacted, synthetic, federated, differential privacy, or secure enclave path.
4. Define what can be exported, logged, cached, or shared.
5. Return a privacy-safe analysis plan and residual risk note.

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
