---
name: game-design-spec
description: Turn an approved game foundation and prototype evidence into a traceable GDD, system contracts, technical plan, and executable production tasks.
---

# Game Design Spec

게임의 핵심 판타지와 기둥을 실제 시스템, 데이터, UX, 콘텐츠, 테스트로 추적 가능한 제작 명세로 변환한다.

## 사용 시점

- Foundation 계약과 핵심 프로토타입 판정이 준비됐을 때
- 기존 GDD가 설명문 위주이고 구현 경계와 검증법이 없을 때
- 대규모 업데이트를 기능 묶음과 시스템 계약으로 나눌 때

## 입력

- `GAME_CONTRACT.md`, `CONTEXT.md`, `RISK_REGISTER.md`
- 프로토타입 결과
- 엔진·플랫폼·기술 제약
- 기존 코드·데이터 구조
- UI·아트·밸런스 요구
- 출시 범위와 프로토타입 범위

## 외부 연동

- `github/spec-kit`: 원칙 → 명세 → 계획 → 작업 → 일관성 분석의 추적 구조
- `BMad Game Dev Studio`: 게임 브리프, GDD, 기술 아키텍처, 플레이테스트, 제작 계획의 누락 검사

외부 워크플로를 그대로 복제하지 않고 GamePlanner 계약에 맞는 섹션과 추적표만 사용한다.

## 절차

1. **모드 선택**
   - `QUICK`: 작은 프로토타입·짧은 데모
   - `FULL`: 출시 제품·장기 업데이트
2. **추적 사슬 생성**
   - `Pillar → Player Loop → Mechanic → System Contract → Data → UI/Feedback → Test`
3. **시스템 계약 작성**
   - 입력, 상태, 규칙, 출력, 실패, 저장, 이벤트, 성능 예산을 정의한다.
4. **콘텐츠 모델 작성**
   - ID, 스키마, 참조, 생성 비용, 변형 방식, 현지화 경계를 정의한다.
5. **기술 계획 작성**
   - 엔진 씬·컴포넌트 경계, 데이터 권위, 저장, 툴, 테스트, 빌드 구조를 정한다.
6. **생산 범위 분리**
   - 프로토타입, 첫 플레이 가능 빌드, 출시 최소 범위, 출시 후 범위를 분리한다.
7. **작업 분해**
   - 사용자 가치와 검증 가능한 수직 조각으로 나누며, 단순 파일 목록이 되지 않게 한다.
8. **일관성 감사**
   - 기둥에 연결되지 않은 기능, 테스트 없는 계약, UI 없는 상태, 저장 누락을 찾는다.

## 필수 문서 영역

- 플레이어 경험과 핵심 루프
- 게임 상태와 진행 구조
- 전투·경제·성장·AI·레벨 규칙
- 콘텐츠 타입과 데이터 모델
- UI, 입력, 접근성
- 아트, 애니메이션, VFX, 오디오
- 저장, 버전 마이그레이션, 결정성
- 현지화와 텍스트 길이
- 성능·메모리·로딩 예산
- 테스트, 계측, 플레이테스트
- 출시와 업데이트 경계

## 하드 게이트

- “적당히”, “다양하게”, “밸런스를 맞춘다”를 수치·상태·검증법 없이 남기지 않는다.
- 플레이어 경험에 연결되지 않는 기술 시스템을 우선 제작하지 않는다.
- 모든 기능을 한 번에 출시 범위로 넣지 않는다.
- 코드 구조를 확정하지 않은 디자인 문서가 구현 세부를 거짓으로 단정하지 않게 한다.
- 기존 저장과 콘텐츠를 깨뜨리는 변경은 마이그레이션 계약 없이 승인하지 않는다.

## 산출물

```text
docs/foundation/GAME_DESIGN_SPEC.md
docs/game-planner/spec/
├── SYSTEM_CONTRACTS.md
├── CONTENT_MODEL.md
├── TECHNICAL_PLAN.md
├── PRODUCTION_SCOPE.md
├── TRACEABILITY.md
└── IMPLEMENTATION_BACKLOG.md
```

## 완료 게이트

- 모든 출시 기능이 최소 하나의 게임 기둥에 연결된다.
- 모든 시스템 계약에 입력, 상태, 출력, 실패, 검증이 있다.
- 프로토타입과 출시 코드의 경계가 명확하다.
- 첫 구현 묶음이 독립적으로 플레이·검증 가능한 수직 조각이다.
- 문서 간 모순과 미결정 사항이 별도 목록으로 남았다.
