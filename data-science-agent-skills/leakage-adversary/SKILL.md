---
name: leakage-adversary
description: Actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage. Use when Codex needs to handle data science workflows involving attack ml pipelines for leakage, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Leakage Adversary

## Mission

Actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage.

Current pain point: Models look excellent offline and fail in production because future or target information leaked into training.

Why this skill exists: Leakage must be attacked like a failure mode; ordinary metric review usually detects it too late.

## Required Inputs

- training data
- target definition
- split logic
- feature list
- pipeline code or notebook

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. Restate what information is available at decision time.
2. Probe features, joins, encoders, aggregations, and preprocessing for post-outcome information.
3. Check split logic for temporal bleed, group overlap, duplicated entities, and near-duplicates.
4. Review suspiciously strong features and validation performance jumps.
5. Return leakage findings with severity, evidence, and safer split or feature alternatives.

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
