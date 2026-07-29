---
name: game-dev-memory
description: Maintain an evidence-linked LLM Wiki of game-development decisions, incidents, corrections, experiments, playtests, verification, releases, and handoffs so failures are not repeated.
---

# Game Development Memory

대화 내용을 무작정 축적하지 않는다. 변경하지 않는 원문, 지속 편집되는 구조화 Wiki, 문서 규칙을 정의하는 스키마를 분리해 **프로젝트가 스스로 학습하는 기록 체계**를 유지한다.

## 사용 시점

- 모든 작업 세션 시작과 종료
- 사용자 피드백, 결정 변경, 버그, 회귀, 실패한 접근이 발생했을 때
- 플레이테스트·검증·릴리스 결과가 나왔을 때
- 다음 Agent나 사람이 작업을 인수할 때

## 입력

- 사용자 원문 또는 원문 참조
- Work Order, 변경 diff, branch, SHA, 빌드
- 재현·근본 원인·수정·검증 증거
- 결정의 대안과 트레이드오프
- 플레이테스트·릴리스 결과
- 기존 Wiki의 관련 사건과 활성 규칙

## 모드

- `PREFLIGHT`: 현재 작업과 관련된 상태·결정·사건·규칙만 조회
- `RECORD`: 결정, 변경, 실험, 검증, 플레이테스트, 릴리스 기록
- `INCIDENT`: 문제 사건을 생성하고 단계별로 갱신
- `HANDOFF`: 다음 세션이 안전하게 이어갈 현재 상태 작성
- `LINT`: 중복, 모순, 오래된 규칙, 깨진 참조 검사

## 기본 구조

```text
.game-wiki/
├── SCHEMA.md
├── index.md
├── log.md
├── current-state.md
├── raw/
│   ├── sessions/
│   ├── tool-logs/
│   ├── screenshots/
│   └── playtest-notes/
├── project/
│   ├── overview.md
│   ├── architecture.md
│   ├── glossary.md
│   └── systems/
├── decisions/
├── incidents/
├── rules/
├── experiments/
├── playtests/
├── verifications/
├── releases/
├── handoffs/
└── _archive/
```

## 기록 유형

- `DECISION`: 되돌리기 어렵고 실제 트레이드오프가 있는 선택
- `CHANGE`: 플레이 경험 또는 시스템 계약 변경
- `INCIDENT`: 기대와 다른 결과가 발생한 사건
- `CORRECTION`: 사용자가 Agent 해석을 바로잡은 사건
- `EXPERIMENT`: 가설을 검증한 프로토타입·밸런스 실험
- `PLAYTEST`: 실제 사용자 관찰과 결정
- `VERIFICATION`: 완료 주장에 사용한 증거
- `RELEASE`: 배포 가능한 기준점과 알려진 문제

## 사건 생명주기

```text
draft
→ reproduced
→ root-caused
→ fixed
→ verified
→ rule-candidate
→ active-rule | closed | superseded
```

한 번의 사용자 수정 지시를 즉시 영구 규칙으로 만들지 않는다. 재현, 원인, 수정, 검증을 거쳐 같은 유형의 실패를 실제로 예방할 수 있을 때만 규칙으로 승격한다.

## 절차

1. `PREFLIGHT`에서는 전체 Wiki를 읽지 않고 시스템 태그, 파일 경로, 기능 ID로 관련 문서만 찾는다.
2. 원문과 로그는 `raw/`에 수정하지 않는 참조로 보존한다.
3. Wiki 문서는 사실, 해석, 결정, 미확인을 구분한다.
4. 모순은 오래된 내용을 삭제해 숨기지 않고 날짜·출처·대체 관계를 적는다.
5. 중요한 사건은 사용자 요청 → Agent 해석 → 기대 → 관찰 → 재현 → 원인 → 수정 → 검증 → 예방 순서로 작성한다.
6. Git에는 무엇이 바뀌었는지, Wiki에는 왜 바뀌었고 무엇을 반복하면 안 되는지 기록한다.
7. `index.md`는 현재 유효한 문서를, `log.md`는 시간순 중요 사건을 가리킨다.
8. 세션 종료마다 `current-state.md`와 handoff를 갱신한다.
9. `scripts/wiki_lint.py`를 실행한다.
10. 오래된 규칙은 증거와 현재 계약을 비교해 `superseded` 또는 `_archive`로 이동한다.

## 개인정보·보안

- 비밀번호, 토큰, 개인식별정보, 비공개 고객 자료를 Wiki에 복사하지 않는다.
- 필요한 경우 원문 위치와 비식별 요약만 기록한다.
- 공개 저장소에 편입하기 전 원문·스크린샷·로그의 공개 가능성을 확인한다.

## 하드 게이트

- 원문과 Agent 해석을 같은 문장으로 합치지 않는다.
- 근본 원인 없는 사건을 `active-rule`로 승격하지 않는다.
- 검증하지 않은 수정을 성공 사례로 기록하지 않는다.
- 모든 커밋을 Wiki에 중복 기록하지 않는다.
- 현재 작업과 무관한 전체 기억을 매번 컨텍스트에 넣지 않는다.
- 모순되는 기록을 조용히 삭제하지 않는다.

## 산출물

주요 템플릿은 다음을 사용한다.

- `templates/INCIDENT.template.md`
- `templates/HANDOFF.template.md`
- `templates/WIKI_SCHEMA.template.md`

## 완료 게이트

- 다음 작업자가 현재 목표, 기준 SHA, 완료·미완료, 금지 변경을 알 수 있다.
- 중요한 결정과 사건이 증거에 연결된다.
- 활성 규칙이 원인과 검증을 가진다.
- 중복 ID와 필수 섹션 누락이 없다.
- Wiki lint가 통과한다.
