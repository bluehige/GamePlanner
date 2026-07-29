---
name: skill-quality-auditor
description: Audit GamePlanner and project-specific skills for trigger precision, workflow completeness, evidence gates, reference integrity, external-source policy, and adversarial failure cases.
---

# Skill Quality Auditor

스킬을 설명문이 아니라 **Agent 행동을 통제하는 실행 규칙**으로 검수한다. 발동 조건, 중단 조건, 산출물, 검증, 실패 사례가 실제로 작동하는지 확인한다.

## 사용 시점

- GamePlanner 스킬을 추가·수정·번호 변경할 때
- 외부 스킬 버전을 갱신할 때
- 프로젝트 전용 스킬을 생성했을 때
- Agent가 규칙을 우회하거나 과도하게 발동했을 때

## 입력

- 대상 `SKILL.md`와 references, schemas, scripts, tests
- 저장소 AGENTS.md와 우선순위 규칙
- 외부 버전 lock과 라이선스 고지
- 정상·경계·실패·규칙 우회 테스트 사례
- 최근 실제 사용 사건

## 절차

1. frontmatter의 이름과 설명이 발동 범위를 정확히 표현하는지 검사한다.
2. 다른 스킬과 발동 조건이 겹칠 때 우선순위가 있는지 검사한다.
3. 사용 시점과 사용하지 말아야 할 조건을 검토한다.
4. 입력, 절차, 하드 게이트, 산출물, 완료 게이트가 연결되는지 검사한다.
5. 사용자가 제공하지 않은 결정을 Agent가 임의로 확정하게 만드는 규칙을 찾는다.
6. 검증 없이 완료를 선언할 수 있는 빈틈을 찾는다.
7. 로컬 링크, 스키마, 스크립트, 외부 ref와 라이선스를 검사한다.
8. 범용 원칙이 프로젝트별 스킬에 불필요하게 복제됐는지 검사한다.
9. 최소 정상 사례, 누락 입력, 모순 요청, 범위 확장 유도, 거짓 완료 주장 사례를 시험한다.
10. `python scripts/validate_repository.py`와 전체 단위 테스트를 실행한다.
11. 발견 항목을 차단·중요·개선으로 분류한다.

## 감사 기준

- `Trigger`: 필요한 요청에만 발동하는가
- `Boundary`: 담당하지 않는 영역이 명확한가
- `Procedure`: Agent가 순서대로 실행할 수 있는가
- `Gate`: 합리화로 건너뛸 수 없는가
- `Artifact`: 결과가 재사용 가능한 형식인가
- `Evidence`: 완료 주장을 검증하는가
- `Integration`: 전후 단계와 입력·출력이 연결되는가
- `Maintainability`: 상세 자료를 필요할 때만 읽는가
- `Provenance`: 외부 출처와 라이선스가 추적되는가
- `Tests`: 실패와 우회 시나리오가 있는가

## 하드 게이트

- 링크가 깨진 스킬을 배포하지 않는다.
- 외부 원문을 라이선스와 고지 없이 복제하지 않는다.
- “상황에 맞게 잘 판단한다”만으로 핵심 절차를 대체하지 않는다.
- 자동 검증이 없는 구조화 산출물을 안정적이라고 선언하지 않는다.
- 프로젝트별 예외를 범용 코어에 즉시 일반화하지 않는다.
- 테스트가 현재 스킬 내용을 실제로 읽지 않으면 검수로 인정하지 않는다.

## 산출물

```text
docs/game-planner/skill-audits/<date>/
├── INVENTORY.md
├── FINDINGS.md
├── TEST_RESULTS.md
├── EXTERNAL_PROVENANCE.md
└── VERDICT.md
```

## 완료 게이트

- 모든 번호 스킬이 목록과 실제 파일에서 일치한다.
- 필수 섹션과 참조가 존재한다.
- 외부 버전·라이선스 정책이 유효하다.
- 정상·실패·우회 테스트가 통과한다.
- 차단 항목 0건이며 남은 제한이 문서화됐다.
