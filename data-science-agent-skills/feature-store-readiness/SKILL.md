---
name: feature-store-readiness
description: Evaluate whether an ML workflow needs a feature store and audit online-versus-offline feature parity. Use when checking point-in-time join correctness, serving latency SLAs, backfill cost, and entity-level value skew across training and serving.
---

# Feature Store Readiness

## Mission

Decide whether a feature store is needed and design features to avoid training-serving skew, staleness, and reuse confusion.

Primary failure mode prevented: teams either overbuild feature stores too early or underbuild shared feature governance until skew breaks models.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`feature list, training data flow, serving flow, latency needs`) must be audited for red flags such as `same feature computed differently online`, `freshness unknown`, `no point-in-time join`, `feature owner unclear`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/online_offline_skew_check.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`same feature computed differently online`, `freshness unknown`, `no point-in-time join`, `feature owner unclear`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Feature Store Readiness decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `feature-store decision`, `skew risk table`, `feature contract outline`, `TTL and freshness plan`, `migration steps`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/online_offline_skew_check.py path/to/offline.csv path/to/online.csv --key entity_id
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Assess whether features need online serving, reuse, point-in-time correctness, or shared governance.
2. Check training-serving skew, freshness, TTL, backfill, and ownership risks.
3. Recommend no store, lightweight registry, batch feature table, or full feature store.
4. Define feature contracts and lineage requirements.
5. Return a readiness decision and migration plan.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Feature Store Readiness — Audit online-offline feature parity, point-in-time joins, and serving TTL freshness.
- **简体中文**: 特征平台就绪度与在线离线一致性 — 审计离线训练与在线服务特征的逐实体一致性（Train-Serve Skew）、时间点关联与 TTL 时效（参见 `references/multilingual-guide.md`）。
- **日本語**: 特徴量ストア準備度＆オンライン／オフライン整合性 — 学習用バッチ特徴量と推論用オンライン特徴量の一致性（Train-Serve Skew）・時点結合・TTLを監査（`references/multilingual-guide.md` を参照）。
- **한국어**: 피처 스토어 준비도 및 온라인·오프라인 정합성 — 오프라인 학습 피처와 온라인 서빙 피처 간 정합성(Train-Serve Skew), 시점 정합 조인, TTL을 감사 (`references/multilingual-guide.md` 참조).

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
