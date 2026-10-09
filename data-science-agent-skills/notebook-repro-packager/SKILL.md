---
name: notebook-repro-packager
description: Audit and package Jupyter notebooks for deterministic top-to-bottom execution across machines. Use when detecting out-of-order cell execution, hardcoded local paths, unseeded randomness, inline shell installs, or leaked secrets.
---

# Notebook Repro Packager

## Mission

Package notebooks so another machine or teammate can reproduce their results with known data, environment, seeds, and order.

Primary failure mode prevented: notebooks break because execution order, hidden state, local paths, package versions, and data provenance are not captured.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`notebook files, data dependencies, environment files, expected outputs`) must be audited for red flags such as `out-of-order execution`, `local absolute paths`, `unseeded randomness`, `implicit data downloads`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/notebook_repro_audit.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`out-of-order execution`, `local absolute paths`, `unseeded randomness`, `implicit data downloads`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit Notebook Repro Packager decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `notebook audit`, `environment manifest`, `data manifest`, `run instructions`, `smoke-test plan`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/notebook_repro_audit.py path/to/notebook.ipynb
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Audit execution order, hidden state, hard-coded paths, missing seeds, and external dependencies.
2. Capture environment, data manifest, run command, and expected output checks.
3. Separate exploratory cells from required run path.
4. Add smoke-test guidance and failure messages.
5. Return a reproducibility package checklist and patch plan.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: Notebook Repro Packager — Audit Jupyter notebooks for out-of-order cells, unseeded RNG, hardcoded paths, and lockfiles.
- **简体中文**: Notebook 可复现性打包器 — 审计 Jupyter Notebook 的乱序执行、未固定随机种子、硬编码绝对路径与依赖锁定（参见 `references/multilingual-guide.md`）。
- **日本語**: Notebook再現性パッケージャー — Jupyter Notebookのセル実行順序の乱れ・未固定シード・絶対パス・依存ロック漏れを監査（`references/multilingual-guide.md` を参照）。
- **한국어**: 노트북 재현성 패키저 — Jupyter 노트북의 셀 역순 실행, 미고정 난수 시드, 절대 경로, 의존성 잠금 누락을 감사 (`references/multilingual-guide.md` 참조).

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
