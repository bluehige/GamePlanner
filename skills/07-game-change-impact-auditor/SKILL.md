---
name: game-change-impact-auditor
description: Map direct and indirect effects of a proposed game change, define regression coverage, and protect unrelated systems before implementation.
---

# Game Change Impact Auditor

한 기능의 수정이 다른 시스템, 저장, 데이터, UI, 자산, 튜토리얼을 깨뜨리는 문제를 구현 전에 찾는다.

## 사용 시점

- `medium` 또는 `high` Work Order
- 기존 기능을 교체·통합·삭제하는 작업
- UI, 입력, 전투, 저장, 콘텐츠 구조가 연결된 변경
- 버전 간 기능을 합치거나 backport할 때

## 입력

- 검증된 Work Order
- 시스템 계약과 source map
- 코드·씬·데이터 참조
- 기존 저장 샘플과 테스트
- 최근 관련 사건

## 절차

1. **계약 diff**
   - 현재 행동과 요청 후 행동을 상태 단위로 비교한다.
2. **직접 영향**
   - 수정 파일, 씬, 컴포넌트, 리소스, 데이터 테이블을 찾는다.
3. **간접 영향**
   - 호출자, 구독자, 저장, UI 표시, 튜토리얼, 현지화, 성능을 추적한다.
4. **플레이 경로 영향**
   - 시작, 진행, 실패, 재시도, 저장·로드, 결과 화면에 미치는 영향을 본다.
5. **회귀 범위**
   - 변경 전 유지돼야 할 대표 시나리오와 엣지 케이스를 정의한다.
6. **롤백 설계**
   - feature flag, 데이터 버전, branch 기준점, 자산 복원 경로를 정한다.
7. **위험 재평가**
   - Work Order의 위험도가 낮게 잡혔다면 상향한다.

## 검사 축

```text
플레이 경험
게임 규칙
UI와 입력
씬·프리팹·노드
데이터와 콘텐츠 참조
저장과 마이그레이션
AI와 애니메이션
오디오와 VFX
현지화
성능·메모리·로딩
테스트와 빌드
```

## 하드 게이트

- 파일 검색 결과만으로 영향 범위를 완성했다고 보지 않는다. 런타임 연결과 데이터 참조를 별도로 본다.
- 삭제 또는 이름 변경은 참조 탐색과 저장 호환 계획 없이 승인하지 않는다.
- UI 표시용 계산을 새로 만들면서 게임 규칙의 두 번째 source-of-truth를 만들지 않는다.
- 영향이 불명확한 고위험 시스템은 격리 프로토타입 또는 feature flag를 요구한다.

## 산출물

`docs/game-planner/impacts/IMPACT-<work-order-id>.md`

```yaml
change: ""
direct_effects: []
indirect_effects: []
contract_changes: []
preserved_behaviors: []
regression_scenarios: []
data_migrations: []
performance_risks: []
rollback:
  baseline_sha: ""
  procedure: []
final_risk: high
```

## 완료 게이트

- 직접·간접 영향과 모르는 영역이 분리됐다.
- 유지해야 할 기존 동작이 시나리오로 기록됐다.
- 저장·데이터·콘텐츠 참조 영향이 판정됐다.
- 회귀 테스트와 롤백 경로가 있다.
- Work Order 범위를 수정해야 하는지 결정됐다.
