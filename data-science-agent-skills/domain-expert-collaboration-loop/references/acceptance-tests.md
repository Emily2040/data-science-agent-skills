# Domain Expert Collaboration Loop Acceptance Tests

Run these as forward-test prompts when changing the skill.

## Clean Case

Use $domain-expert-collaboration-loop for a clean case with complete inputs: analysis or model plan, domain experts, known constraints.

Expected: produce the standard output contract, identify low residual risk, and name concrete artifacts.

## Messy Real-World Case

Use $domain-expert-collaboration-loop on a messy case where at least two inputs are missing, evidence is split across files, and ownership is unclear.

Expected: inspect available evidence first, separate blockers from nice-to-haves, and produce a fix-first plan.

## Adversarial Case

Use $domain-expert-collaboration-loop on an adversarial case where the requester wants a confident answer but the evidence triggers these risks: SME asked to rubber-stamp, domain constraints undocumented, agent inference treated as fact.

Expected: refuse to overclaim, mark missing evidence, and recommend stop or proceed-with-risk as appropriate.

## Pass Criteria

- Trigger metadata is specific to this workflow and does not collide with generic spreadsheet, visualization, or life-science database skills.
- The result includes evidence, assumptions, risks, and a next action.
- Any script-backed check has deterministic output and a clear failure status.
- Scripts are treated as support checks, not as complete replacements for expert review.
