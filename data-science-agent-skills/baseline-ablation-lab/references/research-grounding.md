# Research Grounding

This skill is designed from patterns visible in high-quality data-science and agent-skill repositories.

- [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science): Readable structure, immutable raw data, reusable project layout, docs, tests, and dependency files make data science easier to share.
- [Kedro](https://github.com/kedro-org/kedro): Production data science benefits from modular, reproducible, maintainable pipelines and explicit data catalogs.
- [MLflow](https://github.com/mlflow/mlflow): World-class ML workflows preserve parameters, metrics, artifacts, evaluations, model registry state, deployment paths, and broad framework integrations.
- [Anthropic Skills](https://github.com/anthropics/skills): A portable skill starts with a folder, SKILL.md frontmatter, clear usage instructions, scripts, and resources that can be loaded on demand.
- [CfRR Data Science Best Practices](https://coding-for-reproducible-research.github.io/CfRR_Courses/short_courses/data_science_best_practices.html): Reproducibility, transparency, documentation, dependency management, version control, testing, and collaboration are baseline quality requirements.

## Design Translation For `baseline-ablation-lab`

- Predictable structure: every skill has the same file contract and validation path.
- Modular reasoning: workflow steps are explicit and independently reviewable.
- Reproducibility: local scripts, fixtures, references, and output contracts are included.
- Lifecycle awareness: decisions consider handoff, audit, monitoring, ownership, and governance.
- Portability: the skill avoids vendor-specific assumptions and provides adaptation notes.

## Known Likes From Strong Repos

- Clear folder conventions.
- Fast start for new users.
- Tests and CI-friendly commands.
- Modular pipeline or workflow boundaries.
- Good documentation and examples.
- Strong provenance and reproducibility story.

## Known Friction To Avoid

- Heavy frameworks before users understand the problem.
- Hidden state and configuration sprawl.
- Docs that explain concepts but not the next command.
- Validation that catches syntax but not decision quality.
- Tool-specific lock-in that prevents another agent or provider from reusing the package.
