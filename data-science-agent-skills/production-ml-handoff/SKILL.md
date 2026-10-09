---
name: production-ml-handoff
description: Package prototype ML models into production engineering handoff bundles with input/output schemas, latency budgets, fallback baselines, and rollback triggers. Use when transitioning a validated model from data science exploration to ML engineering ownership.
---

# Production ML Handoff

## Mission

Convert data science prototypes into engineering-ready ML handoffs with contracts, artifacts, SLOs, monitoring, and ownership.

Primary failure mode prevented: engineering teams receive notebooks and model files without enough interface, operational, or rollback detail.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`prototype repo or notebook, model artifact, feature inputs, serving pattern`) must be audited for red flags such as `notebook is only artifact`, `feature definitions ambiguous`, `no rollback plan`, `latency unknown`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/handoff_readiness_audit.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`notebook is only artifact`, `feature definitions ambiguous`, `no rollback plan`, `latency unknown`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Production ML Handoff decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `API or batch contract`, `artifact manifest`, `SLO and monitoring plan`, `rollback plan`, `handoff acceptance checklist`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/handoff_readiness_audit.py path/to/handoff_bundle.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Define inference contract: inputs, outputs, types, thresholds, errors, latency, and privacy constraints.
2. Package artifacts, versioning, environment, and reproducibility evidence.
3. Specify deployment path, rollback, monitoring, alerting, and ownership.
4. Identify engineering blockers and unresolved research assumptions.
5. Return a handoff brief and acceptance checklist.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Production ML Handoff — Verify model SHA-256, input/output contracts, p99 latency SLA, fallback, and rollback readiness.
- **简体中文**: 机器学习生产交付门禁 — 核验模型制品 SHA-256、输入输出契约、p99 延迟 SLA、降级基线与自动回滚触发器（参见 `references/multilingual-guide.md`）。
- **日本語**: 本番MLハンドオフ（運用引き継ぎ監査） — モデルSHA-256・入出力スキーマ・p99レイテンシSLA・フォールバック・ロールバック条件を検証（`references/multilingual-guide.md` を参照）。
- **한국어**: 프로덕션 ML 핸드오프 — 모델 SHA-256 해시, 입출력 스키마, p99 지연시간 SLA, 폴백 베이스라인, 롤백 트리거를 검증 (`references/multilingual-guide.md` 참조).

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
