# Feature Store Readiness Acceptance Tests

Run these as forward-test prompts when changing the skill.

## Clean Case

Use $feature-store-readiness for a clean case with complete inputs: feature list, training data flow, serving flow.

Expected: produce the standard output contract, identify low residual risk, and name concrete artifacts.

## Messy Real-World Case

Use $feature-store-readiness on a messy case where at least two inputs are missing, evidence is split across files, and ownership is unclear.

Expected: inspect available evidence first, separate blockers from nice-to-haves, and produce a fix-first plan.

## Adversarial Case

Use $feature-store-readiness on an adversarial case where the requester wants a confident answer but the evidence triggers these risks: same feature computed differently online, freshness unknown, no point-in-time join.

Expected: refuse to overclaim, mark missing evidence, and recommend stop or proceed-with-risk as appropriate.

## Pass Criteria

- Trigger metadata is specific to this workflow and does not collide with generic spreadsheet, visualization, or life-science database skills.
- The result includes evidence, assumptions, risks, and a next action.
- Any script-backed check has deterministic output and a clear failure status.
- Scripts are treated as support checks, not as complete replacements for expert review.
