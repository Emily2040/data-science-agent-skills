# 데이터 사이언스 에이전트 스킬 — 카탈로그 인덱스

**Language / 语言 / 言語 / 언어**: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

| Stage | Skill | Summary | Script |
| --- | --- | --- | --- |
| 1단계: 문제 정의 및 데이터 트리아지 | [데이터 문제 정의 및 프레이밍 (`data-question-framing`)](data-question-framing/) | 모호한 비즈니스·연구 요청을 측정 가능한 데이터 사이언스 문제로 구조화 | `scripts/decision_canvas_validator.py` |
| 1단계: 문제 정의 및 데이터 트리아지 | [AI 데이터 준비도 트리아지 (`ai-data-readiness-triage`)](ai-data-readiness-triage/) | 예산과 엔지니어링 투입 전 AI·분석·모델링용 데이터 준비 상태 진단 | `scripts/profile_table.py` |
| 1단계: 문제 정의 및 데이터 트리아지 | [데이터셋 계약 포렌식 (`dataset-contract-forensics`)](dataset-contract-forensics/) | 스키마·집계 단위(Grain)·고유성·최신성·결측 계약을 추론 및 검증 | `scripts/profile_table.py` |
| 1단계: 문제 정의 및 데이터 트리아지 | [시맨틱 리니지 매퍼 (`semantic-lineage-mapper`)](semantic-lineage-mapper/) | SQL, 노트북, 파이프라인 전반에서 테이블·컬럼·지표의 의미론적 계보 추적 | `scripts/extract_lineage_tokens.py` |
| 1단계: 문제 정의 및 데이터 트리아지 | [메시 데이터 클린룸 (`messy-data-cleanroom`)](messy-data-cleanroom/) | 원본 데이터를 훼손하지 않고 가역적·감사가능한 정제 및 격리(Quarantine) 규칙 설계 | `scripts/profile_table.py` |
| 2단계: 타당성 및 누수 검증 | [데이터 누수(Leakage) 레드팀 (`leakage-adversary`)](leakage-adversary/) | 타깃·시계열·그룹·전처리 데이터 누수를 적대적(Red-team) 관점에서 탐지 및 차단 | `scripts/split_leakage_probe.py` |
| 2단계: 타당성 및 누수 검증 | [인과 추론 가정 스카우트 (`causal-assumption-scout`)](causal-assumption-scout/) | 교란변수·충돌변수(Collider)·처치 후 통제변수 및 식별 가능성을 점검하여 인과 주장 검증 | `scripts/confounder_backdoor_check.py` |
| 2단계: 타당성 및 누수 검증 | [소표본 검정력·MDE 플래너 (`small-data-power-planner`)](small-data-power-planner/) | 최소감지효과(MDE), 통계적 검정력, 소표본 과적합 경계(EPV)를 산출 | `scripts/power_sample_size.py` |
| 2단계: 타당성 및 누수 검증 | [결측 메커니즘 조사기 (MCAR / MAR / MNAR) (`missingness-mechanism-investigator`)](missingness-mechanism-investigator/) | 결측치의 MCAR·MAR·MNAR 메커니즘을 진단하고 단순 평균 대체·행 삭제 편향을 방지 | `scripts/profile_table.py` |
| 2단계: 타당성 및 누수 검증 | [베이스라인 및 어블레이션 랩 (`baseline-ablation-lab`)](baseline-ablation-lab/) | 복잡한 모델 채택 전 단순 베이스라인 비교, 다중 시드 검증, 피처 어블레이션을 강제 | `scripts/ablation_delta_audit.py` |
| 3단계: 재현성 및 파이프라인 엔지니어링 | [노트북 재현성 패키저 (`notebook-repro-packager`)](notebook-repro-packager/) | Jupyter 노트북의 셀 역순 실행, 미고정 난수 시드, 절대 경로, 의존성 잠금 누락을 감사 | `scripts/notebook_repro_audit.py` |
| 3단계: 재현성 및 파이프라인 엔지니어링 | [노트북-파이프라인 리팩터링 서전 (`notebook-to-pipeline-surgeon`)](notebook-to-pipeline-surgeon/) | 탐색적 노트북을 모듈화·멱등성·단위 테스트를 갖춘 프로덕션 파이프라인으로 전환 | `scripts/notebook_repro_audit.py` |
| 3단계: 재현성 및 파이프라인 엔지니어링 | [실험 프로비넌스(출처) 원장 (`experiment-provenance-ledger`)](experiment-provenance-ledger/) | 실험별 데이터셋 SHA-256 해시, Git 커밋·더티 상태, 난수 시드, 하이퍼파라미터를 기록 | `scripts/capture_provenance.py` |
| 3단계: 재현성 및 파이프라인 엔지니어링 | [오픈소스 DS 공급망 감사기 (`oss-ds-supply-chain-auditor`)](oss-ds-supply-chain-auditor/) | Python·DS 의존성 매니페스트의 버전 미고정, 직접 URL 설치, 안전하지 않은 피클(Pickle) 로드를 감사 | `scripts/dependency_surface.py` |
| 3단계: 재현성 및 파이프라인 엔지니어링 | [비용 인지형 컴퓨팅 플래너 (`cost-aware-compute-planner`)](cost-aware-compute-planner/) | 재시도 기댓값이 반영된 GPU·클라우드 비용을 산출하고 전체 학습 전 10% 파일럿 게이트를 적용 | `scripts/compute_budget_estimator.py` |
| 4단계: 평가, 거버넌스 및 전문가 루프 | [지표 설계 리뷰 보드 (`metric-design-review-board`)](metric-design-review-board/) | 핵심 KPI의 분모 정의, 집계 윈도우, 가드레일 지표, 굿하트 법칙(게이밍) 취약점을 심사 | `scripts/metric_guardrail_check.py` |
| 4단계: 평가, 거버넌스 및 전문가 루프 | [모델 평가 리얼리티 체크 (`evaluation-reality-check`)](evaluation-reality-check/) | 세부 집단(Slice)별 오차 격차, 확률 보정(Calibration), 오프라인 지표의 비즈니스 전환 타당성 감사 | `scripts/slice_error_auditor.py` |
| 4단계: 평가, 거버넌스 및 전문가 루프 | [모델 리스크 및 컴플라이언스 메모 (`model-risk-compliance-memo`)](model-risk-compliance-memo/) | 모델 영향 범위(Blast Radius), 인간 개입(HITL) 통제, 폴백 정책, 롤백 책임자를 검증 및 문서화 | `scripts/risk_tier_gate.py` |
| 4단계: 평가, 거버넌스 및 전문가 루프 | [프라이버시 보호 데이터 사이언스 (`privacy-preserving-ds`)](privacy-preserving-ds/) | 직접 개인정보(PII), 준식별자(Quasi-identifier) 재식별 위험, 최소 수집 및 보존 기한을 감사 | `scripts/profile_table.py` |
| 4단계: 평가, 거버넌스 및 전문가 루프 | [도메인 전문가(SME) 협업 루프 (`domain-expert-collaboration-loop`)](domain-expert-collaboration-loop/) | 전문가 간 라벨 일치도(Cohen's Kappa)를 측정하고 경계 사례에 대한 라벨 조정 루브릭 수립 | `scripts/sme_label_agreement.py` |
| 5단계: 프로덕션 운영 및 인사이트 전달 | [프로덕션 ML 핸드오프 (`production-ml-handoff`)](production-ml-handoff/) | 모델 SHA-256 해시, 입출력 스키마, p99 지연시간 SLA, 폴백 베이스라인, 롤백 트리거를 검증 | `scripts/handoff_readiness_audit.py` |
| 5단계: 프로덕션 운영 및 인사이트 전달 | [피처 스토어 준비도 및 온라인·오프라인 정합성 (`feature-store-readiness`)](feature-store-readiness/) | 오프라인 학습 피처와 온라인 서빙 피처 간 정합성(Train-Serve Skew), 시점 정합 조인, TTL을 감사 | `scripts/online_offline_skew_check.py` |
| 5단계: 프로덕션 운영 및 인사이트 전달 | [드리프트 모니터 디자이너 (`drift-monitor-designer`)](drift-monitor-designer/) | 평균 이동, 분산 폭증, 상수 컬럼 깨짐, NaN 오염, 결측률 급증을 탐지하고 실행 가능한 알림 설계 | `scripts/drift_probe.py` |
| 5단계: 프로덕션 운영 및 인사이트 전달 | [데이터 사이언스 인시던트 근본원인분석(RCA) (`data-science-incident-rca`)](data-science-incident-rca/) | 데이터 수집·스키마·피처·모델·지표 5개 계층의 이벤트 타임라인을 상관 분석해 장애 원인 규명 | `scripts/incident_timeline_correlator.py` |
| 5단계: 프로덕션 운영 및 인사이트 전달 | [이해관계자 인사이트 스토리텔러 (`stakeholder-insight-storyteller`)](stakeholder-insight-storyteller/) | 검증된 분석 근거를 의사결정 요청, 불확실성 구간, 한계점이 명시된 임원용 의사결정 메모로 구조화 | `scripts/memo_claim_evidence_check.py` |
