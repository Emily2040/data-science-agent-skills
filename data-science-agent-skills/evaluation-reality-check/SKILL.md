---
name: evaluation-reality-check
description: Design evaluation strategies that match task type, deployment setting, time, groups, and decision risk. Use when Codex needs to handle data science workflows involving design trustworthy model evaluation, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Evaluation Reality Check

## Mission

Design evaluation strategies that match task type, deployment setting, time, groups, and decision risk.

Current pain point: Offline evaluation often overstates real-world performance because splits, metrics, and benchmarks do not match deployment.

Why this skill exists: Evaluation must simulate the future decision surface, not just produce a leaderboard score.

## Required Inputs

- task type
- data generation process
- deployment use
- target and features
- metric
- risk level

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Identify whether the problem is tabular, time series, NLP, CV, ranking, recommendation, or anomaly detection.
2. Choose split strategy: temporal, grouped, stratified, rolling, external validation, or benchmark holdout.
3. Check leakage, label delay, distribution shift, uncertainty, and subgroup coverage.
4. Define confidence intervals, calibration, threshold testing, and failure slices.
5. Return an evaluation protocol and minimum launch evidence.

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
