---
name: metric-design-review-board
description: Review whether a chosen data science metric actually supports the decision, user outcome, risk, and cost tradeoff. Use when Codex needs to handle data science workflows involving align metrics with real decisions, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Metric Design Review Board

## Mission

Review whether a chosen data science metric actually supports the decision, user outcome, risk, and cost tradeoff.

Current pain point: Projects optimize metrics that look scientific but misalign with business impact or safety.

Why this skill exists: Metric design is a governance problem: success, guardrails, thresholds, and cost curves must be decided together.

## Required Inputs

- decision context
- candidate metrics
- stakeholders
- false positive and false negative costs
- guardrails

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Map metrics to the real decision and affected user or entity.
2. Separate primary, diagnostic, fairness, reliability, and guardrail metrics.
3. Review threshold effects, class imbalance, cost asymmetry, and gaming risk.
4. Check offline-online and proxy-outcome mismatch.
5. Return a metric board decision with acceptance and monitoring criteria.

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
