# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `cost-aware-compute-planner`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$cost-aware-compute-planner` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 3: Repro & Pipelines | **Cost Aware Compute Planner** | Estimate retry-adjusted GPU/cloud spend and enforce 10% pilot gates before full runs | `"Estimate retry-adjusted compute cost for this training sweep and set staged budget guardrails."` |
| **简体中文** | 阶段 3：可复现性与工程管道 | **成本感知算力规划师** | 测算含重试期望的 GPU/云算力成本，并在全量训练前强制执行 10% 小样本先导门禁 | `"测算这批训练任务的期望算力成本（含失败重试），并制定 10% 先导验证与预算熔断规则。"` |
| **日本語** | ステージ 3：再現性・パイプライン化 | **コスト意識型コンピュートプランナー** | 再試行期待値を織り込んだGPU・クラウド費用を見積もり、全量実行前に10%パイロット検証を徹底 | `"失敗再試行を考慮した学習コストを見積もり、10%パイロット検証ゲートと予算上限ルールを設計してください。"` |
| **한국어** | 3단계: 재현성 및 파이프라인 엔지니어링 | **비용 인지형 컴퓨팅 플래너** | 재시도 기댓값이 반영된 GPU·클라우드 비용을 산출하고 전체 학습 전 10% 파일럿 게이트를 적용 | `"실패 재시도율을 반영한 총 컴퓨팅 비용을 추정하고 10% 파일럿 게이트와 예산 가드레일을 설정해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Teams burn cloud GPU budgets on full-dataset sweeps before verifying pipeline stability on a 10% pilot sample.
- **简体中文**: 在尚未通过小样本验证代码稳定性与收益前，直接启动全量数据与大规模 GPU 超参搜索，导致算力预算迅速烧穿。
- **日本語**: パイプラインの安定性を小規模サンプルで確認する前にフルデータでGPUクラスタを回し、予算を浪費する。
- **한국어**: 10% 소규모 샘플로 파이프라인 안정성을 검증하기도 전에 전체 데이터셋과 대형 GPU 클러스터를 돌려 예산을 소진함.

Inspected red flags across all locales: `full-data first run`, `no budget owner`, `idle GPU notebooks`, `inference cost ignored`, `training cheaper than monitoring is assumed`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/compute_budget_estimator.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/compute_budget_estimator.py`.
