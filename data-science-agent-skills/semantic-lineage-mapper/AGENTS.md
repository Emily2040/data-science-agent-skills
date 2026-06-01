# AGENTS.md

When working inside this independent skill folder:

- Treat `SKILL.md` as the source of runtime behavior.
- Keep the skill provider-neutral: Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, and custom agents should be able to use it.
- Run `python scripts/quick_validate_skill.py . --strict` after edits.
- Run `python tests/test_skill_contract.py .` after edits.
- Preserve raw artifacts and do not add private data to examples.
- Keep visual assets present and correctly sized.
