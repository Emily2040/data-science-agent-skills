# データサイエンス・エージェントスキル集 (Data Science Agent Skills)

**Language / 语言 / 言語 / 언어**: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

![データサイエンス・エージェントスキル・ヒーロー画像](assets/repo-hero.png)

![データサイエンス・ライフサイクル・ワークフロー](assets/repo-workflow-hero.png)

データサイエンスおよび機械学習エンジニアリングにおける判断の難所を網羅した、**全25種類のプロフェッショナル・エージェントスキル（Skill Catalog）**です。すべてのスキルに**Python標準ライブラリのみで動作する決定論的検証スクリプト**と**8セクションの意思決定契約**が組み込まれており、**英語（English）・簡体字中国語（简体中文）・日本語・韓国語（한국어）**の4言語ネイティブ実行に対応しています。

すべてのスキルは統一された8つのセクション（`Problem / 課題定義`、`Inputs / 入力データと前提`、`Checks performed / 実行済み検証`、`Findings / 検証結果と根拠`、`Decision / 意思決定`、`Risks / リスクとブロッカー`、`Next actions / 次のアクション`、`Artifacts / 成果物`）を出力し、5段階の明確な判定（`go`、`fix-first`、`stop`、`proceed-with-risk`、`needs-owner-review`）を返します。

---

## ライフサイクル段階別スキル一覧

![25スキル・ライフサイクルマップ](assets/repo-skill-map-infographic.png)

