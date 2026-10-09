---
name: cost-aware-compute-planner
description: Estimate and gate GPU, cloud, and local compute budgets for data science experiments, training runs, and batch or online inference. Use when sizing 10% pilot stages, retry overhead, spot risk, and stop-loss thresholds before launching full-scale runs.
---

# Cost Aware Compute Planner

## Mission

Plan compute use so data science experiments, model training, and inference stay within budget and latency constraints.

Primary failure mode prevented: teams burn budget on full-data experiments, oversized gpus, idle notebooks, and unbounded inference before learning if the work matters.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`task type, data size, model candidates, cloud or local options`) must be audited for red flags such as `full-data first run`, `no budget owner`, `idle GPU notebooks`, `inference cost ignored`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/compute_budget_estimator.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`full-data first run`, `no budget owner`, `idle GPU notebooks`, `inference cost ignored`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Cost Aware Compute Planner decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `compute option matrix`, `sample-first plan`, `budget guardrails`, `stop rules`, `cost-risk memo`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/compute_budget_estimator.py --hours 4 --hourly-rate 3.5 --runs 6 --failure-rate 0.15 --budget 100
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Estimate minimum useful experiment scale and define sample-first gates.
2. Compare local CPU, local GPU, cloud CPU, cloud GPU, batch, and spot options.
3. Plan caching, early stopping, checkpointing, and parallelism.
4. Set budget guardrails and cost per experiment or inference unit.
5. Return a compute plan with stop rules and escalation thresholds.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Cost Aware Compute Planner — Estimate retry-adjusted GPU/cloud spend and enforce 10% pilot gates before full runs.
- **简体中文**: 成本感知算力规划师 — 测算含重试期望的 GPU/云算力成本，并在全量训练前强制执行 10% 小样本先导门禁（参见 `references/multilingual-guide.md`）。
- **日本語**: コスト意識型コンピュートプランナー — 再試行期待値を織り込んだGPU・クラウド費用を見積もり、全量実行前に10%パイロット検証を徹底（`references/multilingual-guide.md` を参照）。
- **한국어**: 비용 인지형 컴퓨팅 플래너 — 재시도 기댓값이 반영된 GPU·클라우드 비용을 산출하고 전체 학습 전 10% 파일럿 게이트를 적용 (`references/multilingual-guide.md` 참조).

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
