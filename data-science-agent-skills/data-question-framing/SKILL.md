---
name: data-question-framing
description: Translate ambiguous business, product, policy, or research asks into measurable data science decision canvases. Use when locking down the decision owner, action threshold, analysis unit, target definition, time horizon, and guardrail metrics.
---

# Data Question Framing

## Mission

Turn ambiguous business, product, policy, or research asks into decision-ready data science problem statements.

Primary failure mode prevented: teams waste cycles modeling the wrong target, optimizing vanity metrics, or answering questions that no owner can act on.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`raw stakeholder request, available decision or business context, known data sources or constraints, deadline and decision owner`) must be audited for red flags such as `no decision owner`, `target unavailable at decision time`, `metric can improve while user outcome worsens`, `causal claim hidden inside prediction wording`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/decision_canvas_validator.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`no decision owner`, `target unavailable at decision time`, `metric can improve while user outcome worsens`, `causal claim hidden inside prediction wording`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Data Question Framing decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `decision canvas`, `metric tree`, `assumption log`, `scope boundaries`, `next evidence needed`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/decision_canvas_validator.py path/to/decision_canvas.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Extract the decision, action, and user or entity affected.
2. Define the analysis unit, target, time horizon, and comparison baseline.
3. Separate prediction, causal, descriptive, and operational questions.
4. Choose success, guardrail, and decision metrics before any modeling plan.
5. Return a decision canvas with assumptions and unresolved questions.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Data Question Framing — Turn vague business or research asks into measurable DS problem statements.
- **简体中文**: 数据问题界定与拆解 — 将模糊的业务或科研诉求转化为可量化的数据科学问题定义（参见 `references/multilingual-guide.md`）。
- **日本語**: データ課題フレーミング — 曖昧なビジネス・研究要望を測定可能なDS課題定義へ構造化（`references/multilingual-guide.md` を参照）。
- **한국어**: 데이터 문제 정의 및 프레이밍 — 모호한 비즈니스·연구 요청을 측정 가능한 데이터 사이언스 문제로 구조화 (`references/multilingual-guide.md` 참조).

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
