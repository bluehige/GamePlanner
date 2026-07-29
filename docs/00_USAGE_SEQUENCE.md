# 00. 게임 제작 사용 순서

## A. 새 게임 발굴

```text
00 Router
→ 01 Idea Portfolio
→ 02 Foundation Grill
→ 03 Project Builder
→ 04 Prototype Gate
→ 05 Game Design Spec
```

- 이미 게임 콘셉트가 확정됐다면 `01`은 생략한다.
- 기존 IP나 계약 프로젝트처럼 핵심 방향이 이미 고정돼도 `02`의 `AUDIT` 모드로 모순과 누락을 검사한다.
- 핵심 재미나 기술 실현 가능성이 불확실하면 `04`를 생략하지 않는다.

## B. 기능 제작 반복

```text
00 Router
→ 17 Memory PREFLIGHT
→ 06 Work Order
→ 07 Change Impact
→ 08/09/10/11 중 필요한 전문 스킬
→ 12 Implementation
→ 14 Data/Save Validation 조건부
→ 15 Verification
→ 17 Memory RECORD/HANDOFF
```

## C. 오류 수정

```text
00 Router
→ 17 관련 사건·활성 규칙 조회
→ 06 버그 수정 Work Order
→ 13 Systematic Debugging
→ 07 수정 영향 분석
→ 12 최소 수정
→ 14 조건부 검증
→ 15 원증상·회귀 검증
→ 17 사건 종결·예방 규칙 승격
```

## D. 플레이테스트와 방향 수정

```text
16 Playtest Experiment
→ 관찰·지표 수집
→ 17 PLAYTEST 기록
→ 02/05 계약 변경 필요성 판정
→ 06 Work Order
→ 이후 제작 반복
```

## E. 출시

```text
15 기능별 최신 증거 확인
→ 16 출시 후보 플레이테스트
→ 18 성능·패키징·플랫폼 검증
→ 17 Release/Handoff 기록
```

## 단계 생략 규칙

단계를 생략할 때는 Route Packet에 이유와 위험을 기록한다. `15`는 완료 선언 전 생략할 수 없고, 중요한 결정·사건이 있었던 세션에서 `17`을 생략할 수 없다.
