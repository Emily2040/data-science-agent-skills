# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `baseline-ablation-lab`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$baseline-ablation-lab` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 2: Validity & Leakage | **Baseline Ablation Lab** | Require naive/simple baselines and controlled ablations before accepting complex models | `"Audit whether the candidate model beats simple baselines after accounting for seed variance and latency."` |
| **简体中文** | 阶段 2：有效性验证与防泄漏 | **基线对标与消融实验室** | 在接纳复杂模型前强制开展简单基线对标、多随机种子复现与特征消融实验 | `"审计候选模型相对于简单基线的净增益、跨随机种子稳定性、延迟代价与特征消融结果。"` |
| **日本語** | ステージ 2：妥当性・リーク検証 | **ベースライン＆アブレーション実験室** | 複雑なモデルを採用する前に単純ベースラインとの比較・複数シード検証・アブレーションを徹底 | `"候補モデルが単純ベースラインを統計的かつレイテンシ制約内で上回っているかアブレーション監査してください。"` |
| **한국어** | 2단계: 타당성 및 누수 검증 | **베이스라인 및 어블레이션 랩** | 복잡한 모델 채택 전 단순 베이스라인 비교, 다중 시드 검증, 피처 어블레이션을 강제 | `"후보 모델이 다중 시드 분산과 추론 지연시간을 감안해도 단순 베이스라인을 유의미하게 앞서는지 감사해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Teams deploy heavyweight ensembles or deep models without proving lift over simple heuristics across multiple seeds.
- **简体中文**: 未与规则基线或简单线性模型对比、仅凭单一随机种子跑分，就上线高延迟且难以维护的复杂模型。
- **日本語**: 単純なヒューリスティックや軽量モデルとの比較やシード分散の確認なしに、高コストな複雑モデルを本番投入してしまう。
- **한국어**: 단순 규칙이나 경량 모델 대비 실질적 성능 향상과 추론 지연 비용을 검증하지 않고 무거운 모델부터 배포함.

Inspected red flags across all locales: `no naive baseline`, `single random seed`, `improvement below uncertainty`, `cost ignored`, `feature ablations missing`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/ablation_delta_audit.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/ablation_delta_audit.py`.
