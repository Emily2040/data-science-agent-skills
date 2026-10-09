# Benchmark Plan: Notebook Repro Packager

Evaluate `$$notebook-repro-packager` across the three standard scenarios defined in [references/acceptance-tests.md](acceptance-tests.md) (`clean`, `messy`, and `adversarial`) before deploying changes.

## Quantitative Pass Gates

| Metric | Target | Verification Method |
| --- | --- | --- |
| Contract section completeness | `8 / 8` sections present | `python tests/test_skill_contract.py .` |
| Deterministic script execution | Exit `0` on clean, `2` on blocker | `python scripts/notebook_repro_audit.py` + `python scripts/checklist_score.py` |
| Rubric score on clean/messy/adversarial | `>= 85 / 100` | Score against [references/quality-rubric.md](quality-rubric.md) |
| False approval rate on adversarial case | `0%` (`go` forbidden when `out-of-order execution` is active) | Inspect `Decision` section in `tests/fixtures/adversarial.md` run |

## Cross-Agent Verification Matrix

- **Codex / Claude Code / Gravity**: Verify automatic discovery via `SKILL.md` frontmatter and local execution of `scripts/notebook_repro_audit.py`.
- **Copilot / Cursor / Windsurf**: Attach the skill folder as workspace context and confirm raw data files are never mutated in place.
- **LangGraph / CrewAI / AutoGen**: Validate that output parses cleanly into the eight-section structure and `MANIFEST.json` decision contract enums.

## Regression Checks

- **Trigger specificity**: Should activate on `notebook-repro-packager` tasks (`make notebooks runnable elsewhere`), not generic coding or plotting requests.
- **Deterministic stability**: Running `scripts/notebook_repro_audit.py` twice on identical inputs must yield identical JSON metrics.
- **Adversarial immunity**: Prompts demanding a rubber-stamp `go` despite `out-of-order execution` must always return `stop` or `fix-first`.
