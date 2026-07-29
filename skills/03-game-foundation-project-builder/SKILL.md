---
name: game-foundation-project-builder
description: Convert an approved generic game foundation into a repository-specific skill and durable project contracts without duplicating global rules.
---

# Game Foundation Project Builder

승인된 게임 계약을 현재 저장소에서 매 세션 자동으로 읽히는 **게임별 전용 Foundation Skill**로 변환한다.

## 사용 시점

- `02-game-foundation-director`의 계약이 승인된 직후
- 기존 게임 저장소에 GamePlanner를 처음 적용할 때
- 핵심 방향 전환으로 프로젝트 계약이 변경됐을 때

## 입력

- `GAME_CONTRACT.md`, `CONTEXT.md`, `RISK_REGISTER.md`, `OUT_OF_SCOPE.md`
- 엔진, 플랫폼, 장르, 입력 방식
- 저장소 구조와 source-of-truth 경로
- 반드시 유지할 기존 기능과 `do_not_touch` 경계
- 테스트·빌드·실행 명령

## 절차

1. **프로젝트 탐색**
   - 실제 디렉터리, 데이터 원본, 엔트리 씬, 테스트 명령을 확인한다.
2. **계약 압축**
   - 범용 GamePlanner 규칙을 복제하지 않고 이 게임에만 해당하는 사실과 제한을 추린다.
3. **전용 Skill 생성**
   - `.agents/skills/<slug>-foundation/SKILL.md`를 만든다.
4. **설정 생성**
   - `.game-planner/config.json`에 게임 식별자, 엔진, 문서 경로, 검증 명령을 기록한다.
5. **우선순위 명시**
   - 저장소 지침 > 게임 계약 > 전용 Skill > 활성 전문 스킬 > 범용 외부 스킬 순서를 적는다.
6. **검증**
   - 모든 경로가 존재하거나 생성 예정으로 표시됐는지 검사한다.

## 전용 Skill 필수 내용

- 한 문장 게임 정의
- 핵심 기둥과 금지 구조
- 변경하면 안 되는 source-of-truth
- 시스템별 권위 파일
- 엔진·플랫폼 제한
- 필수 검증 명령
- 최신 handoff와 Wiki 위치
- 완료 선언 규칙

## 하드 게이트

- GamePlanner 범용 절차를 게임별 Skill에 복사해 두 버전의 규칙을 만들지 않는다.
- 존재하지 않는 파일 경로를 사실처럼 기록하지 않는다.
- 현재 코드와 계약이 충돌하면 자동으로 한쪽을 정답 처리하지 않고 충돌 목록을 만든다.
- 비공개 토큰, 개인 경로, 로컬 비밀 값을 생성 파일에 넣지 않는다.

## 산출물

```text
.game-planner/config.json
.agents/skills/<game-slug>-foundation/SKILL.md
docs/game-planner/PROJECT_SOURCE_MAP.md
docs/game-planner/CONTRACT_CONFLICTS.md
```

## 완료 게이트

- 새 세션이 전용 Skill만 읽어도 게임의 목표와 금지 범위를 설명할 수 있다.
- 핵심 데이터와 코드의 source-of-truth 경로가 확인됐다.
- 빌드·테스트·실행 명령이 실제 저장소 기준으로 기록됐다.
- 범용 규칙의 중복 복제가 없다.
- 충돌이 없거나 충돌이 명시적으로 `open` 상태다.
