---
name: playtest-experiment-director
description: Design and analyze game playtests as decision experiments with hypotheses, participant profiles, observation protocols, metrics, and keep-change-kill thresholds.
---

# Playtest Experiment Director

플레이테스트를 “재미있었나요?”라는 감상 수집이 아니라 **의사결정을 위한 관찰 실험**으로 설계한다.

## 사용 시점

- 핵심 루프·조작·UI·튜토리얼·난이도 가정을 검증할 때
- 프로토타입 유지·폐기 결정을 내릴 때
- 마일스톤, 수직 슬라이스, 출시 후보를 평가할 때
- 상충하는 내부 의견을 실제 사용자 행동으로 판별할 때

## 입력

- 검증할 게임 계약 또는 Work Order
- 고정된 빌드 ID, branch, SHA, 플랫폼
- 대상 사용자 프로필
- 현재 가설과 결정 가능한 선택지
- 계측 가능한 이벤트와 기록 장비
- 개인정보·녹화·보상 동의 정책

## 절차

1. 이번 테스트가 바꿀 수 있는 결정을 한 문장으로 적는다.
2. 반증 가능한 가설을 작성한다.
3. 통과·실패·보류 임계치를 테스트 전에 정한다.
4. 대상 사용자와 제외 조건을 정한다.
5. 설명 없이 관찰할 구간과 안내할 구간을 분리한다.
6. 실제 플레이 순서, 과제, 중단 조건을 작성한다.
7. 진행자의 금지 질문과 개입 기준을 정한다.
8. 행동·시간·오류·재시도·선택과 발화를 분리 기록한다.
9. 세션 직후 사실, 해석, 권고를 따로 정리한다.
10. 문제를 심각도와 빈도뿐 아니라 핵심 기둥 영향으로 분류한다.
11. 미리 정한 임계치에 따라 유지·수정·폐기·추가 실험을 결정한다.
12. 결과를 `17-game-dev-memory`의 PLAYTEST 사건으로 편입한다.

## 최소 실험 계약

```yaml
hypothesis: "초회 플레이어가 설명 없이 몬스터 배치를 완료한다"
decision_if_pass: "현재 배치 흐름 유지"
decision_if_fail: "정보 계층과 입력 흐름 재설계"
participants:
  profile: "장르 경험이 적은 목표 사용자"
  count: 5
success_thresholds:
  completion_rate: ">= 80%"
  median_time: "<= 45초"
  facilitator_interventions: 0
failure_signals:
  - "핵심 행동을 10초 이상 찾지 못함"
  - "확정 상태를 인지하지 못함"
```

## 관찰 우선순위

1. 실제 행동과 상태 전환
2. 반복되는 망설임·오입력·우회
3. 성공·실패 시간과 개입 횟수
4. 플레이 뒤의 설명과 감정
5. 선호도·아이디어 제안

말한 선호보다 실제 행동을 우선하되, 행동의 이유를 임의로 단정하지 않는다.

## 하드 게이트

- 서로 다른 빌드를 같은 실험 결과로 합치지 않는다.
- 진행자가 정답 행동을 유도하지 않는다.
- 핵심 가설이 여러 개인 세션은 결과를 분리한다.
- 표본이 작을 때 비율을 시장 전체의 사실로 일반화하지 않는다.
- 플레이어 제안을 그대로 기능 요구사항으로 채택하지 않는다.
- 플레이테스트 실패를 밸런스 숫자만으로 즉시 덮지 않는다.

## 산출물

```text
docs/game-planner/playtests/<test-id>/
├── TEST_PLAN.md
├── PARTICIPANT_MATRIX.md
├── OBSERVATION_LOG.md
├── FINDINGS.md
├── DECISION.md
└── EVIDENCE_INDEX.md
```

## 완료 게이트

- 테스트가 어떤 결정을 지원하는지 명확하다.
- 가설과 임계치가 사전에 고정됐다.
- 동일 빌드와 동일 핵심 과제를 사용했다.
- 사실·해석·권고가 분리됐다.
- 다음 결정과 담당 작업이 기록됐다.
