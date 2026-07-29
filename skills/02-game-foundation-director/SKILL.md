---
name: game-foundation-director
description: Interrogate, synthesize, and audit the foundational decisions of a game before major planning or implementation begins.
---

# Game Foundation Director

큰 기둥을 세우기 전에 게임의 플레이 경험, 핵심 루프, 의미 있는 결정, 범위, 위험 가정을 질문으로 확정한다. 일반적인 `grill-me`를 게임 제작 계약으로 확장한 스킬이다.

## 사용 시점

- 신규 게임의 핵심 기획을 시작할 때
- 기존 기획이 장황하지만 실제 플레이가 정의되지 않았을 때
- 팀·Agent마다 게임을 다르게 이해할 때
- 방향 전환, 대규모 업데이트, 핵심 시스템 교체 전

## 입력

- 선택된 아이디어 브리프 또는 기존 GDD
- 제작 조건과 금지 구조
- 이미 확정된 사용자 결정
- 기존 코드·프로토타입·플레이테스트 증거
- 해결되지 않은 충돌과 질문

## 외부 연동

설치돼 있으면 `mattpocock/skills`의 다음 원칙을 사용한다.

- `grilling`: 한 번에 결정 하나, 각 질문에 권장 답변, 환경에서 확인 가능한 사실은 직접 조사
- `domain-modeling`: 용어 충돌 즉시 지적, 구체적 경계 시나리오, 구현 정보 없는 `CONTEXT.md`
- `wayfinder`: 한 세션에 들어가지 않는 대형 기획을 결정 티켓과 미지 영역으로 분리

GamePlanner는 이 원칙 위에 게임 전용 질문 트리와 종료 게이트를 추가한다.

## 절차

### 1. 모드 선택

- `GRILL`: 사용자와 한 질문씩 핵심 결정을 확정
- `SYNTHESIZE`: 이미 나온 답변을 계약 문서로 정리
- `AUDIT`: 기존 기획의 누락, 충돌, 과잉 범위 검사

### 2. 사실과 결정을 분리

엔진 기능, 저장소 상태, 플랫폼 제한처럼 조사 가능한 사실은 직접 확인한다. 플레이어 판타지, 핵심 기둥, 허용할 실패 비용처럼 제작자가 결정해야 하는 사항만 질문한다.

### 3. 결정 트리

아래 순서를 의존성에 따라 한 질문씩 진행한다.

1. 플레이어는 누구이며 어떤 역할 판타지를 얻는가
2. 플레이어가 가장 자주 반복하는 1~3개의 핵심 동사는 무엇인가
3. 30초, 5분, 한 세션 루프는 각각 무엇인가
4. 반복해서 내려야 하는 의미 있는 결정은 무엇인가
5. 정보, 자원, 공간, 시간 중 무엇이 그 결정을 어렵게 만드는가
6. 승패에 실력, 전략, 지식, 운이 각각 어떻게 기여하는가
7. 실패 시 무엇을 잃고 어떻게 회복하는가
8. 게임을 규정하는 기둥 2~4개는 무엇인가
9. 의도적으로 하지 않을 것은 무엇인가
10. 콘텐츠 제작량을 폭발시키는 요소는 무엇인가
11. 가장 위험한 재미 가정과 기술 가정은 무엇인가
12. 프로토타입에서 한 가지 무엇을 증명해야 하는가
13. 어떤 결과가 나오면 유지·재설계·폐기할 것인가

### 4. 용어 고정

- 동일 단어가 다른 시스템을 뜻하면 이름을 분리한다.
- `CONTEXT.md`에는 게임 세계와 규칙의 의미만 기록한다.
- 기술 선택은 되돌리기 어렵고 놀랍고 실제 트레이드오프가 있을 때만 ADR 후보로 만든다.

### 5. 대형 기획 분할

결정이 한 세션을 넘으면 다음 티켓으로 나눈다.

- `research`: 외부 사실 조사
- `prototype`: 구체물을 만들어야 결정 가능한 문제
- `grilling`: 제작자의 선택이 필요한 문제
- `task`: 결정을 막는 선행 작업
- `fog`: 질문 자체를 아직 정확히 만들 수 없는 영역

### 6. 문서 합성

`templates/`의 파일을 사용해 계약 문서를 생성하고 서로 교차 참조한다.

## 하드 게이트

- 한 메시지에 여러 독립 결정을 몰아서 질문하지 않는다.
- 사용자의 결정을 Agent가 대신 답하고 승인된 것으로 처리하지 않는다.
- “재미있게”, “직관적으로”, “풍부하게” 같은 형용사를 측정 가능한 행동으로 바꾸지 못하면 미결정으로 남긴다.
- 기둥은 2~4개를 기본으로 하며, 모든 기능이 최소 하나의 기둥에 연결돼야 한다.
- 가장 위험한 가정과 폐기 기준이 없는 상태에서 대규모 제작 계획으로 넘어가지 않는다.

## 산출물

```text
docs/foundation/
├── GAME_CONTRACT.md
├── CONTEXT.md
├── DECISION_LOG.md
├── RISK_REGISTER.md
├── PROTOTYPE_BRIEF.md
├── OUT_OF_SCOPE.md
└── OPEN_QUESTIONS.md
```

## 완료 게이트

```yaml
foundation_exit_gate:
  critical_unknowns: 0
  contradictory_decisions: 0
  game_pillars: "2-4"
  player_fantasy_defined: true
  core_loop_defined: true
  meaningful_decisions_defined: true
  primary_risk_defined: true
  prototype_question_defined: true
  keep_redesign_kill_criteria_defined: true
  out_of_scope_defined: true
  user_approved_summary: true
```

승인이 없는 비대화형 작업에서는 `user_approved_summary`를 `pending`으로 표시하고 구현이 아니라 검토 가능한 초안까지만 만든다.
