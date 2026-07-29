---
name: game-idea-portfolio-router
description: Generate and compare mechanically distinct game concept candidates before selecting one for foundation design.
---

# Game Idea Portfolio Router

표현만 다른 아이디어 목록이 아니라 **플레이 동사, 의사결정 구조, 실패 방식, 제작 위험이 서로 다른 후보 포트폴리오**를 만든다.

## 사용 시점

- 게임 콘셉트가 아직 정해지지 않았을 때
- 기존 아이디어를 다른 방향으로 비틀어야 할 때
- 하나의 익숙한 장르 조합에 사고가 고착됐을 때

## 사용하지 말아야 할 때

- 핵심 게임 계약이 이미 승인됐고 단일 기능만 제작하는 경우
- 사용자가 명확한 콘셉트를 변경하지 말라고 지정한 경우

## 입력

- 제작자 강점과 약점
- 엔진, 플랫폼, 예산, 팀 규모, 목표 기간이 아닌 **허용 제작 범위**
- 금지 구조와 반드시 사용할 자산
- 시장·테마·장르 제약
- 기존 후보와 피해야 할 유사작

## 외부 연동

가능하면 `external/UPSTREAMS.lock.json`에 고정된 `bluehige/idea-diversity-engine`의 `game-design` 확장팩을 사용한다. 비주얼 후보가 필요하면 `visual-3d-design`, 검수 후보가 필요하면 `software-qa`를 추가한다.

외부 스킬이 없으면 아래 내부 층화 절차를 수행하며, 결과에 `external_engine_used: false`를 기록한다.

## 절차

1. **전형적 해법 명시**
   - 이 요청에서 LLM이 가장 먼저 낼 법한 장르 조합과 메커니즘을 적는다.
2. **해결 공간 층화**
   - 핵심 동사
   - 정보 비대칭
   - 자원과 시간 구조
   - 실패·회복 구조
   - 동료·적과의 관계
   - 공간·카메라
   - 세션 길이
   - 콘텐츠 생산 방식
3. **후보 생성**
   - 각 후보는 최소 두 개의 층에서 다른 작동 원리를 가져야 한다.
4. **의미 중복 제거**
   - 테마와 이름만 다른 후보는 하나로 합친다.
5. **제약·위험 평가**
   - 재미 가정, 기술 위험, 콘텐츠 비용, UI 복잡도, 밸런스 부담을 평가한다.
6. **포트폴리오 선택**
   - 안전 후보, 차별화 후보, 저비용 검증 후보를 포함한다.
7. **Foundation 전달**
   - 각 후보를 `02-game-foundation-director`가 질문할 수 있는 브리프로 변환한다.

## 하드 게이트

- 낮은 전형성을 품질이나 시장 성공 가능성으로 해석하지 않는다.
- 후보 수를 채우기 위해 실행 불가능한 안을 유지하지 않는다.
- 최종 선택을 Agent가 독단적으로 확정하지 않는다. 추천과 근거를 제공하고 선택 상태를 기록한다.
- 기존 작품의 고유 표현·캐릭터·아트 스타일을 복제하는 방향을 추천하지 않는다.

## 산출물

```yaml
idea_portfolio:
  constraints: []
  typical_solution: ""
  candidates:
    - id: C01
      one_line: ""
      player_fantasy: ""
      core_verbs: []
      decision_engine: ""
      failure_recovery: ""
      production_shape: ""
      biggest_risk: ""
      cheapest_test: ""
      similarity_notes: []
  recommendation:
    primary: C01
    alternative: C03
    reason: ""
```

## 완료 게이트

- 후보가 이름과 테마가 아니라 작동 원리로 구분된다.
- 모든 후보가 제작 제약을 통과하거나 명시적으로 실험 후보로 표시됐다.
- 추천 후보의 가장 위험한 가정과 가장 싼 검증법이 정의됐다.
- 선택된 후보가 `02`의 입력 브리프로 전달 가능하다.
