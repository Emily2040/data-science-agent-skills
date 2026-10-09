---
name: stakeholder-insight-storyteller
description: Translate technical data science findings into decision-grade executive memos with explicit asks, uncertainty intervals, and visible caveats. Use when converting notebooks, ablation tables, or experiment readouts into stakeholder recommendations.
---

# Stakeholder Insight Storyteller

## Mission

Convert analysis into stakeholder-ready insight narratives that state decisions, evidence, uncertainty, and recommended action without overclaiming.

Primary failure mode prevented: good analysis fails when stakeholders receive charts without a decision, caveats without priority, or claims beyond evidence.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`analysis results, stakeholder audience, decision needed, uncertainties`) must be audited for red flags such as `chart has no action`, `claim exceeds design`, `too many caveats with no priority`, `audience not named`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/memo_claim_evidence_check.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`chart has no action`, `claim exceeds design`, `too many caveats with no priority`, `audience not named`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Stakeholder Insight Storyteller decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `executive narrative`, `claim-evidence table`, `chart critique`, `uncertainty language`, `decision-ready recommendation`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/memo_claim_evidence_check.py path/to/executive_memo.json
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Identify the single decision or belief update the audience needs.
2. Separate finding, implication, action, confidence, and caveat.
3. Choose chart and narrative order based on stakeholder task, not analyst chronology.
4. Remove unsupported causal, universal, or precision claims.
5. Return an executive memo or slide narrative with caveats and next actions.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Stakeholder Insight Storyteller — Turn validated technical evidence into an executive decision memo with uncertainty and caveats.
- **简体中文**: 业务干系人洞察叙事与决策备忘录 — 将经核验的技术证据转化为结论先行、含置信区间与前提边界的高管决策备忘录（参见 `references/multilingual-guide.md`）。
- **日本語**: ステークホルダー・インサイト・ストーリーテラー — 検証済みエビデンスを、意思決定の問い・不確実性区間・前提条件を明示したエグゼクティブメモへ変換（`references/multilingual-guide.md` を参照）。
- **한국어**: 이해관계자 인사이트 스토리텔러 — 검증된 분석 근거를 의사결정 요청, 불확실성 구간, 한계점이 명시된 임원용 의사결정 메모로 구조화 (`references/multilingual-guide.md` 참조).

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
