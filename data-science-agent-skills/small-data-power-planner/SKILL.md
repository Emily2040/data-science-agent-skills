---
name: small-data-power-planner
description: Calculate minimum detectable effect (MDE), sample-size requirements, and events-per-variable ratios for small or rare-event datasets. Use when preventing underpowered experiments and overfitted models on scarce data.
---

# Small Data Power Planner

## Mission

Help teams decide what can be learned responsibly from small, imbalanced, expensive, or scarce datasets.

Primary failure mode prevented: small datasets are forced through high-capacity methods, producing unstable conclusions and overconfident narratives.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`sample size, outcome rate, candidate features, effect size of interest`) must be audited for red flags such as `more features than observations`, `rare outcome with random split`, `single holdout set only`, `unreported uncertainty`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/power_sample_size.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`more features than observations`, `rare outcome with random split`, `single holdout set only`, `unreported uncertainty`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Small Data Power Planner decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `power and uncertainty note`, `baseline plan`, `validation limits`, `collection recommendation`, `safe communication text`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/power_sample_size.py --n-per-arm 120 --baseline-std 1.0 --features 6 --events 90
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Identify the decision and minimum useful effect size.
2. Estimate signal limits, imbalance, uncertainty, and variance risks.
3. Recommend descriptive, Bayesian, resampling, regularized, or data-collection paths.
4. Define validation limits and language for uncertainty.
5. Return a do-model, simplify, or collect-more recommendation.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Small Data Power Planner — Calculate minimum detectable effect (MDE), sample power, and low-N overfitting bounds.
- **简体中文**: 小样本统计功效与容量规划 — 计算最小可检测效应（MDE）、统计功效与小样本过拟合边界（参见 `references/multilingual-guide.md`）。
- **日本語**: 小標本検出力・MDEプランナー — 最小検出可能効果（MDE）・統計的検出力・少数サンプルでの過学習境界を算出（`references/multilingual-guide.md` を参照）。
- **한국어**: 소표본 검정력·MDE 플래너 — 최소감지효과(MDE), 통계적 검정력, 소표본 과적합 경계(EPV)를 산출 (`references/multilingual-guide.md` 참조).

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
