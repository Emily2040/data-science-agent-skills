---
name: baseline-ablation-lab
description: Design honest baselines and ablations before complex models are accepted. Use when Codex needs to handle data science workflows involving force honest baselines and ablations, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Baseline Ablation Lab

## Mission

Design honest baselines and ablations before complex models are accepted.

Current pain point: Teams ship complex models without proving they outperform simple, cheaper, or safer alternatives.

Why this skill exists: Baselines and ablations reveal whether complexity adds real value or only narrative weight.

## Required Inputs

- task type
- dataset summary
- candidate model
- metric
- deployment constraints
- cost constraints

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Select task-appropriate naive, rule-based, statistical, and simple ML baselines.
2. Define ablations for features, model components, preprocessing, data volume, and inference cost.
3. Set metric and uncertainty reporting before running comparisons.
4. Identify complexity penalties: latency, maintainability, explainability, and monitoring burden.
5. Return a baseline and ablation matrix with accept/reject criteria.

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
