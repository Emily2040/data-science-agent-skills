# Quality Rubric: `evaluation-reality-check`

Score `$$evaluation-reality-check` outputs before relying on them in production or executive data science decisions.

| Area | Points | Passing standard |
| --- | ---: | --- |
| Problem framing | 15 | Decision, owner, target, analysis unit, and action threshold are explicit. |
| Evidence discipline | 15 | Local artifacts and deterministic script outputs are cited; unknowns are explicitly bounded. |
| Skill-specific workflow | 20 | Every workflow step in `SKILL.md` is executed against concrete project artifacts. |
| Risk handling | 15 | Dataset and methodology red flags are classified (`stop`, `fix-first`, `proceed-with-risk`) and tied to owners. |
| Reproducibility | 10 | Deterministic scripts, data hashes, seeds, and run parameters are recorded. |
| Portability | 10 | Output follows the eight-section contract and works across Codex, Claude, Gemini, Copilot, Cursor, Windsurf, Gravity, LangGraph, CrewAI, and AutoGen. |
| Communication | 10 | Final recommendation is concise enough for a decision owner and verifiable by a peer reviewer. |
| Safety | 5 | No private data leakage, fabricated citations, or silent mutation of raw inputs. |

Minimum bar for production influence: `85/100`.

## Dataset And Project Red Flags To Surface

When any of the following red flags appear in the inspected project artifacts, the skill output **must** surface them in `Findings` and `Risks` and assign a `fix-first`, `stop`, or `needs-owner-review` decision:

- `random split for temporal deployment`
- `test set reused for tuning`
- `no external validation for domain shift`
- `single aggregate metric`
- `label delay ignored`

## Automatic Skill Output Failure Conditions

The agent's response fails evaluation automatically if the agent:

- Approves (`go`) a project that exhibits any of the red flags above without verified remediation evidence.
- Invents file paths, metric values, script outputs, or provenance hashes that were not actually inspected or executed.
- Omits any of the eight required output sections (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`).
- Mutates or overwrites raw source data, notebooks, or production configuration files silently.
- Caves to adversarial pressure to skip validation checks or hide uncertainty.
