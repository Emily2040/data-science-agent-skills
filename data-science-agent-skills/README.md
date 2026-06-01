# Independent Data Science Skills

![Data Science Agent Skill Map](../assets/repo-skill-map-infographic.png)

This directory contains 25 standalone data-science agent skills. Each folder is independently usable: open the folder, read its `README.md`, and copy the whole folder into the target agent's skill directory.

Every skill folder includes `SKILL.md`, `README.md`, `MANIFEST.json`, `references/`, `scripts/`, `tests/`, `assets/hero-shot.png`, and `assets/reddit-infographic.png`.

## Skill Index

| Skill | Use it when you need to... |
|---|---|
| [ai-data-readiness-triage](ai-data-readiness-triage/) | Decide whether data is ready for AI or analytics. |
| [baseline-ablation-lab](baseline-ablation-lab/) | Prove model lift against honest baselines and ablations. |
| [causal-assumption-scout](causal-assumption-scout/) | Prevent causal overclaims and document assumptions. |
| [cost-aware-compute-planner](cost-aware-compute-planner/) | Plan cloud, GPU, sample, and stop-rule cost controls. |
| [data-question-framing](data-question-framing/) | Turn vague stakeholder asks into measurable DS problems. |
| [data-science-incident-rca](data-science-incident-rca/) | Diagnose broken data, model, dashboard, or pipeline incidents. |
| [dataset-contract-forensics](dataset-contract-forensics/) | Infer practical contracts and tests from messy datasets. |
| [domain-expert-collaboration-loop](domain-expert-collaboration-loop/) | Structure SME review, assumptions, and signoff. |
| [drift-monitor-designer](drift-monitor-designer/) | Design drift metrics, thresholds, and alert playbooks. |
| [evaluation-reality-check](evaluation-reality-check/) | Build trustworthy evaluation across DS task types. |
| [experiment-provenance-ledger](experiment-provenance-ledger/) | Preserve code, data, environment, metrics, and decisions. |
| [feature-store-readiness](feature-store-readiness/) | Decide whether a feature store is needed and safe. |
| [leakage-adversary](leakage-adversary/) | Attack ML pipelines for leakage and contaminated splits. |
| [messy-data-cleanroom](messy-data-cleanroom/) | Produce reversible, auditable cleaning plans. |
| [metric-design-review-board](metric-design-review-board/) | Align metrics with business decisions, costs, and guardrails. |
| [missingness-mechanism-investigator](missingness-mechanism-investigator/) | Diagnose missingness mechanisms before imputation. |
| [model-risk-compliance-memo](model-risk-compliance-memo/) | Create governance-ready model risk artifacts. |
| [notebook-repro-packager](notebook-repro-packager/) | Make notebooks runnable elsewhere. |
| [notebook-to-pipeline-surgeon](notebook-to-pipeline-surgeon/) | Refactor notebooks into scripts or pipeline tasks. |
| [oss-ds-supply-chain-auditor](oss-ds-supply-chain-auditor/) | Audit packages, notebooks, weights, datasets, and licenses. |
| [privacy-preserving-ds](privacy-preserving-ds/) | Minimize sensitive-data exposure during analysis. |
| [production-ml-handoff](production-ml-handoff/) | Hand prototypes to engineering with contracts and monitoring. |
| [semantic-lineage-mapper](semantic-lineage-mapper/) | Reconstruct meaning and dependencies across the data stack. |
| [small-data-power-planner](small-data-power-planner/) | Avoid overfitting and false certainty with scarce data. |
| [stakeholder-insight-storyteller](stakeholder-insight-storyteller/) | Turn analysis into decision-grade narrative. |

## Portable Contract

Each skill is written to work with Codex, ChatGPT Agents, Claude, Gemini, Copilot-style agents, Cursor, Windsurf, Gravity, LangGraph, CrewAI, AutoGen, OpenHands, Goose, OpenCode, and local LLM agents.

The shared output contract is: `Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, and `Artifacts`.
