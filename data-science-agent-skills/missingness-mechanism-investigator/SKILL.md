---
name: missingness-mechanism-investigator
description: Diagnose whether missing data is MCAR, MAR, MNAR, or structurally absent before applying imputation or row deletion. Use when profiling column missingness rates, cross-tabulating missingness against outcomes, and choosing safe handling rules.
---

# Missingness Mechanism Investigator

## Mission

Diagnose missing-data mechanisms and design imputation, exclusion, or sensitivity plans.

Primary failure mode prevented: missing values are filled or dropped mechanically, creating bias and false confidence.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`dataset, analysis goal, column meanings, collection process`) must be audited for red flags such as `target-dependent missingness`, `structural missing treated as random`, `imputed identifiers`, `dropped rows change population`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/profile_table.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`target-dependent missingness`, `structural missing treated as random`, `imputed identifiers`, `dropped rows change population`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Missingness Mechanism Investigator decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `missingness heat map summary`, `mechanism labels`, `imputation plan`, `sensitivity plan`, `claim limitations`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/profile_table.py path/to/dataset.csv --max-rows 10000
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Profile missingness by column, row, group, time, and target relationship.
2. Classify likely mechanisms as MCAR, MAR, MNAR, structural missing, or unknown.
3. Identify whether missingness itself should be a feature, exclusion reason, or bias warning.
4. Recommend complete-case, imputation, indicator, model-based, or sensitivity strategy.
5. Return a missingness report with assumptions and impact on claims.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Missingness Mechanism Investigator — Diagnose MCAR, MAR, and MNAR missingness and block naive imputation traps.
- **简体中文**: 缺失机制诊断（MCAR / MAR / MNAR） — 诊断完全随机、随机与非随机缺失机制，防范盲目均值插补或删行偏倚（参见 `references/multilingual-guide.md`）。
- **日本語**: 欠測メカニズム調査（MCAR / MAR / MNAR） — 欠測がMCAR・MAR・MNARのいずれかを診断し、安易な平均値補完や行削除によるバイアスを防止（`references/multilingual-guide.md` を参照）。
- **한국어**: 결측 메커니즘 조사기 (MCAR / MAR / MNAR) — 결측치의 MCAR·MAR·MNAR 메커니즘을 진단하고 단순 평균 대체·행 삭제 편향을 방지 (`references/multilingual-guide.md` 참조).

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