| ライフサイクル段階 | スキルパッケージ (`slug`) | 主な監査スコープと防止する失敗モード | 決定論的検証スクリプト |
| --- | --- | --- | --- |
| ステージ 1：課題定義・データ診断 | [データ課題フレーミング (`data-question-framing`)](data-science-agent-skills/data-question-framing/) | 曖昧なビジネス・研究要望を測定可能なDS課題定義へ構造化 | `scripts/decision_canvas_validator.py` |
| ステージ 1：課題定義・データ診断 | [AIデータ準備度トリアージ (`ai-data-readiness-triage`)](data-science-agent-skills/ai-data-readiness-triage/) | AI・分析・モデリング着手前にデータの利用可能性と品質を判定 | `scripts/profile_table.py` |
| ステージ 1：課題定義・データ診断 | [データセット契約フォレンジック (`dataset-contract-forensics`)](data-science-agent-skills/dataset-contract-forensics/) | スキーマ・粒度・一意性・鮮度・欠損ルールを推論し契約違反を検出 | `scripts/profile_table.py` |
| ステージ 1：課題定義・データ診断 | [セマンティック系譜マッパー (`semantic-lineage-mapper`)](data-science-agent-skills/semantic-lineage-mapper/) | SQL・Notebook・パイプラインを横断してテーブル・列・指標の意味論的系譜を追跡 | `scripts/extract_lineage_tokens.py` |
| ステージ 1：課題定義・データ診断 | [メッシーデータ・クリーンルーム (`messy-data-cleanroom`)](data-science-agent-skills/messy-data-cleanroom/) | 生データを破壊せず、可逆かつ監査可能なクレンジング・隔離ルールを設計 | `scripts/profile_table.py` |
| ステージ 2：妥当性・リーク検証 | [リーケージ・アドバーサリ（データ漏洩レッドチーム） (`leakage-adversary`)](data-science-agent-skills/leakage-adversary/) | 目的変数・時系列・グループ・前処理のデータリーケージを敵対的視点で徹底検証 | `scripts/split_leakage_probe.py` |
| ステージ 2：妥当性・リーク検証 | [因果推論仮定スカウト (`causal-assumption-scout`)](data-science-agent-skills/causal-assumption-scout/) | 交絡・合流点バイアス・処置後変数の統制・識別可能性を点検し因果主張の妥当性を審査 | `scripts/confounder_backdoor_check.py` |
| ステージ 2：妥当性・リーク検証 | [小標本検出力・MDEプランナー (`small-data-power-planner`)](data-science-agent-skills/small-data-power-planner/) | 最小検出可能効果（MDE）・統計的検出力・少数サンプルでの過学習境界を算出 | `scripts/power_sample_size.py` |
| ステージ 2：妥当性・リーク検証 | [欠測メカニズム調査（MCAR / MAR / MNAR） (`missingness-mechanism-investigator`)](data-science-agent-skills/missingness-mechanism-investigator/) | 欠測がMCAR・MAR・MNARのいずれかを診断し、安易な平均値補完や行削除によるバイアスを防止 | `scripts/profile_table.py` |
| ステージ 2：妥当性・リーク検証 | [ベースライン＆アブレーション実験室 (`baseline-ablation-lab`)](data-science-agent-skills/baseline-ablation-lab/) | 複雑なモデルを採用する前に単純ベースラインとの比較・複数シード検証・アブレーションを徹底 | `scripts/ablation_delta_audit.py` |
| ステージ 3：再現性・パイプライン化 | [Notebook再現性パッケージャー (`notebook-repro-packager`)](data-science-agent-skills/notebook-repro-packager/) | Jupyter Notebookのセル実行順序の乱れ・未固定シード・絶対パス・依存ロック漏れを監査 | `scripts/notebook_repro_audit.py` |
| ステージ 3：再現性・パイプライン化 | [Notebook・トゥ・パイプライン・サージョン (`notebook-to-pipeline-surgeon`)](data-science-agent-skills/notebook-to-pipeline-surgeon/) | 探索的Notebookをモジュール化・べき等・テスト可能な本番パイプラインへ外科的に再構築 | `scripts/notebook_repro_audit.py` |
| ステージ 3：再現性・パイプライン化 | [実験プロヴェナンス台帳（来歴管理） (`experiment-provenance-ledger`)](data-science-agent-skills/experiment-provenance-ledger/) | データセットのSHA-256ハッシュ・Gitコミット状態・乱数シード・設定を実行ごとに記録 | `scripts/capture_provenance.py` |
| ステージ 3：再現性・パイプライン化 | [OSSデータサイエンス・サプライチェーン監査 (`oss-ds-supply-chain-auditor`)](data-science-agent-skills/oss-ds-supply-chain-auditor/) | 依存定義ファイルの未固定バージョン・直接URL参照・危険なpickle読み込みを監査 | `scripts/dependency_surface.py` |
| ステージ 3：再現性・パイプライン化 | [コスト意識型コンピュートプランナー (`cost-aware-compute-planner`)](data-science-agent-skills/cost-aware-compute-planner/) | 再試行期待値を織り込んだGPU・クラウド費用を見積もり、全量実行前に10%パイロット検証を徹底 | `scripts/compute_budget_estimator.py` |
| ステージ 4：評価・ガバナンス・SME協働 | [指標設計レビューボード (`metric-design-review-board`)](data-science-agent-skills/metric-design-review-board/) | 主要KPIの分母定義・集計期間・ガードレール指標・Goodhartの法則によるハック耐性を審査 | `scripts/metric_guardrail_check.py` |
| ステージ 4：評価・ガバナンス・SME協働 | [モデル評価リアリティチェック (`evaluation-reality-check`)](data-science-agent-skills/evaluation-reality-check/) | サブグループ別のスライス誤差・確率キャリブレーション・ビジネス価値への換算を監査 | `scripts/slice_error_auditor.py` |
| ステージ 4：評価・ガバナンス・SME協働 | [モデルリスク・コンプライアンスメモ (`model-risk-compliance-memo`)](data-science-agent-skills/model-risk-compliance-memo/) | 影響範囲（ブラスト半径）・人間による介入（HITL）・フォールバック・ロールバック責任者を審査 | `scripts/risk_tier_gate.py` |
| ステージ 4：評価・ガバナンス・SME協働 | [プライバシー保護データサイエンス (`privacy-preserving-ds`)](data-science-agent-skills/privacy-preserving-ds/) | 直接PII・準識別子による再識別リスク・データ最小化・保持期限ルールを監査 | `scripts/profile_table.py` |
| ステージ 4：評価・ガバナンス・SME協働 | [ドメインエキスパート協働ループ (`domain-expert-collaboration-loop`)](data-science-agent-skills/domain-expert-collaboration-loop/) | 専門家のアノテーション一致度（Cohenのκ係数）を計測し、境界事例の裁定基準を整備 | `scripts/sme_label_agreement.py` |
| ステージ 5：本番運用・監視・意思決定伝達 | [本番MLハンドオフ（運用引き継ぎ監査） (`production-ml-handoff`)](data-science-agent-skills/production-ml-handoff/) | モデルSHA-256・入出力スキーマ・p99レイテンシSLA・フォールバック・ロールバック条件を検証 | `scripts/handoff_readiness_audit.py` |
| ステージ 5：本番運用・監視・意思決定伝達 | [特徴量ストア準備度＆オンライン／オフライン整合性 (`feature-store-readiness`)](data-science-agent-skills/feature-store-readiness/) | 学習用バッチ特徴量と推論用オンライン特徴量の一致性（Train-Serve Skew）・時点結合・TTLを監査 | `scripts/online_offline_skew_check.py` |
| ステージ 5：本番運用・監視・意思決定伝達 | [ドリフトモニター設計 (`drift-monitor-designer`)](data-science-agent-skills/drift-monitor-designer/) | 平均シフト・分散爆発・定数列の崩壊・NaN混入・欠損率急増を検知し実践的なアラートを設計 | `scripts/drift_probe.py` |
| ステージ 5：本番運用・監視・意思決定伝達 | [データサイエンス・インシデント根本原因分析（RCA） (`data-science-incident-rca`)](data-science-agent-skills/data-science-incident-rca/) | データ取込・スキーマ・特徴量・モデル・指標定義の5層でイベント時系列を相関させ原因を特定 | `scripts/incident_timeline_correlator.py` |
| ステージ 5：本番運用・監視・意思決定伝達 | [ステークホルダー・インサイト・ストーリーテラー (`stakeholder-insight-storyteller`)](data-science-agent-skills/stakeholder-insight-storyteller/) | 検証済みエビデンスを、意思決定の問い・不確実性区間・前提条件を明示したエグゼクティブメモへ変換 | `scripts/memo_claim_evidence_check.py` |

