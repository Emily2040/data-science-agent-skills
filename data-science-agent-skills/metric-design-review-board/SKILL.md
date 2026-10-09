---
name: metric-design-review-board
description: Stress-test primary, guardrail, and diagnostic metrics for denominator shifts, Goodhart gaming vectors, and decision alignment. Use when defining experiment or product KPIs so optimization cannot silently degrade user experience or unit economics.
---

# Metric Design Review Board

## Mission

Review whether a chosen data science metric actually supports the decision, user outcome, risk, and cost tradeoff.

Primary failure mode prevented: projects optimize metrics that look scientific but misalign with business impact or safety.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`decision context, candidate metrics, stakeholders, false positive and false negative costs`) must be audited for red flags such as `metric not tied to action`, `proxy metric can be gamed`, `threshold chosen after results`, `guardrails missing`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/metric_guardrail_check.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`metric not tied to action`, `proxy metric can be gamed`, `threshold chosen after results`, `guardrails missing`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Metric Design Review Board decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `metric tree`, `cost curve notes`, `guardrail list`, `threshold recommendation`, `metric risk memo`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/metric_guardrail_check.py path/to/metric_spec.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Map metrics to the real decision and affected user or entity.
2. Separate primary, diagnostic, fairness, reliability, and guardrail metrics.
3. Review threshold effects, class imbalance, cost asymmetry, and gaming risk.
4. Check offline-online and proxy-outcome mismatch.
5. Return a metric board decision with acceptance and monitoring criteria.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Metric Design Review Board — Stress-test primary metrics, denominators, time windows, and anti-gaming guardrails.
- **简体中文**: 指标设计评审委员会 — 对核心北极星指标的分母口径、时间窗口、护栏指标与古德哈特（Goodhart）作弊路径开展压力测试（参见 `references/multilingual-guide.md`）。
- **日本語**: 指標設計レビューボード — 主要KPIの分母定義・集計期間・ガードレール指標・Goodhartの法則によるハック耐性を審査（`references/multilingual-guide.md` を参照）。
- **한국어**: 지표 설계 리뷰 보드 — 핵심 KPI의 분모 정의, 집계 윈도우, 가드레일 지표, 굿하트 법칙(게이밍) 취약점을 심사 (`references/multilingual-guide.md` 참조).

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
