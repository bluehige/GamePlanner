---
name: game-work-order
description: Normalize a natural-language game-development request into a bounded, testable work contract before files are changed.
---

# Game Work Order

사용자의 자연어 명령을 목표, 범위, 비범위, 영향 시스템, 수용 기준, 검증법, 롤백 기준이 있는 실행 계약으로 바꾼다.

## 사용 시점

- 기능 추가, UI 수정, 밸런스 조정, 리팩터링, 버그 수정, 자산 교체 전
- 여러 문서·브랜치·버전이 섞여 오해 가능성이 있을 때
- “간단하게”, “예쁘게”, “기존처럼”처럼 해석 여지가 큰 요청

## 입력

- 사용자 원문
- 관련 Game Contract와 시스템 계약
- 현재 branch, HEAD SHA, 빌드
- 영향받을 가능성이 있는 파일·데이터·씬
- 이전 사건과 활성 예방 규칙

## 절차

1. 원문을 보존하고 한 문장 목표를 작성한다.
2. 플레이어 결과와 시스템 결과를 분리한다.
3. source-of-truth와 기준 버전을 고정한다.
4. `in_scope`와 `out_of_scope`를 명시한다.
5. 변경이 금지된 계약과 파일을 적는다.
6. 수용 기준을 관찰 가능한 상태로 작성한다.
7. 필요한 검증을 E1~E4로 배치한다.
8. 위험도를 `low`, `medium`, `high`, `prototype`으로 분류한다.
9. 롤백 기준점과 중단 조건을 기록한다.
10. `schemas/work-order.schema.json`과 `scripts/validate_work_order.py`로 검사한다.

## 위험도

- `low`: 문구, 단일 데이터 값, 독립 자산 등 파급이 제한됨
- `medium`: 화면, 입력, 단일 시스템 동작 변경
- `high`: 저장, 전투 공식, 아키텍처, 다수 씬·데이터, 출시 빌드
- `prototype`: 제품 계약을 바꾸지 않는 격리 실험

## 하드 게이트

- UI 작업에 밸런스 변경을, 리팩터링에 기능 변경을 숨기지 않는다.
- `out_of_scope`가 빈 상태로 중·고위험 작업을 시작하지 않는다.
- “기존과 동일”은 기준 branch·SHA·빌드가 없으면 수용 기준이 아니다.
- 검증 명령을 실행할 수 없는 경우 대체 증거와 한계를 적는다.
- 사용자 결정을 다시 물을 수 없는 상황에서는 가장 보수적인 범위를 선택하고 가정을 명시한다.

## 산출물

`docs/game-planner/work-orders/WO-YYYY-NNNN.json`

```json
{
  "work_order_id": "WO-2026-0001",
  "request_summary": "배치 화면을 단순화한다",
  "raw_request_ref": "session-or-issue-link",
  "interpreted_goal": {
    "player_outcome": "플레이어가 핵심 배치를 완료한다",
    "system_outcome": "기존 전투 규칙은 유지한다"
  },
  "source_of_truth": [],
  "in_scope": [],
  "out_of_scope": [],
  "forbidden_changes": [],
  "acceptance_criteria": [],
  "affected_systems": [],
  "verification": [],
  "risk_tier": "medium",
  "rollback": {"baseline_sha": "", "strategy": ""},
  "assumptions": []
}
```

## 완료 게이트

- 사용자 원문과 Agent 해석을 구분할 수 있다.
- 범위와 비범위가 상호 모순되지 않는다.
- 모든 수용 기준에 검증 방법이 대응한다.
- 위험도와 변경 영향 분석 필요성이 결정됐다.
- Work Order 검증 스크립트가 통과한다.
