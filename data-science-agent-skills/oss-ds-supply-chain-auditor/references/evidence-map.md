# Evidence Map For OSS Data Science Supply Chain Auditor

Skill-specific pain point: Data science supply chains include packages, model files, datasets, and notebooks that standard app audits often miss.

Skill-specific hypothesis: A DS-specific audit catches model/data provenance and notebook execution risks alongside dependency risk.

## Public Evidence Base

- Anaconda 8th Annual State of Data Science and AI: https://www.anaconda.com/lp/8th-annual-state-of-data-science-ai-report
- Drexel and Precisely 2026 Data Integrity and AI Readiness: https://www.lebow.drexel.edu/sites/default/files/2026-01/lebow-precisely-state-data-integrity-ai-readiness-2026.pdf
- SYNQ 2025 Data Quality Benchmark Survey: https://www.synq.io/blog/2025-data-quality-benchmark-survey
- AgentDS 2026: https://arxiv.org/abs/2603.19005
- Microsoft notebook pain-point study: https://www.microsoft.com/en-us/research/publication/whats-wrong-with-computational-notebooks/
- ML leakage survey: https://link.springer.com/article/10.1186/s40537-025-01193-8
- MLOps systematic literature review: https://www.sciencedirect.com/science/article/pii/S0950584925000722

## Skill-Specific Evidence Themes

- DS supply-chain surfaces: packages, notebooks, model weights, datasets, licenses, remote installs, binary artifacts, and hidden notebook outputs.
- Traditional app dependency scans are extended to model and data provenance.

## Non-Duplication Position

Existing public tools often cover individual operations such as profiling, validation, tracking, orchestration, visualization, or monitoring. This skill is not a wrapper for one tool. It packages the judgment workflow around tool selection, evidence review, risk classification, and audit-ready reporting.
