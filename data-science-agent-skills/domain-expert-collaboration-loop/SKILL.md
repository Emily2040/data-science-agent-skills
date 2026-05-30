---
name: domain-expert-collaboration-loop
description: Structure collaboration between data scientists, AI agents, and domain experts when domain judgment is required. Use when Codex needs to handle data science workflows involving structure sme review for agent-assisted ds, including requirements discovery, artifact review, risk analysis, implementation planning, or audit-ready reporting.
---

# Domain Expert Collaboration Loop

## Mission

Structure collaboration between data scientists, AI agents, and domain experts when domain judgment is required.

Current pain point: Agents and analysts can produce plausible work that misses domain constraints, tacit knowledge, and operational reality.

Why this skill exists: A disciplined SME loop captures assumptions, challenge questions, evidence, review decisions, and signoff.


## What This Skill Must Do

- Convert the request into an explicit Domain Expert Collaboration Loop decision rather than a loose analysis task.
- List the evidence used, the evidence missing, and the assumptions that are driving the recommendation.
- Run the skill workflow against local artifacts when available: analysis or model plan, domain experts, known constraints, critical assumptions.
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

- SME asked to rubber-stamp
- domain constraints undocumented
- agent inference treated as fact
- feedback not linked to changes
- signoff missing

## Required Inputs

- analysis or model plan
- domain experts
- known constraints
- critical assumptions
- review deadline
- decision owner

If an input is missing, inspect available files first. Ask only for information that cannot be recovered from the workspace and would change the recommendation.

## Workflow

1. List assumptions that require domain validation.
2. Prepare SME questions tied to decisions, not generic review.
3. Capture evidence, objections, corrections, and unresolved uncertainty.
4. Update analysis plan or model design based on review.
5. Return an assumption ledger and signoff record.

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
