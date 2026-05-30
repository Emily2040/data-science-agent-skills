---
name: small-data-power-planner
description: Help teams decide what can be learned responsibly from small, imbalanced, expensive, or scarce datasets. Use when Codex needs to handle data science workflows involving avoid overfitting scarce data, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Small Data Power Planner

## Mission

Help teams decide what can be learned responsibly from small, imbalanced, expensive, or scarce datasets.

Current pain point: Small datasets are forced through high-capacity methods, producing unstable conclusions and overconfident narratives.

Why this skill exists: Power, uncertainty, resampling, priors, and simpler baselines must be planned before modeling scarce data.

## Required Inputs

- sample size
- outcome rate
- candidate features
- effect size of interest
- cost of errors
- collection options

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Identify the decision and minimum useful effect size.
2. Estimate signal limits, imbalance, uncertainty, and variance risks.
3. Recommend descriptive, Bayesian, resampling, regularized, or data-collection paths.
4. Define validation limits and language for uncertainty.
5. Return a do-model, simplify, or collect-more recommendation.

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