---

## クイックスタート：一括検証・4言語リスト表示・フラットインストール

すべての補助スクリプトと契約テストはPython 3標準ライブラリのみで実装されており、追加パッケージのインストールなしで即座に実行できます。

```bash
# 全25スキルの厳格な契約テストとスクリプト動作スモークテストを実行
python scripts/catalog_cli.py validate

# 日本語・英語・中国語・韓国語でスキル一覧を表示
python scripts/catalog_cli.py list --lang ja
python scripts/catalog_cli.py list --lang en
python scripts/catalog_cli.py list --lang zh-CN
python scripts/catalog_cli.py list --lang ko

# エージェントのスキル自動検出向けにフラットなディレクトリ構成でインストール
python scripts/catalog_cli.py install --target ~/.codex/skills
python scripts/catalog_cli.py install --target ~/.claude/skills
python scripts/catalog_cli.py install --target ~/.gemini/config/skills

# エンドツーエンドのライフサイクル連携テストスイートを実行
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## マルチエージェント＆データ基盤の相互運用性

![プロバイダー互換性](assets/repo-provider-compatibility.png)

- **18種類のエージェント実行環境に対応**：OpenAI Codex、ChatGPT Agents、Anthropic Claude、Claude Code、Google Gemini、Gravity / Antigravity、GitHub Copilot、Cursor、Windsurf、Goose、OpenCode、OpenHands、LangGraph、CrewAI、AutoGen、LlamaIndex、Semantic Kernel、ローカルLLMエージェント。
- **翻訳調を排した4言語ネイティブ設計**：各スキルの `references/multilingual-guide.md` に、日本のデータサイエンス・MLOps現場で自然に使われる専門用語と8セクション見出し定義を収録しています。
