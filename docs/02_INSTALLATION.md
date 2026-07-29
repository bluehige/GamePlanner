# 02. 설치

## 전체 설치

```bash
git clone https://github.com/bluehige/GamePlanner.git
```

Agent가 저장소의 `skills/`를 직접 읽을 수 없는 환경에서는 필요한 폴더를 전역 Skill 경로나 프로젝트 `.agents/skills/`에 연결한다.

## 최소 설치

새 게임의 초기 기획만 진행한다면 다음 스킬부터 시작한다.

```text
00-game-production-router
02-game-foundation-director
03-game-foundation-project-builder
04-game-prototype-gate
05-game-design-spec
17-game-dev-memory
```

## 외부 스킬

외부 프로젝트는 자동 설치하지 않는다. `external/UPSTREAMS.lock.json`에 기록된 ref를 검토한 뒤 각 원본의 설치 절차를 따른다. 설치하지 않아도 GamePlanner 내부 기본 절차는 작동하지만, 전문 기능의 깊이는 낮아질 수 있다.

## 선택형 외부 설치

외부 스킬 목록과 고정 SHA를 확인하려면 `python scripts/install_upstreams.py --list`를 실행한다. 선택 설치는 [06. 외부 스킬 설치](06_EXTERNAL_INSTALLATION.md)를 따른다.
