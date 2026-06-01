# Provider Interop

Use providers as evidence sources for `$model-risk-compliance-memo`. Do not let a provider decide the answer.

## Evidence Sources

- Snowflake
- BigQuery
- Databricks
- Postgres
- dbt
- Dagster
- Airflow
- Prefect
- MLflow
- DVC
- Weights and Biases
- SageMaker
- Vertex AI
- Azure ML
- Great Expectations
- Pandera
- Evidently
- Kedro
- local files

## Rules

- Prefer exports, metadata, schemas, samples, logs, model cards, experiment records, lineage, and validation reports over screenshots.
- Record provider name, artifact path, timestamp, owner, and freshness.
- Mark provider-specific features as optional; the skill must still work with local files.
- Do not upload private data to a new provider without explicit approval.
- When provider evidence conflicts with local evidence, surface the conflict in `Risks`.
