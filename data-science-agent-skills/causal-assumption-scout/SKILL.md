---
name: causal-assumption-scout
description: Clarify when a data science request needs causal reasoning, what assumptions are required, and what evidence is missing. Use when Codex needs to handle data science workflows involving stop predictive work from pretending causality, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Causal Assumption Scout

## Mission

Clarify when a data science request needs causal reasoning, what assumptions are required, and what evidence is missing.

Current pain point: Teams overclaim causal impact from observational models, dashboards, or correlations.

Why this skill exists: Causal claims need explicit estimand, intervention, confounders, assumptions, and sensitivity checks.

## Required Inputs

- proposed claim
- treatment or intervention
- outcome
- population
- available covariates
- study design

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Rewrite the claim as prediction, association, or causal effect.
2. Define treatment, outcome, population, time window, and estimand.
3. Draft a DAG-level assumption map and confounder inventory.
4. Recommend experiment, quasi-experiment, matching, weighting, regression, or do-not-claim-causality.
5. Return language that is safe for stakeholders and a sensitivity plan.

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
