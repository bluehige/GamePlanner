# 03. 프로젝트 초기화

`bootstrap_project.py`는 기존 게임 프로젝트를 삭제하지 않고, 존재하지 않는 GamePlanner 기본 파일만 생성한다.

```text
.game-planner/config.json
.game-wiki/SCHEMA.md
.game-wiki/index.md
.game-wiki/log.md
.game-wiki/current-state.md
.game-wiki/raw/
.game-wiki/project/
.game-wiki/decisions/
.game-wiki/incidents/
.game-wiki/rules/
.game-wiki/experiments/
.game-wiki/playtests/
.game-wiki/verifications/
.game-wiki/releases/
.game-wiki/handoffs/
docs/foundation/GAME_CONTRACT.md
docs/foundation/CONTEXT.md
docs/foundation/DECISION_LOG.md
docs/foundation/RISK_REGISTER.md
docs/foundation/PROTOTYPE_BRIEF.md
docs/foundation/GAME_DESIGN_SPEC.md
docs/game-planner/<production-output-folders>/
.agents/skills/<slug>-foundation/SKILL.md
```

## 실행

```bash
python scripts/bootstrap_project.py ../MyGame \
  --slug my-game \
  --title "My Game" \
  --engine "Godot 4.5" \
  --platform Windows \
  --platform Linux \
  --genre "Strategy Simulation"
```

이미 존재하는 파일은 기본적으로 **건너뛰며 덮어쓰지 않는다**. 출력에 skipped 목록이 표시된다. `--force`는 GamePlanner가 관리하는 동일 경로를 교체하므로, 사용 전에 Git 상태와 diff를 확인한다.

초기화 후 가장 먼저 `docs/foundation/GAME_CONTRACT.md`를 완성하고 `02-game-foundation-director`의 완료 게이트를 통과한다.
