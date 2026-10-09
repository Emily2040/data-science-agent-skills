# Agent Portability Guide: Model Risk Compliance Memo

This skill package is provider-neutral and structured so any agent runtime can load progressive context without vendor lock-in.

| Runtime / Host | How to load and execute `model-risk-compliance-memo` |
| --- | --- |
| OpenAI Codex CLI | Place the skill folder in `~/.codex/skills/model-risk-compliance-memo/`; Codex reads `SKILL.md` frontmatter and `agents/openai.yaml` metadata, then runs `scripts/risk_tier_gate.py` and `scripts/checklist_score.py` locally. |
| ChatGPT Agents | Upload or attach `SKILL.md` and `references/playbook.md` in the session workspace; use Code Interpreter to run `scripts/risk_tier_gate.py` on attached CSV/JSON artifacts. |
| Anthropic Claude | Load `SKILL.md` as project knowledge or a skill prompt; attach `references/quality-rubric.md` when grading decision memos. |
| Claude Code | Install under `.claude/skills/model-risk-compliance-memo/`; Claude Code triggers on the `SKILL.md` frontmatter description and invokes `python scripts/risk_tier_gate.py` via bash tool calls. |
| Google Gemini | Provide `SKILL.md` in system instructions or `.gemini/skills/model-risk-compliance-memo/` and require the eight-section `Output Contract` in markdown output. |
| GitHub Copilot | Reference `SKILL.md` and `references/playbook.md` via `#file` workspace context in Copilot Chat before reviewing data or pipeline PRs. |
| Cursor | Add `model-risk-compliance-memo/SKILL.md` as a workspace rule or `@file` reference; run `python scripts/quick_validate_skill.py . --strict` in the integrated terminal. |
| Windsurf | Pin `SKILL.md` in Cascade workspace context and invoke `scripts/risk_tier_gate.py` before accepting generated modeling or ETL code. |
| Goose | Register the folder as a local Goose skill; Goose executes the stdlib Python scripts in `scripts/` to gather deterministic evidence first. |
| OpenCode | Mount the skill directory in the project workspace and bind `scripts/risk_tier_gate.py` as a verification command. |
| OpenHands | Run `scripts/risk_tier_gate.py` and `scripts/checklist_score.py` inside the sandboxed runtime before emitting the final eight-section decision memo. |
| Gravity / Antigravity | Install into `.gemini/config/skills/model-risk-compliance-memo/` or workspace `.agent/skills/model-risk-compliance-memo/`; use `view_file` on `SKILL.md` and `run_command` for `scripts/risk_tier_gate.py`. |
| LangGraph | Bind `MANIFEST.json` `required_sections` and `decision_contract` as a typed state schema; wrap `scripts/risk_tier_gate.py` as a deterministic tool node. |
| CrewAI | Assign `SKILL.md` as the agent backstory/goal and `references/quality-rubric.md` as the task expected-output verification rubric. |
| AutoGen | Configure a two-agent review loop where the executor runs `scripts/risk_tier_gate.py` and the critic scores the output against `references/quality-rubric.md`. |
| LlamaIndex | Index `references/playbook.md` and `references/evidence-map.md` as queryable workflow context and enforce `MANIFEST.json` decision enums on synthesis. |
| Semantic Kernel | Map `SKILL.md` into a semantic plugin prompt and expose `scripts/risk_tier_gate.py` plus `scripts/checklist_score.py` as native function tools. |
| Local LLM agents | Keep prompt context tight by loading only `SKILL.md` (`<100` lines) first and delegating arithmetic or file profiling to `scripts/risk_tier_gate.py`. |
