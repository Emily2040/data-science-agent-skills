# Data Science Agent Skills

Twenty-five independent, production-grade Agent/Codex skills for data science work where judgment matters: framing, readiness, data quality, leakage, reproducibility, evaluation, governance, privacy, MLOps, incident response, and stakeholder communication.

Each skill is a standalone package with its own `SKILL.md`, `README.md`, tests, references, provider guidance, helper scripts, hero shot, and detailed Reddit-ready infographic. Public users can open any skill folder below and use it independently.

## How To Use

1. Choose the skill that matches the data-science problem.
2. Open that skill's folder and read its independent `README.md`.
3. Copy or install the whole folder into an agent skill directory.
4. Give the agent the relevant data, notebooks, SQL, model artifacts, or stakeholder context.
5. Run the skill workflow and keep the returned evidence artifact with the project.

The standard output contract across skills is:

`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, and `Artifacts`.

## Skill Catalog

| Skill | What it solves | Main artifact |
|---|---|---|
| [AI Data Readiness Triage](data-science-agent-skills/ai-data-readiness-triage/) | Scores whether data is ready for AI or analytics before modeling starts. | Readiness scorecard and blocker plan |
| [Baseline Ablation Lab](data-science-agent-skills/baseline-ablation-lab/) | Forces honest baselines and ablations before trusting complex models. | Baseline table and ablation matrix |
| [Causal Assumption Scout](data-science-agent-skills/causal-assumption-scout/) | Stops prediction work from being oversold as causal evidence. | DAG, assumption map, sensitivity notes |
| [Cost Aware Compute Planner](data-science-agent-skills/cost-aware-compute-planner/) | Prevents runaway cloud and GPU spend before experiments launch. | Compute budget plan and stop rules |
| [Data Question Framing](data-science-agent-skills/data-question-framing/) | Turns vague stakeholder asks into measurable data-science problems. | Decision canvas and metric tree |
| [Data Science Incident RCA](data-science-agent-skills/data-science-incident-rca/) | Diagnoses broken models, dashboards, data products, and pipeline incidents. | RCA memo, timeline, countermeasures |
| [Dataset Contract Forensics](data-science-agent-skills/dataset-contract-forensics/) | Infers practical data contracts and tests from messy schemas and samples. | Contract draft and test suggestions |
| [Domain Expert Collaboration Loop](data-science-agent-skills/domain-expert-collaboration-loop/) | Structures SME review so agents do not miss domain assumptions. | Assumption log and signoff trail |
| [Drift Monitor Designer](data-science-agent-skills/drift-monitor-designer/) | Designs data, concept, and performance drift monitoring with actions. | Monitoring design and alert playbook |
| [Evaluation Reality Check](data-science-agent-skills/evaluation-reality-check/) | Builds trustworthy evaluation for tabular, time-series, NLP, CV, and ranking. | Evaluation plan and stress-test report |
| [Experiment Provenance Ledger](data-science-agent-skills/experiment-provenance-ledger/) | Preserves code, data, environment, model, metrics, and decisions. | Experiment ledger and audit trail |
| [Feature Store Readiness](data-science-agent-skills/feature-store-readiness/) | Decides whether a feature store is warranted and how to design features safely. | Store-or-skip decision and feature contract |
| [Leakage Adversary](data-science-agent-skills/leakage-adversary/) | Attacks ML pipelines for target, temporal, group, split, and join leakage. | Leakage report and split validation notes |
| [Messy Data Cleanroom](data-science-agent-skills/messy-data-cleanroom/) | Produces reversible cleaning plans instead of silent data edits. | Cleaning plan and audit log |
| [Metric Design Review Board](data-science-agent-skills/metric-design-review-board/) | Aligns metrics with real decisions, costs, thresholds, and guardrails. | Metric tree and review verdict |
| [Missingness Mechanism Investigator](data-science-agent-skills/missingness-mechanism-investigator/) | Diagnoses MCAR, MAR, MNAR, or unknown missingness before imputation. | Missingness report and sensitivity plan |
| [Model Risk Compliance Memo](data-science-agent-skills/model-risk-compliance-memo/) | Creates governance-ready artifacts for privacy, fairness, safety, auditability, and monitoring. | Model risk memo and conditions |
| [Notebook Repro Packager](data-science-agent-skills/notebook-repro-packager/) | Makes notebooks runnable elsewhere with environment, seeds, data manifest, and smoke tests. | Repro package and smoke test |
| [Notebook To Pipeline Surgeon](data-science-agent-skills/notebook-to-pipeline-surgeon/) | Refactors exploratory notebooks into modular scripts or DAG tasks. | Pipeline extraction plan and CLI contract |
| [OSS Data Science Supply Chain Auditor](data-science-agent-skills/oss-ds-supply-chain-auditor/) | Audits deps, notebooks, model weights, datasets, licenses, and provenance. | SBOM-style risk report |
| [Privacy Preserving Data Science](data-science-agent-skills/privacy-preserving-ds/) | Guides minimized, local-first, aggregated, synthetic, federated, or enclave analysis. | Privacy decision tree and safe-analysis plan |
| [Production ML Handoff](data-science-agent-skills/production-ml-handoff/) | Turns data-science prototypes into engineering-ready production handoffs. | Handoff packet, API contract, monitoring plan |
| [Semantic Lineage Mapper](data-science-agent-skills/semantic-lineage-mapper/) | Reconstructs lineage from SQL, notebooks, pipelines, configs, and dashboards. | Lineage map and owner prompts |
| [Small Data Power Planner](data-science-agent-skills/small-data-power-planner/) | Helps teams avoid overfitting, false certainty, and premature modeling with scarce data. | Power plan, uncertainty summary, stop rule |
| [Stakeholder Insight Storyteller](data-science-agent-skills/stakeholder-insight-storyteller/) | Converts analysis into decision-grade narrative without overclaiming. | Executive memo and recommendation narrative |

## Package Standard

Every skill folder includes:

- `SKILL.md`: portable agent instructions and trigger guidance
- `README.md`: public skill page with usage, problem, workflow, and validation
- `MANIFEST.json`: machine-readable package contract
- `references/`: playbook, provider interoperability, portability, research grounding, tests, and rubric
- `scripts/`: deterministic helpers where useful
- `tests/`: portable contract tests and clean, messy, adversarial fixtures
- `assets/hero-shot.png`: `1600x900` hero visual
- `assets/reddit-infographic.png`: `1080x1350` detailed public infographic

## Agent And Provider Compatibility

The skills are written for OpenAI Codex, ChatGPT Agents, Anthropic Claude and Claude Code, Google Gemini, GitHub Copilot, Cursor, Windsurf, Goose, OpenCode, OpenHands, Gravity, LangGraph, CrewAI, AutoGen, LlamaIndex, Semantic Kernel, and local LLM agents.

Provider output is evidence, not authority. The agent should inspect local artifacts first, preserve raw evidence, avoid silent mutation, and ask for user or owner confirmation when missing context would change the decision.

## Validation

Run the contract checks inside any skill folder:

```bash
python scripts/quick_validate_skill.py . --strict
python tests/test_skill_contract.py .
```

For the full repository, repeat those checks across all folders in `data-science-agent-skills/`.
