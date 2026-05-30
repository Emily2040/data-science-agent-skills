# Experiment Provenance Ledger Acceptance Tests

Run these as forward-test prompts when changing the skill.

## Clean Case

Use $experiment-provenance-ledger for a clean case with complete inputs: repo path, dataset identifiers, environment files.

Expected: produce the standard output contract, identify low residual risk, and name concrete artifacts.

## Messy Real-World Case

Use $experiment-provenance-ledger on a messy case where at least two inputs are missing, evidence is split across files, and ownership is unclear.

Expected: inspect available evidence first, separate blockers from nice-to-haves, and produce a fix-first plan.

## Adversarial Case

Use $experiment-provenance-ledger on an adversarial case where the requester wants a confident answer but the evidence triggers these risks: unversioned dataset, dirty code used for final metric, missing seed.

Expected: refuse to overclaim, mark missing evidence, and recommend stop or proceed-with-risk as appropriate.

## Pass Criteria

- Trigger metadata is specific to this workflow and does not collide with generic spreadsheet, visualization, or life-science database skills.
- The result includes evidence, assumptions, risks, and a next action.
- Any script-backed check has deterministic output and a clear failure status.
- Scripts are treated as support checks, not as complete replacements for expert review.
