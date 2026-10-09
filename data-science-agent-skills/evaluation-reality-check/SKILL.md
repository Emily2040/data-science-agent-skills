---
name: evaluation-reality-check
description: Audit offline model evaluations for temporal split fidelity, subgroup slice disparity, calibration error, and metric-to-business alignment. Use when stress-testing benchmark numbers before approving deployment or executive reporting.
---

# Evaluation Reality Check

## Mission

Design evaluation strategies that match task type, deployment setting, time, groups, and decision risk.

Primary failure mode prevented: offline evaluation often overstates real-world performance because splits, metrics, and benchmarks do not match deployment.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`task type, data generation process, deployment use, target and features`) must be audited for red flags such as `random split for temporal deployment`, `test set reused for tuning`, `no external validation for domain shift`, `single aggregate metric`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/slice_error_auditor.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`random split for temporal deployment`, `test set reused for tuning`, `no external validation for domain shift`, `single aggregate metric`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Evaluation Reality Check decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `evaluation protocol`, `split recommendation`, `failure-slice plan`, `uncertainty report`, `launch evidence checklist`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/slice_error_auditor.py path/to/predictions.csv --max-slice-gap 0.10
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Identify whether the problem is tabular, time series, NLP, CV, ranking, recommendation, or anomaly detection.
2. Choose split strategy: temporal, grouped, stratified, rolling, external validation, or benchmark holdout.
3. Check leakage, label delay, distribution shift, uncertainty, and subgroup coverage.
4. Define confidence intervals, calibration, threshold testing, and failure slices.
5. Return an evaluation protocol and minimum launch evidence.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Evaluation Reality Check — Audit subgroup slice errors, probability calibration, and offline-to-business translation.
- **简体中文**: 模型评估真实性核查 — 审计分群切片误差（Slice Error）、概率校准度（Brier）与离线指标到业务收益的映射（参见 `references/multilingual-guide.md`）。
- **日本語**: モデル評価リアリティチェック — サブグループ別のスライス誤差・確率キャリブレーション・ビジネス価値への換算を監査（`references/multilingual-guide.md` を参照）。
- **한국어**: 모델 평가 리얼리티 체크 — 세부 집단(Slice)별 오차 격차, 확률 보정(Calibration), 오프라인 지표의 비즈니스 전환 타당성 감사 (`references/multilingual-guide.md` 참조).

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
