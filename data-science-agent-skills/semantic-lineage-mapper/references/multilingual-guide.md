# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `semantic-lineage-mapper`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$semantic-lineage-mapper` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 1: Framing & Triage | **Semantic Lineage Mapper** | Trace table, column, and metric definitions across SQL, notebooks, and pipelines | `"Map the upstream SQL and Python lineage for these columns and flag semantic definition drift."` |
| **简体中文** | 阶段 1：问题界定与数据初筛 | **语义血缘与口径映射** | 跨 SQL、Notebook 与数据管道追踪表、字段与指标的真实语义口径 | `"追踪这些字段在 SQL 和 Python 脚本中的血缘链路，排查同名异义口径冲突。"` |
| **日本語** | ステージ 1：課題定義・データ診断 | **セマンティック系譜マッパー** | SQL・Notebook・パイプラインを横断してテーブル・列・指標の意味論的系譜を追跡 | `"SQLとPythonコードから対象カラムの系譜を抽出し、定義の食い違いを特定してください。"` |
| **한국어** | 1단계: 문제 정의 및 데이터 트리아지 | **시맨틱 리니지 매퍼** | SQL, 노트북, 파이프라인 전반에서 테이블·컬럼·지표의 의미론적 계보 추적 | `"SQL과 Python 스크립트에서 이 컬럼들의 데이터 리니지를 추적하고 정의 불일치를 찾아 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Identically named metrics and columns carry incompatible business logic across warehouse layers and dashboards.
- **简体中文**: 同名指标或字段在数仓不同分层、训练脚本与 BI 报表中采用了相互冲突的过滤或聚合逻辑。
- **日本語**: 同じ名前の指標やカラムが、DWH層・学習スクリプト・BIダッシュボード間で異なる集計ロジックを持っている。
- **한국어**: 동일한 이름의 지표나 컬럼이 데이터 웨어하우스 계층과 대시보드마다 서로 다른 비즈니스 로직으로 계산됨.

Inspected red flags across all locales: `dashboard-only metric logic`, `manual spreadsheet hop`, `feature generated outside pipeline`, `PII source unclear`, `ownerless table`.

---

## 3. Eight-Section Output Contract (Localized Section Headers)

Always emit all eight sections in order. When responding in Chinese, Japanese, or Korean, include the canonical English section key in parentheses so both human stakeholders and automated contract validators can parse the memo:

| # | Canonical Key | English Header | 简体中文标题 | 日本語見出し | 한국어 섹션 제목 |
| --- | --- | --- | --- | --- | --- |
| 1 | `Problem` | `1. Problem` | `1. 问题定义 (Problem)` | `1. 課題定義 (Problem)` | `1. 문제 정의 (Problem)` |
| 2 | `Inputs` | `2. Inputs` | `2. 输入与数据契约 (Inputs)` | `2. 入力データと前提 (Inputs)` | `2. 입력 및 전제 조건 (Inputs)` |
| 3 | `Checks performed` | `3. Checks performed` | `3. 已执行的确定性检查 (Checks performed)` | `3. 実行済み検証 (Checks performed)` | `3. 수행된 검증 (Checks performed)` |
| 4 | `Findings` | `4. Findings` | `4. 关键发现与证据 (Findings)` | `4. 検証結果と根拠 (Findings)` | `4. 주요 발견 및 근거 (Findings)` |
| 5 | `Decision` | `5. Decision` | `5. 决策结论 (Decision)` | `5. 意思決定 (Decision)` | `5. 의사결정 (Decision)` |
| 6 | `Risks` | `6. Risks` | `6. 风险与阻塞项 (Risks)` | `6. リスクとブロッカー (Risks)` | `6. 리스크 및 차단 요인 (Risks)` |
| 7 | `Next actions` | `7. Next actions` | `7. 下一步行动 (Next actions)` | `7. 次のアクション (Next actions)` | `7. 후속 조치 (Next actions)` |
| 8 | `Artifacts` | `8. Artifacts` | `8. 交付物与产物 (Artifacts)` | `8. 成果物 (Artifacts)` | `8. 산출물 및 아티팩트 (Artifacts)` |

---

## 4. Five-State Decision Enum (Canonical Token + Native Verdict)

Always include the exact canonical token (`go`, `fix-first`, `stop`, `proceed-with-risk`, or `needs-owner-review`) alongside the localized verdict:

| Canonical Token | English Verdict | 简体中文判定 | 日本語判定 | 한국어 판정 | Operational Meaning |
| --- | --- | --- | --- | --- | --- |
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/extract_lineage_tokens.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/extract_lineage_tokens.py`.
