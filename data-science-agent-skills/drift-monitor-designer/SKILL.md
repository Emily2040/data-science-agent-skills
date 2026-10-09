---
name: drift-monitor-designer
description: Design production feature, prediction, and label drift monitors with calibrated alert thresholds and named on-call owners. Use when comparing baseline vs current distributions for mean shift, variance explosion, missingness spikes, and delayed ground truth.
---

# Drift Monitor Designer

## Mission

Design drift monitoring for production models and data products across data, concept, performance, and operational signals.

Primary failure mode prevented: models degrade silently because teams monitor uptime but not input, label, behavior, or outcome change.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`model purpose, features, prediction logs, label availability`) must be audited for red flags such as `alerts with no owner`, `thresholds copied from defaults`, `label delay ignored`, `no baseline window`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/drift_probe.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`alerts with no owner`, `thresholds copied from defaults`, `label delay ignored`, `no baseline window`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Drift Monitor Designer decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `monitor catalog`, `baseline definitions`, `threshold plan`, `alert ownership`, `drift response playbook`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/drift_probe.py path/to/baseline.csv path/to/current.csv
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Classify drift risks: schema, distribution, relationship, concept, performance, and operational drift.
2. Choose monitors based on data type, label delay, and actionability.
3. Set thresholds, baselines, alert routing, and suppression rules.
4. Define retrain, rollback, investigation, or no-action playbooks.
5. Return a monitor design and incident response path.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Drift Monitor Designer — Detect mean shifts, variance explosions, constant-column breaks, NaNs, and missing-rate spikes.
- **简体中文**: 数据与概念漂移监控设计 — 检测均值偏移、方差暴增、常量列突变、NaN 污染与缺失率飙升，设计分级告警动作（参见 `references/multilingual-guide.md`）。
- **日本語**: ドリフトモニター設計 — 平均シフト・分散爆発・定数列の崩壊・NaN混入・欠損率急増を検知し実践的なアラートを設計（`references/multilingual-guide.md` を参照）。
- **한국어**: 드리프트 모니터 디자이너 — 평균 이동, 분산 폭증, 상수 컬럼 깨짐, NaN 오염, 결측률 급증을 탐지하고 실행 가능한 알림 설계 (`references/multilingual-guide.md` 참조).

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
