---
name: game-ui-ux-bridge
description: Bridge GamePlanner contracts to the dedicated Game UI/UX Rules skills without duplicating their design and evidence system.
---

# Game UI/UX Bridge

GamePlanner의 게임 계약과 Work Order를 `bluehige/UI_UX_Skill_for_Game`의 전용 UI·UX 절차에 전달하고, 결과를 구현·검증 흐름으로 되돌린다.

## 사용 시점

- HUD, 메뉴, 배치 화면, 인벤토리, 튜토리얼, 결과 화면
- 입력 체계, 포커스, 접근성, 반응형, 정보 계층
- 기존 UI 감사와 게임별 UI Skill 생성

## 입력

- Game Contract와 관련 시스템 계약
- 화면이 답해야 할 플레이어 질문
- 현재 게임 상태의 source-of-truth
- 지원 입력 방식과 해상도
- 실제 데이터·상태·스크린샷·빌드
- UI Work Order와 변경 영향 보고서

## 외부 연동

1. 설치돼 있으면 `game-ui-ux-director`를 호출한다.
2. 프로젝트별 장기 작업이면 `game-ui-ux-project-builder`로 전용 UI Skill을 만든다.
3. 사용한 upstream ref를 결과에 기록한다.

외부 스킬이 없으면 화면 계약, P0~P3 정보 우선순위, 입력·상태 매트릭스, 검증 계획까지만 작성하고 정식 UI 승인으로 간주하지 않는다.

## 절차

1. 화면의 `player_question`, `primary_decision`, `primary_action`을 고정한다.
2. Game Contract에서 의도된 난이도와 UI가 만들면 안 되는 마찰을 분리한다.
3. 외부 UI Skill로 감사 또는 설계를 수행한다.
4. 결과가 게임 규칙이나 밸런스 변경을 요구하면 UI 작업에 포함하지 않고 새 Work Order로 분리한다.
5. 구현 후 실제 엔진 렌더, 입력, 화면 전환, 사용자 테스트 증거를 `15`와 `16`에 전달한다.

## 하드 게이트

- 가짜 데이터로 만든 예쁜 목업을 구현 승인 근거로 쓰지 않는다.
- UI가 게임 상태를 중복 계산하거나 규칙을 재정의하지 않는다.
- 지원한다고 명시한 입력 중 하나로 진행할 수 없으면 실패다.
- 자동 레이아웃·노드 존재·비겹침 검사를 실제 UX 승인으로 오인하지 않는다.
- 외부 UI Skill이 없는데 그 평가 모델을 사용했다고 주장하지 않는다.

## 산출물

```text
docs/game-planner/ui/
├── SCREEN_CONTRACTS.md
├── INFORMATION_PRIORITY.md
├── INPUT_STATE_MATRIX.md
├── UI_IMPLEMENTATION_PLAN.md
└── UI_EVIDENCE_PLAN.md
```

## 완료 게이트

- 화면의 핵심 질문과 행동이 명확하다.
- UI 변경과 게임 규칙 변경이 분리됐다.
- 실제 데이터 source가 연결됐다.
- 모든 지원 입력과 오류·빈 상태·로딩 상태가 정의됐다.
- `15`가 요구할 증거 수준이 지정됐다.
