# Evidence Map For Dataset Contract Forensics

Skill-specific pain point: Data breaks downstream because implicit assumptions about schema, meaning, ranges, uniqueness, and freshness are never written down.

Skill-specific hypothesis: Forensic contract inference converts observed data behavior into explicit tests that can be reviewed and automated.

## Public Evidence Base

- Anaconda 8th Annual State of Data Science and AI: https://www.anaconda.com/lp/8th-annual-state-of-data-science-ai-report
- Drexel and Precisely 2026 Data Integrity and AI Readiness: https://www.lebow.drexel.edu/sites/default/files/2026-01/lebow-precisely-state-data-integrity-ai-readiness-2026.pdf
- SYNQ 2025 Data Quality Benchmark Survey: https://www.synq.io/blog/2025-data-quality-benchmark-survey
- AgentDS 2026: https://arxiv.org/abs/2603.19005
- Microsoft notebook pain-point study: https://www.microsoft.com/en-us/research/publication/whats-wrong-with-computational-notebooks/
- ML leakage survey: https://link.springer.com/article/10.1186/s40537-025-01193-8
- MLOps systematic literature review: https://www.sciencedirect.com/science/article/pii/S0950584925000722

## Skill-Specific Evidence Themes

- Data contract practice from Great Expectations, Pandera, dbt tests, and SQL constraints.
- Schema drift, freshness, nullability, uniqueness, accepted values, and semantic-owner review.

## Non-Duplication Position

Existing public tools often cover individual operations such as profiling, validation, tracking, orchestration, visualization, or monitoring. This skill is not a wrapper for one tool. It packages the judgment workflow around tool selection, evidence review, risk classification, and audit-ready reporting.
