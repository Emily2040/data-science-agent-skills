# Multilingual Execution Guide (English / 简体中文 / 日本語 / 한국어): `stakeholder-insight-storyteller`

This skill is authored for native execution across **English**, **Simplified Chinese (简体中文)**, **Japanese (日本語)**, and **Korean (한국어)**. When a user invokes `$stakeholder-insight-storyteller` or asks a matching question in any of these four languages, respond in the user's language using native data science and ML engineering terminology (never machine-translationese), while preserving the canonical five-state decision token (`go`, `fix-first`, `stop`, `proceed-with-risk`, `needs-owner-review`) in parentheses so automated downstream parsers remain 100% interoperable.

---

## 1. Native Skill Identity Across Four Languages

| Language | Lifecycle Stage | Native Skill Title | Native Core Mission | Example Native Trigger Prompt |
| --- | --- | --- | --- | --- |
| **English** | Stage 5: Ops & Storytelling | **Stakeholder Insight Storyteller** | Turn validated technical evidence into an executive decision memo with uncertainty and caveats | `"Audit and structure this executive memo so the decision ask, uncertainty bounds, and caveats are explicit."` |
| **简体中文** | 阶段 5：生产交付、监控与叙事 | **业务干系人洞察叙事与决策备忘录** | 将经核验的技术证据转化为结论先行、含置信区间与前提边界的高管决策备忘录 | `"审查并重构这份高管汇报备忘录，确保决策诉求、置信区间、局限性与证据链清晰对齐。"` |
| **日本語** | ステージ 5：本番運用・監視・意思決定伝達 | **ステークホルダー・インサイト・ストーリーテラー** | 検証済みエビデンスを、意思決定の問い・不確実性区間・前提条件を明示したエグゼクティブメモへ変換 | `"このエグゼクティブ向け提案メモを監査し、意思決定の選択肢・信頼区間・制約条件が明確になるよう構成してください。"` |
| **한국어** | 5단계: 프로덕션 운영 및 인사이트 전달 | **이해관계자 인사이트 스토리텔러** | 검증된 분석 근거를 의사결정 요청, 불확실성 구간, 한계점이 명시된 임원용 의사결정 메모로 구조화 | `"이 임원 보고용 메모에 의사결정 요청, 불확실성 범위, 전제 조건이 명확히 담기도록 감사하고 재구성해 줘."` |

---

## 2. Native Failure Mode & Red Flags

- **English**: Decision makers either receive a 40-chart dump with no clear ask or a slick narrative that hides uncertainty and observational limits.
- **简体中文**: 向业务决策层堆砌几十张技术图表却无明确决策诉求，或者为了故事流畅而隐瞒不确定性区间与非因果前提。
- **日本語**: グラフを大量に並べるだけで意思決定の選択肢がなかったり、逆に分かりやすさを優先して不確実性や前提条件を隠してしまう。
- **한국어**: 의사결정 요청 없이 차트만 나열하거나, 매끄러운 서사를 위해 신뢰구간과 관찰 데이터의 한계를 숨김.

Inspected red flags across all locales: `chart has no action`, `claim exceeds design`, `too many caveats with no priority`, `audience not named`, `uncertainty hidden`.

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
| `go` | **Go (Approved)** | **通过 (`go`)** | **承認・進行可 (`go`)** | **진행 승인 (`go`)** | All deterministic checks pass (`scripts/memo_claim_evidence_check.py`, `scripts/checklist_score.py --strict`); no unresolved blockers. |
| `fix-first` | **Fix-First (Conditional Hold)** | **先修复再推进 (`fix-first`)** | **要修正後に再審査 (`fix-first`)** | **선조치 후 진행 (`fix-first`)** | Concrete, remediable defects exist; block progression until the specified remediation passes verification. |
| `stop` | **Stop (Blocked)** | **终止或拦截 (`stop`)** | **中止・ブロック (`stop`)** | **중단 / 차단 (`stop`)** | Fundamental data, leakage, validity, or compliance blocker makes the current approach invalid. |
| `proceed-with-risk` | **Proceed with Documented Risk** | **带风险放行 (`proceed-with-risk`)** | **リスク受容の上で進行 (`proceed-with-risk`)** | **리스크 감수 진행 (`proceed-with-risk`)** | Non-fatal limitations are quantified, bounded by guardrails, and explicitly accepted by the owner. |
| `needs-owner-review` | **Needs Owner Review** | **需责任人裁决 (`needs-owner-review`)** | **オーナー判断待ち (`needs-owner-review`)** | **책임자 검토 필요 (`needs-owner-review`)** | Technical evidence is complete, but a policy, budget, or business trade-off requires human sign-off. |

---

## 5. Anti-Slop Localization Rules

1. **No literal calques**: Use native domain terms (`数据血缘 / データ系譜 / 데이터 리니지`, `最小可检测效应 MDE / 最小検出可能効果 / 최소감지효과`, `在线离线一致性 / オンライン・オフライン整合性 / 온라인·오프라인 정합성`).
2. **Preserve deterministic evidence**: Never translate file paths, CLI flags, SHA-256 hashes, column names, or JSON keys emitted by `scripts/memo_claim_evidence_check.py`.
