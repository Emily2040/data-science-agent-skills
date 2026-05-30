# Evaluation Reality Check Acceptance Tests

Run these as forward-test prompts when changing the skill.

## Clean Case

Use $evaluation-reality-check for a clean case with complete inputs: task type, data generation process, deployment use.

Expected: produce the standard output contract, identify low residual risk, and name concrete artifacts.

## Messy Real-World Case

Use $evaluation-reality-check on a messy case where at least two inputs are missing, evidence is split across files, and ownership is unclear.

Expected: inspect available evidence first, separate blockers from nice-to-haves, and produce a fix-first plan.

## Adversarial Case

Use $evaluation-reality-check on an adversarial case where the requester wants a confident answer but the evidence triggers these risks: random split for temporal deployment, test set reused for tuning, no external validation for domain shift.

Expected: refuse to overclaim, mark missing evidence, and recommend stop or proceed-with-risk as appropriate.

## Pass Criteria

- Trigger metadata is specific to this workflow and does not collide with generic spreadsheet, visualization, or life-science database skills.
- The result includes evidence, assumptions, risks, and a next action.
- Any script-backed check has deterministic output and a clear failure status.
- Scripts are treated as support checks, not as complete replacements for expert review.
