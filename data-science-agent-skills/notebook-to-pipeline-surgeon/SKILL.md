---
name: notebook-to-pipeline-surgeon
description: Refactor exploratory Jupyter notebooks into modular, testable Python pipeline stages with explicit input/output contracts. Use when extracting data loading, feature engineering, training, and evaluation out of stateful notebook cells.
---

# Notebook To Pipeline Surgeon

## Mission

Convert exploratory notebooks into modular, parameterized scripts or orchestrated pipeline tasks.

Primary failure mode prevented: production workflows inherit notebook state, copy-pasted cells, and manual execution steps.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`notebook, target runtime, data locations, expected outputs`) must be audited for red flags such as `global mutable state`, `manual cell ordering`, `plot-only outputs used downstream`, `external calls in transform functions`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/notebook_repro_audit.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`global mutable state`, `manual cell ordering`, `plot-only outputs used downstream`, `external calls in transform functions`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Notebook To Pipeline Surgeon decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `pipeline extraction map`, `module boundaries`, `parameter contract`, `test plan`, `orchestrator recommendation`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/notebook_repro_audit.py path/to/notebook.ipynb
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Identify notebook sections: config, IO, transforms, modeling, evaluation, visualization, and side effects.
2. Extract reusable functions and isolate parameters.
3. Define CLI or config file and deterministic outputs.
4. Choose simple scripts first; use Dagster, Kedro, Prefect, or Airflow only when orchestration value is clear.
5. Return a refactor plan with tests and migration steps.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Notebook To Pipeline Surgeon — Refactor exploratory notebooks into modular, testable, idempotent pipeline stages.
- **简体中文**: Notebook 转生产管道重构师 — 将探索性 Notebook 拆解重构为模块化、幂等、可单测的生产数据与训练管道（参见 `references/multilingual-guide.md`）。
- **日本語**: Notebook・トゥ・パイプライン・サージョン — 探索的Notebookをモジュール化・べき等・テスト可能な本番パイプラインへ外科的に再構築（`references/multilingual-guide.md` を参照）。
- **한국어**: 노트북-파이프라인 리팩터링 서전 — 탐색적 노트북을 모듈화·멱등성·단위 테스트를 갖춘 프로덕션 파이프라인으로 전환 (`references/multilingual-guide.md` 참조).

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
