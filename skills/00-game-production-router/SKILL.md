---
name: game-production-router
description: Route any game-development request to the smallest safe sequence of planning, implementation, verification, memory, and release skills.
---

# Game Production Router

게임 제작 요청을 바로 수행하지 말고 현재 단계, 계약 상태, 위험도, 필요한 증거를 판독해 **가장 작은 안전한 스킬 조합**으로 연결한다.

## 사용 시점

- 새 게임 아이디어, 기획, 프로토타입, 구현, 수정, 디버깅, 검수, 출시 요청이 들어왔을 때
- 저장소 작업을 재개하거나 다른 Agent가 넘긴 작업을 인수할 때
- 요청이 여러 제작 단계를 동시에 포함할 때

## 사용하지 말아야 할 때

- 게임과 무관한 일반 문서·웹·업무 자동화 요청
- 이미 상위 저장소 규칙이 정확한 전용 라우터를 지정한 경우

## 입력

- 사용자 원문 요청
- 저장소 `AGENTS.md`와 하위 지침
- `.game-planner/config.json`
- 최신 `.game-wiki/handoffs/` 문서
- 관련 Game Contract, Work Order, 미해결 사건, 활성 규칙
- 현재 branch, HEAD SHA, 빌드 식별자

## 절차

1. **저장소 판독**
   - 저장소 지침, 현재 branch와 변경 파일, 최신 handoff를 읽는다.
   - `.game-wiki`가 있으면 `17-game-dev-memory`의 `PREFLIGHT`를 수행한다.
2. **요청 분류**
   - `DISCOVER`: 아이디어 후보가 필요함 → `01`
   - `FOUNDATION`: 핵심 결정이 미정 또는 충돌함 → `02`, `03`
   - `PROVE`: 재미·기술 가정을 검증해야 함 → `04`
   - `SPECIFY`: GDD·시스템 계약·기술 계획이 필요함 → `05`
   - `CHANGE`: 기능 제작·수정 → `06`, 필요 시 `07`
   - `SPECIALIST`: UI `08`, 아트 `09`, 자산 `10`, 밸런스 `11`
   - `IMPLEMENT`: 승인된 계약 구현 → `12`
   - `DEBUG`: 재현 가능한 오류 → `13`
   - `VALIDATE`: 콘텐츠·저장·데이터 → `14`
   - `VERIFY`: 완료 증거 → `15`
   - `PLAYTEST`: 실제 플레이 판단 → `16`
   - `MEMORY`: 결정·사건·handoff → `17`
   - `SHIP`: 성능·패키징·출시 → `18`
3. **최소 경로 선택**
   - 관련 없는 스킬을 모두 실행하지 않는다.
   - 아직 결정되지 않은 상위 계약을 하위 구현 스킬로 메우지 않는다.
4. **Route Packet 작성**
   - 사실, 가정, 누락, 선택한 순서, 생략한 단계와 이유를 기록한다.
5. **실행**
   - 선택한 스킬을 번호 순서로 호출한다.

## 하드 게이트

- 승인된 Game Contract 또는 명시적 `throwaway prototype` 선언 없이 제품 코드를 시작하지 않는다.
- Work Order 없이 중·고위험 파일 변경을 시작하지 않는다.
- `15-game-verification-gate` 없이 완료를 주장하지 않는다.
- 사용자 피드백, 실패, 범위 이탈, 중요한 결정이 생기면 `17-game-dev-memory`를 누락하지 않는다.
- 저장소에 미커밋 변경이 있으면 관련성과 소유권을 확인하기 전 덮어쓰거나 삭제하지 않는다.

## 산출물

```yaml
route_packet:
  request_summary: ""
  repository_state:
    branch: ""
    head_sha: ""
    dirty_paths: []
  known_facts: []
  assumptions: []
  selected_sequence: ["00", "06", "07", "12", "15", "17"]
  skipped_stages:
    - stage: "04"
      reason: "핵심 가정이 이미 E3 증거로 검증됨"
  blocking_contracts: []
  expected_outputs: []
```

## 완료 게이트

- 현재 요청이 정확히 한 주 경로와 필요한 조건부 경로로 분류됐다.
- 선택한 모든 단계의 입력이 존재하거나 가정으로 명시됐다.
- 생략한 필수 단계가 없다.
- 다음 스킬과 첫 산출물이 명확하다.
