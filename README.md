# Data Science Agent Skills

**Language / 语言 / 言語 / 언어**: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

![Data Science Agent Skills Hero](assets/repo-hero.png)

![Data Science Agent Skills Workflow](assets/repo-workflow-hero.png)

A production-grade catalog of **25 judgment-heavy data science and ML engineering agent skills** with deterministic Python standard-library verification tools, strict eight-section decision contracts, and native **English, Simplified Chinese (简体中文), Japanese (日本語), and Korean (한국어)** execution support.

Every skill requires the same final decision structure (`Problem`, `Inputs`, `Checks performed`, `Findings`, `Decision`, `Risks`, `Next actions`, `Artifacts`) and emits an explicit five-state verdict (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`).

---

## Find The Right Skill By Project Stage

![25-Skill Catalog Map](assets/repo-skill-map-infographic.png)

| Lifecycle Stage | Skill Package | Core Judgment & Scope | Primary Deterministic Script |
| --- | --- | --- | --- |
| Stage 1: Framing & Triage | [Data Question Framing (`data-question-framing`)](data-science-agent-skills/data-question-framing/) | Turn vague business or research asks into measurable DS problem statements | `scripts/decision_canvas_validator.py` |
| Stage 1: Framing & Triage | [AI Data Readiness Triage (`ai-data-readiness-triage`)](data-science-agent-skills/ai-data-readiness-triage/) | Score whether datasets are ready for AI, analytics, or modeling | `scripts/profile_table.py` |
| Stage 1: Framing & Triage | [Dataset Contract Forensics (`dataset-contract-forensics`)](data-science-agent-skills/dataset-contract-forensics/) | Infer and verify schema, grain, uniqueness, freshness, and null contracts | `scripts/profile_table.py` |
| Stage 1: Framing & Triage | [Semantic Lineage Mapper (`semantic-lineage-mapper`)](data-science-agent-skills/semantic-lineage-mapper/) | Trace table, column, and metric definitions across SQL, notebooks, and pipelines | `scripts/extract_lineage_tokens.py` |
| Stage 1: Framing & Triage | [Messy Data Cleanroom (`messy-data-cleanroom`)](data-science-agent-skills/messy-data-cleanroom/) | Design reversible, auditable cleaning and quarantine rules without mutating raw data | `scripts/profile_table.py` |
| Stage 2: Validity & Leakage | [Leakage Adversary (`leakage-adversary`)](data-science-agent-skills/leakage-adversary/) | Red-team ML datasets and pipelines for target, temporal, group, and preprocessing leakage | `scripts/split_leakage_probe.py` |
| Stage 2: Validity & Leakage | [Causal Assumption Scout (`causal-assumption-scout`)](data-science-agent-skills/causal-assumption-scout/) | Audit causal claims for confounding, collider bias, post-treatment controls, and identification | `scripts/confounder_backdoor_check.py` |
| Stage 2: Validity & Leakage | [Small Data Power Planner (`small-data-power-planner`)](data-science-agent-skills/small-data-power-planner/) | Calculate minimum detectable effect (MDE), sample power, and low-N overfitting bounds | `scripts/power_sample_size.py` |
| Stage 2: Validity & Leakage | [Missingness Mechanism Investigator (`missingness-mechanism-investigator`)](data-science-agent-skills/missingness-mechanism-investigator/) | Diagnose MCAR, MAR, and MNAR missingness and block naive imputation traps | `scripts/profile_table.py` |
| Stage 2: Validity & Leakage | [Baseline Ablation Lab (`baseline-ablation-lab`)](data-science-agent-skills/baseline-ablation-lab/) | Require naive/simple baselines and controlled ablations before accepting complex models | `scripts/ablation_delta_audit.py` |
| Stage 3: Repro & Pipelines | [Notebook Repro Packager (`notebook-repro-packager`)](data-science-agent-skills/notebook-repro-packager/) | Audit Jupyter notebooks for out-of-order cells, unseeded RNG, hardcoded paths, and lockfiles | `scripts/notebook_repro_audit.py` |
| Stage 3: Repro & Pipelines | [Notebook To Pipeline Surgeon (`notebook-to-pipeline-surgeon`)](data-science-agent-skills/notebook-to-pipeline-surgeon/) | Refactor exploratory notebooks into modular, testable, idempotent pipeline stages | `scripts/notebook_repro_audit.py` |
| Stage 3: Repro & Pipelines | [Experiment Provenance Ledger (`experiment-provenance-ledger`)](data-science-agent-skills/experiment-provenance-ledger/) | Record SHA-256 dataset hashes, git commit state, seeds, and hyperparameters per run | `scripts/capture_provenance.py` |
| Stage 3: Repro & Pipelines | [OSS DS Supply Chain Auditor (`oss-ds-supply-chain-auditor`)](data-science-agent-skills/oss-ds-supply-chain-auditor/) | Audit Python/DS dependency manifests for unpinned packages, URL installs, and pickle risks | `scripts/dependency_surface.py` |
| Stage 3: Repro & Pipelines | [Cost Aware Compute Planner (`cost-aware-compute-planner`)](data-science-agent-skills/cost-aware-compute-planner/) | Estimate retry-adjusted GPU/cloud spend and enforce 10% pilot gates before full runs | `scripts/compute_budget_estimator.py` |
| Stage 4: Eval & Governance | [Metric Design Review Board (`metric-design-review-board`)](data-science-agent-skills/metric-design-review-board/) | Stress-test primary metrics, denominators, time windows, and anti-gaming guardrails | `scripts/metric_guardrail_check.py` |
| Stage 4: Eval & Governance | [Evaluation Reality Check (`evaluation-reality-check`)](data-science-agent-skills/evaluation-reality-check/) | Audit subgroup slice errors, probability calibration, and offline-to-business translation | `scripts/slice_error_auditor.py` |
| Stage 4: Eval & Governance | [Model Risk Compliance Memo (`model-risk-compliance-memo`)](data-science-agent-skills/model-risk-compliance-memo/) | Document blast radius, human-in-the-loop override, fallback policy, and governance gates | `scripts/risk_tier_gate.py` |
| Stage 4: Eval & Governance | [Privacy Preserving DS (`privacy-preserving-ds`)](data-science-agent-skills/privacy-preserving-ds/) | Audit direct PII, quasi-identifiers, k-anonymity risks, and retention boundaries | `scripts/profile_table.py` |
| Stage 4: Eval & Governance | [Domain Expert Collaboration Loop (`domain-expert-collaboration-loop`)](data-science-agent-skills/domain-expert-collaboration-loop/) | Measure inter-annotator agreement (Cohen's kappa) and resolve SME label taxonomy disputes | `scripts/sme_label_agreement.py` |
| Stage 5: Ops & Storytelling | [Production ML Handoff (`production-ml-handoff`)](data-science-agent-skills/production-ml-handoff/) | Verify model SHA-256, input/output contracts, p99 latency SLA, fallback, and rollback readiness | `scripts/handoff_readiness_audit.py` |
| Stage 5: Ops & Storytelling | [Feature Store Readiness (`feature-store-readiness`)](data-science-agent-skills/feature-store-readiness/) | Audit online-offline feature parity, point-in-time joins, and serving TTL freshness | `scripts/online_offline_skew_check.py` |
| Stage 5: Ops & Storytelling | [Drift Monitor Designer (`drift-monitor-designer`)](data-science-agent-skills/drift-monitor-designer/) | Detect mean shifts, variance explosions, constant-column breaks, NaNs, and missing-rate spikes | `scripts/drift_probe.py` |
| Stage 5: Ops & Storytelling | [Data Science Incident RCA (`data-science-incident-rca`)](data-science-agent-skills/data-science-incident-rca/) | Correlate broken dashboards or model drops across ingestion, schema, feature, model, and metric layers | `scripts/incident_timeline_correlator.py` |
| Stage 5: Ops & Storytelling | [Stakeholder Insight Storyteller (`stakeholder-insight-storyteller`)](data-science-agent-skills/stakeholder-insight-storyteller/) | Turn validated technical evidence into an executive decision memo with uncertainty and caveats | `scripts/memo_claim_evidence_check.py` |

---

## Quickstart: Validate, List in 4 Languages, or Install Flat

All helper scripts and validators use only the Python 3 standard library—no `pip install` or virtual environment required.

```bash
# Validate all 25 skills (runs strict contract + behavioral script smoke tests)
python scripts/catalog_cli.py validate

# List the catalog in English, Simplified Chinese, Japanese, or Korean
python scripts/catalog_cli.py list --lang en
python scripts/catalog_cli.py list --lang zh-CN
python scripts/catalog_cli.py list --lang ja
python scripts/catalog_cli.py list --lang ko

# Install flat <target>/<skill-slug>/SKILL.md bundles for single-level agent skill discovery
python scripts/catalog_cli.py install --target ~/.codex/skills
python scripts/catalog_cli.py install --target ~/.claude/skills
python scripts/catalog_cli.py install --target ~/.gemini/config/skills

# Run the end-to-end multi-skill lifecycle and regression test suite
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## Cross-Runtime & Cloud Provider Interoperability

![Provider Compatibility](assets/repo-provider-compatibility.png)

- **18 Supported Agent Runtimes**: OpenAI Codex, ChatGPT Agents, Anthropic Claude, Claude Code, Google Gemini, Gravity / Antigravity, GitHub Copilot, Cursor, Windsurf, Goose, OpenCode, OpenHands, LangGraph, CrewAI, AutoGen, LlamaIndex, Semantic Kernel, and Local LLM Agents.
- **Native Quadrilingual Execution**: Every skill includes [references/multilingual-guide.md](data-science-agent-skills/ai-data-readiness-triage/references/multilingual-guide.md) with localized section headers, decision verdicts, and domain terminology in **English**, **简体中文**, **日本語**, and **한국어**.
- **Executable Helper Scripts and Strict Contract Tests**: Each skill bundles a domain-specific stdlib CLI verifier in `scripts/`, `scripts/checklist_score.py`, `scripts/quick_validate_skill.py`, and `tests/test_skill_contract.py`.
