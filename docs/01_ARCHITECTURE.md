# 01. 아키텍처

GamePlanner는 세 계층을 분리한다.

```text
권위 계층
  GamePlanner 내부 스킬과 프로젝트별 계약

전문 지식 계층
  UI, 엔진, 장르, 아트 도구 등의 외부 스킬

증거·기억 계층
  Work Order, 변경 영향, 테스트, 사건 Wiki, 출시 근거
```

## 권위 순서

```text
저장소 AGENTS.md
> 프로젝트 Game Contract
> 프로젝트 전용 Foundation Skill
> 기능 Work Order
> 활성 전문 스킬
> 범용 외부 스킬
```

외부 스킬은 엔진 API나 세부 방법을 제공하지만, 프로젝트 범위와 완료 기준을 바꾸지 못한다.

## 상태 저장

- 현재 제작 상태: `.game-planner/config.json`
- 승인된 기획: `docs/foundation/`
- 제작 단계 산출물: `docs/game-planner/`
- 장기 기억: `.game-wiki/`
- 프로젝트 전용 스킬: `.agents/skills/<slug>-foundation/`
- 코드·자산 변경 이력: Git

Git은 무엇이 바뀌었는지를 저장하고, Wiki는 왜 바뀌었으며 무엇을 다시 하면 안 되는지를 저장한다.
