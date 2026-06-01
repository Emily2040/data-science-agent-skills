# Agent Portability

This skill must remain useful across hosted chat agents, coding agents, CLI agents, and custom multi-agent runtimes.

| Agent or runtime | Adaptation rule |
| --- | --- |
| OpenAI Codex | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| ChatGPT Agents | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Anthropic Claude | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Claude Code | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Google Gemini | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| GitHub Copilot | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Cursor | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Windsurf | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Goose | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| OpenCode | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| OpenHands | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Gravity | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| LangGraph | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| CrewAI | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| AutoGen | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| LlamaIndex | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| Semantic Kernel | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |
| local LLM agents | Use `SKILL.md` as the role instruction; attach references only when needed; run local tests when filesystem access exists. |

## Minimum Portable Contract

- Load `SKILL.md` first.
- Preserve the eight-section output contract.
- Keep raw artifacts untouched.
- Use local scripts only when the runtime can execute files safely.
- Use `references/playbook.md` for deeper judgment rules.
- Use `references/acceptance-tests.md` for forward tests.
- Use `MANIFEST.json` to verify required files and image assets.

## Runtime Levels

1. Text-only agent: use `SKILL.md`, `README.md`, and references; skip scripts.
2. Filesystem agent: inspect local artifacts and run `scripts/quick_validate_skill.py`.
3. Coding agent: run helper scripts, patch generated artifacts, and add tests.
4. Multi-agent runtime: route collection, critique, and final decision to separate agents, but keep this skill responsible for the final decision artifact.
5. Enterprise runtime: enforce privacy, audit, logging, owner signoff, and retention rules before using external providers.
