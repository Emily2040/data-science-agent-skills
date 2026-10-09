---
name: causal-assumption-scout
description: Audit whether a data science claim requires causal identification rather than predictive correlation. Use when mapping treatments, outcomes, confounders, colliders, post-treatment controls, and quasi-experimental designs before claiming impact.
---

# Causal Assumption Scout

## Mission

Clarify when a data science request needs causal reasoning, what assumptions are required, and what evidence is missing.

Primary failure mode prevented: teams overclaim causal impact from observational models, dashboards, or correlations.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`proposed claim, treatment or intervention, outcome, population`) must be audited for red flags such as `no intervention`, `post-treatment controls`, `selection bias`, `unmeasured confounders`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/confounder_backdoor_check.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`no intervention`, `post-treatment controls`, `selection bias`, `unmeasured confounders`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Causal Assumption Scout decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `causal claim rewrite`, `assumption map`, `confounder checklist`, `method recommendation`, `safe-language memo`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/confounder_backdoor_check.py path/to/causal_spec.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Rewrite the claim as prediction, association, or causal effect.
2. Define treatment, outcome, population, time window, and estimand.
3. Draft a DAG-level assumption map and confounder inventory.
4. Recommend experiment, quasi-experiment, matching, weighting, regression, or do-not-claim-causality.
5. Return language that is safe for stakeholders and a sensitivity plan.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Causal Assumption Scout — Audit causal claims for confounding, collider bias, post-treatment controls, and identification.
- **简体中文**: 因果假设与识别侦察 — 审查因果推断诉求中的混杂偏倚、对撞因子、干预后控制变量与可识别性假设（参见 `references/multilingual-guide.md`）。
- **日本語**: 因果推論仮定スカウト — 交絡・合流点バイアス・処置後変数の統制・識別可能性を点検し因果主張の妥当性を審査（`references/multilingual-guide.md` を参照）。
- **한국어**: 인과 추론 가정 스카우트 — 교란변수·충돌변수(Collider)·처치 후 통제변수 및 식별 가능성을 점검하여 인과 주장 검증 (`references/multilingual-guide.md` 참조).

## Progressive References

- Read `references/multilingual-guide.md` when the user prompts in Simplified Chinese (简体中文), Japanese (日本語), or Korean (한국어), or requests a bilingual/multilingual decision memo.

- Read `references/playbook.md` for detailed step-by-step execution rules and escalation criteria.
- Read `references/quality-rubric.md` to score the output and verify that dataset red flags are separated from agent failure conditions.
- Read `references/acceptance-tests.md` and `references/benchmark-plan.md` when forward-testing clean, messy, and adversarial cases.
- Read `references/provider-interop.md` and `references/agent-portability.md` when adapting across cloud providers or agent hosts.

## Output Contract

Always return these exact eight sections in order:

1. `Problem`
2. `Inputs`
3. `Checks performed`
4. `Findings`
5. `Decision` (`go` | `fix-first` | `stop` | `proceed-with-risk` | `needs-owner-review`)
6. `Risks`
7. `Next actions`
8. `Artifacts`

## Final Checks

- Verify that every factual finding cites the exact file, column, metric, or script output that produced it.
- Run `python scripts/quick_validate_skill.py . --strict` after modifying any file in this skill package.
