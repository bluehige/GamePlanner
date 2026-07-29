---
name: game-implementation-director
description: Implement an approved game work order through isolated changes, traceable tasks, tests, engine validation, and review without expanding scope.
---

# Game Implementation Director

승인된 기획과 Work Order를 실제 엔진 코드·씬·데이터로 구현한다. 구현 속도보다 **범위 보존, 추적 가능성, 작은 변경 단위, 즉시 검증**을 우선한다.

## 사용 시점

- Work Order와 필요한 Change Impact 분석이 완료된 뒤
- 프로토타입을 제품 코드로 다시 구현할 때
- 엔진 코드, 씬, 데이터, 파이프라인을 변경할 때

## 입력

- 승인된 Work Order
- 관련 Game Design Spec과 프로젝트 전용 스킬
- Change Impact 보고서
- 현재 branch, HEAD SHA, 테스트 기준선
- 엔진·플랫폼·장르 기술 팩
- 활성 Wiki 예방 규칙과 미해결 사건

## 외부 연동

- 일반 개발 규율은 `obra/superpowers`의 계획·격리 작업공간·TDD·리뷰 흐름을 우선 사용한다.
- 엔진별 API와 구현 패턴은 `gamedev-skills/awesome-gamedev-agent-skills`에서 현재 엔진에 필요한 최소 스킬만 로드한다.
- 외부 스킬이 프로젝트 계약과 충돌하면 프로젝트 계약이 우선한다.

## 절차

1. 기준 branch와 테스트 상태를 기록한다.
2. 격리된 branch 또는 worktree를 사용한다.
3. Work Order 수용 기준을 구현 작업과 검증 작업으로 분해한다.
4. 각 작업에 정확한 파일, 데이터, 씬, 테스트 경로를 지정한다.
5. 결정론적으로 검증 가능한 로직은 실패 테스트부터 작성한다.
6. 한 번에 하나의 계약만 변경하는 최소 구현을 수행한다.
7. 작업마다 관련 정적 검사와 엔진 검증을 실행한다.
8. 계획과 실제 변경의 차이를 기록한다.
9. 명세 준수 검토 후 코드·씬·데이터 품질 검토를 분리해 수행한다.
10. `15-game-verification-gate`를 통과하기 전 완료를 선언하지 않는다.

## 구현 단위 규칙

각 작업 단위는 다음을 가진다.

```yaml
task_id: IMP-001
work_order_id: WO-2026-0001
changes:
  - exact/path/to/file
contract_changed: placement-confirmation
expected_behavior: "배치 확정 뒤 기존 전투 시작 규칙을 호출한다"
tests:
  - exact/test/or/runtime-check
rollback: "이 작업의 단일 커밋 되돌리기"
```

## 하드 게이트

- 승인되지 않은 기능 개선을 함께 넣지 않는다.
- UI 구현 중 게임 규칙을 복제 계산하지 않는다.
- 프로토타입 코드를 검토 없이 제품 코드로 승격하지 않는다.
- 저장 스키마, 공개 데이터 ID, 입력 계약 변경은 별도 영향 분석 없이 진행하지 않는다.
- 테스트를 나중에 맞추기 위해 수용 기준을 임의로 낮추지 않는다.
- 기존 테스트가 실패한 기준선이면 원인과 허용 범위를 먼저 기록한다.

## 산출물

```text
docs/game-planner/implementation/<work-order-id>/
├── IMPLEMENTATION_PLAN.md
├── TRACEABILITY.md
├── VALIDATION_LOG.md
└── DEVIATIONS.md
```

`TRACEABILITY.md`는 다음 연결을 유지한다.

```text
요구사항 → 시스템 계약 → 작업 → 파일/씬/데이터 → 테스트/실행 증거
```

## 완료 게이트

- 모든 변경이 Work Order의 범위에 매핑된다.
- 범위 밖 변경이 없거나 별도 승인 기록이 있다.
- 테스트와 엔진 검증이 변경 직후 실행됐다.
- 원래 기준선과 비교 가능한 결과가 있다.
- 디버깅이 필요한 실패를 숨기거나 우회하지 않았다.
- 검증 게이트에 넘길 증거 목록이 준비됐다.
