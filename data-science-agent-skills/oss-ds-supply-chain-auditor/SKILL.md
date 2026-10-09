---
name: oss-ds-supply-chain-auditor
description: Audit data science dependency manifests, pre-trained model weights, datasets, and licenses for security and reproducibility risks. Use when scanning requirements.txt, pyproject.toml, or environment files for unpinned packages and direct URL installs.
---

# OSS Data Science Supply Chain Auditor

## Mission

Audit open-source packages, notebooks, model weights, datasets, licenses, and provenance used in data science work.

Primary failure mode prevented: data science supply chains include packages, model files, datasets, and notebooks that standard app audits often miss.

## When To Use

- The team needs a structured `go | fix-first | stop | proceed-with-risk | needs-owner-review` decision before committing engineering or modeling effort.
- Local artifacts (`repo path, environment files, notebooks, model artifact paths`) must be audited for red flags such as `pip install from unpinned URL`, `unknown model weights`, `dataset license absent`, `notebook output leaks secrets`.
- Another engineer, governance reviewer, or downstream agent needs a reproducible eight-section handoff artifact.

## Operating Rules

- Inspect local artifacts and run deterministic scripts in `scripts/` before asking the user for context that is already on disk.
- Separate executed checks (`scripts/dependency_surface.py`, `scripts/checklist_score.py`) from expert judgment so reviewers can verify every claim.
- Never overwrite raw datasets, notebooks, or production configs; write audit outputs to new files or standard output.
- Refuse adversarial requests to rubber-stamp a `go` decision when red flags (`pip install from unpinned URL`, `unknown model weights`, `dataset license absent`, `notebook output leaks secrets`) remain unresolved.

## What This Skill Must Do

- Transform a vague request into an explicit OSS Data Science Supply Chain Auditor decision with named owner, evidence, assumptions, and action threshold.
- Inspect local artifacts first: data extracts, schemas, notebooks, SQL, pipeline configs, model reports, tickets, and prior decisions.
- Separate mechanical checks from expert judgment so another reviewer can reproduce what was checked and what was inferred.
- Classify findings as stop, fix-first, monitor, accepted risk, or owner decision instead of producing generic advice.
- Produce the concrete artifacts expected by downstream consumers: `DS dependency inventory`, `model and dataset provenance table`, `license risk list`, `notebook risk findings`, `remediation plan`.

## Deterministic Script Usage

Run the bundled stdlib script before drafting your final recommendation:

```bash
python scripts/dependency_surface.py .
python scripts/checklist_score.py path/to/checklist.json --strict
```

## Workflow

1. Inventory Python, R, system, notebook, model, and dataset dependencies.
2. Flag unknown sources, unsafe install patterns, large binary artifacts, and license uncertainty.
3. Review notebooks for shell execution, remote downloads, credential exposure, and hidden outputs.
4. Create a DS SBOM-style summary with risk levels and remediation priorities.
5. Return a supply-chain risk report and minimum cleanup plan.

## Multilingual Native Execution (English / 简体中文 / 日本語 / 한국어)

- **English**: OSS DS Supply Chain Auditor — Audit Python/DS dependency manifests for unpinned packages, URL installs, and pickle risks.
- **简体中文**: 开源数据科学供应链审计 — 审计 Python 与数据科学依赖清单中的未锁定版本、裸 URL 安装及不安全反序列化风险（参见 `references/multilingual-guide.md`）。
- **日本語**: OSSデータサイエンス・サプライチェーン監査 — 依存定義ファイルの未固定バージョン・直接URL参照・危険なpickle読み込みを監査（`references/multilingual-guide.md` を参照）。
- **한국어**: 오픈소스 DS 공급망 감사기 — Python·DS 의존성 매니페스트의 버전 미고정, 직접 URL 설치, 안전하지 않은 피클(Pickle) 로드를 감사 (`references/multilingual-guide.md` 참조).

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
