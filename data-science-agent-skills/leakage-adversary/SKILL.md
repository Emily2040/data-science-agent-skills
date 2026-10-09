---
name: leakage-adversary
description: Hunt for target, temporal, entity-group, preprocessing, and join leakage across train, validation, and test splits. Use when probing datasets and pipelines for split key overlap, post-outcome features, or suspiciously high validation scores.
---

# Leakage Adversary

## Mission

Actively search ML datasets and pipelines for target, temporal, group, split, join, and preprocessing leakage.

Primary failure mode prevented: models look excellent offline and fail in production because future or target information leaked into training.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`training data, target definition, split logic, feature list`) must be audited for red flags such as `feature timestamp after target`, `same user in train and test`, `global preprocessing before split`, `leaky aggregate`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/split_leakage_probe.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`feature timestamp after target`, `same user in train and test`, `global preprocessing before split`, `leaky aggregate`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Leakage Adversary decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `leakage attack report`, `feature risk table`, `split risk table`, `safe evaluation recommendation`, `blocker list`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/split_leakage_probe.py path/to/train.csv path/to/eval.csv --key entity_id --target label
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Restate what information is available at decision time.
2. Probe features, joins, encoders, aggregations, and preprocessing for post-outcome information.
3. Check split logic for temporal bleed, group overlap, duplicated entities, and near-duplicates.
4. Review suspiciously strong features and validation performance jumps.
5. Return leakage findings with severity, evidence, and safer split or feature alternatives.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Leakage Adversary — Red-team ML datasets and pipelines for target, temporal, group, and preprocessing leakage.
- **简体中文**: 数据泄漏红队审计 — 对机器学习数据集与特征管道开展标签泄漏、时间穿越与实体重叠红队排查（参见 `references/multilingual-guide.md`）。
- **日本語**: リーケージ・アドバーサリ（データ漏洩レッドチーム） — 目的変数・時系列・グループ・前処理のデータリーケージを敵対的視点で徹底検証（`references/multilingual-guide.md` を参照）。
- **한국어**: 데이터 누수(Leakage) 레드팀 — 타깃·시계열·그룹·전처리 데이터 누수를 적대적(Red-team) 관점에서 탐지 및 차단 (`references/multilingual-guide.md` 참조).

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
