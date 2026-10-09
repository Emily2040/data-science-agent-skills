---
name: data-science-incident-rca
description: Run root-cause analysis for broken ML models, metric drops, pipeline failures, and corrupted dashboards. Use when correlating anomaly timestamps across upstream data, schema changes, code deploys, and serving layers to produce a countermeasure memo.
---

# Data Science Incident RCA

## Mission

Run root-cause analysis for broken models, metrics, dashboards, pipelines, and data science decisions.

Primary failure mode prevented: data incidents become blame hunts because evidence, timelines, blast radius, and controls are scattered.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`incident symptom, time first observed, affected outputs, recent changes`) must be audited for red flags such as `no timestamped evidence`, `only one layer investigated`, `impact not quantified`, `human process omitted`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/incident_timeline_correlator.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`no timestamped evidence`, `only one layer investigated`, `impact not quantified`, `human process omitted`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Data Science Incident RCA decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `incident timeline`, `blast radius`, `root cause memo`, `countermeasure plan`, `monitoring changes`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/incident_timeline_correlator.py path/to/incident_events.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Define symptom, detection path, start time, severity, and affected users or decisions.
2. Build timeline across data sources, pipelines, code, model, dashboard, and human changes.
3. Separate root cause, contributing factors, detection gaps, and impact.
4. Recommend immediate mitigation, durable prevention, monitoring, and ownership updates.
5. Return an RCA memo with evidence and countermeasures.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Data Science Incident RCA — Correlate broken dashboards or model drops across ingestion, schema, feature, model, and metric layers.
- **简体中文**: 数据科学事故根因分析（RCA） — 跨数据接入、表结构、特征计算、模型版本与指标口径五层关联时间线，定位线上异常根因（参见 `references/multilingual-guide.md`）。
- **日本語**: データサイエンス・インシデント根本原因分析（RCA） — データ取込・スキーマ・特徴量・モデル・指標定義の5層でイベント時系列を相関させ原因を特定（`references/multilingual-guide.md` を参照）。
- **한국어**: 데이터 사이언스 인시던트 근본원인분석(RCA) — 데이터 수집·스키마·피처·모델·지표 5개 계층의 이벤트 타임라인을 상관 분석해 장애 원인 규명 (`references/multilingual-guide.md` 참조).

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
