# Quality Rubric

Score `$ai-data-readiness-triage` outputs before trusting them in high-stakes data science work.

| Area | Points | Passing standard |
| --- | ---: | --- |
| Problem framing | 15 | Decision, owner, target, unit, and action threshold are explicit. |
| Evidence discipline | 15 | Artifacts and checks are listed; unknowns are marked. |
| Skill-specific workflow | 20 | All workflow steps are addressed, not merely mentioned. |
| Risk handling | 15 | Red flags are classified and tied to actions. |
| Reproducibility | 10 | Scripts, data versions, assumptions, and run context are preserved. |
| Portability | 10 | Output can be understood by Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, or a custom runtime. |
| Communication | 10 | Final answer is concise enough for a decision owner and precise enough for a reviewer. |
| Safety | 5 | No private data leakage, unsupported claims, or silent mutation. |

Minimum bar for production influence: 85/100.

Automatic failure if any of these occur:

- unknown owner
- no label source
- PII without approved use
- high missingness in core fields
- freshness mismatched to decision cycle

Automatic failure also applies if the answer invents missing evidence, hides uncertainty, mutates raw data silently, or claims compliance/causality/production readiness without enough evidence.
