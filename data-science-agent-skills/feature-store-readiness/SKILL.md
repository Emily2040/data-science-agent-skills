---
name: feature-store-readiness
description: Decide whether a feature store is needed and design features to avoid training-serving skew, staleness, and reuse confusion. Use when Codex needs to handle data science workflows involving decide when a feature store is worth it, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Feature Store Readiness

## Mission

Decide whether a feature store is needed and design features to avoid training-serving skew, staleness, and reuse confusion.

Current pain point: Teams either overbuild feature stores too early or underbuild shared feature governance until skew breaks models.

Why this skill exists: Feature-store readiness should be based on reuse, freshness, online serving, lineage, ownership, and skew risk.

## Required Inputs

- feature list
- training data flow
- serving flow
- latency needs
- reuse demand
- ownership model

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Assess whether features need online serving, reuse, point-in-time correctness, or shared governance.
2. Check training-serving skew, freshness, TTL, backfill, and ownership risks.
3. Recommend no store, lightweight registry, batch feature table, or full feature store.
4. Define feature contracts and lineage requirements.
5. Return a readiness decision and migration plan.

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
