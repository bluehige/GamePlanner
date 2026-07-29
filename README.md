# GamePlanner

AI와 함께 게임을 만들 때 필요한 **기획 전 검증, 작업 계약, 변경 영향 분석, 제작, 검수, 플레이테스트, 장기 기억, 출시 판단**을 하나의 순서로 묶은 게임 제작 Agent Skill 스택입니다.

이 저장소의 번호는 폴더 정렬용이 아니라 **게임 제작 생명주기의 기본 순서**입니다. 모든 단계를 매번 실행하는 것은 아니며, `00-game-production-router`가 현재 작업에 필요한 최소 스킬만 선택합니다. `17-game-dev-memory`처럼 세션 전후에 재진입하는 교차 단계는 번호 위치와 별개로 필요한 시점에 삽입됩니다.

## 기본 제작 흐름

```text
00 요청·저장소 상태 판독
01 아이디어 후보 포트폴리오 생성                선택
02 핵심 기획 질답과 게임 계약 확정              필수
03 게임별 전용 기획 스킬 생성                   프로젝트당 1회
04 가장 위험한 가정의 프로토타입 검증           조건부 필수
05 GDD·시스템 계약·기술 계획 작성               필수
06 개별 작업을 Work Order로 정규화              작업마다
07 변경 영향과 회귀 범위 분석                   중·고위험 변경마다
08 게임 UI·UX 설계                              해당 작업
09 아트 디렉션 확정                              아트 제작 전
10 그래픽·3D·VFX·애니메이션 자산 제작           해당 작업
11 전투·경제·성장 밸런스 실험                   해당 작업
12 엔진 구현                                     승인된 작업만
13 체계적 디버깅                                 오류 발생 시
14 콘텐츠·데이터·저장 호환 검증                 관련 변경 시
15 완료 주장 전 증거 검증                       모든 완료 전
16 플레이테스트 실험                            마일스톤마다
17 결정·사건·피드백·교훈을 LLM Wiki에 편입      세션 전후·사건 발생 시
18 성능·패키징·출시 준비 판단                   출시 후보 빌드
90 스킬 저장소 자체 품질 감사                   스킬 변경 시
```

상세 순서는 [`docs/00_USAGE_SEQUENCE.md`](docs/00_USAGE_SEQUENCE.md), 전체 카탈로그는 [`CATALOG.md`](CATALOG.md)를 참고합니다.

## 핵심 원칙

1. 아이디어를 바로 코드로 바꾸지 않는다. 먼저 플레이 경험과 위험 가정을 고정한다.
2. 사용자의 자연어 명령을 그대로 실행하지 않는다. 목표·범위·비범위·수용 기준·검증법을 작업 계약으로 정규화한다.
3. UI 변경, 아트 교체, 밸런스 수정에 다른 시스템 변경을 몰래 포함하지 않는다.
4. 버그 수정은 재현과 근본 원인 확인 뒤에 수행한다.
5. 테스트 통과, 빌드 성공, 실제 플레이 성공은 서로 다른 증거다.
6. 같은 실수를 반복하지 않도록 사건을 원문·해석·근본 원인·검증·예방 규칙으로 남긴다.
7. 외부 스킬은 원문을 복제하지 않고 버전 고정된 어댑터로 연결한다.

## 설치

Codex 또는 호환 Agent Skill 환경에서 이 저장소를 설치하거나, 필요한 스킬 폴더만 프로젝트의 `.agents/skills/` 아래에 배치합니다.

```bash
git clone https://github.com/bluehige/GamePlanner.git
cd GamePlanner
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

새 게임 프로젝트에 기본 문서와 게임 전용 기획 스킬을 생성하려면 다음을 실행합니다.

```bash
python scripts/bootstrap_project.py ../MyGame \
  --slug my-game \
  --engine "Godot 4.5" \
  --platform "Windows" \
  --genre "Strategy Simulation"
```

## 외부 스킬 연동

이 저장소는 아래 시스템을 **어댑터 방식**으로 연결합니다.

- `bluehige/idea-diversity-engine`
- `mattpocock/skills`의 `grill-me`, `grilling`, `domain-modeling`, `wayfinder`
- `github/spec-kit`
- `bmad-code-org/bmad-module-game-dev-studio`
- `bluehige/UI_UX_Skill_for_Game`
- `jay6697117/agent-sprite-forge-codex-skill`
- `bluehige/blender_exprorter_for_Engine`
- `obra/superpowers`
- `gamedev-skills/awesome-gamedev-agent-skills`
- Andrej Karpathy의 `LLM Wiki` 아이디어 파일

고정 버전과 라이선스는 [`external/UPSTREAMS.lock.json`](external/UPSTREAMS.lock.json), 포함 정책은 [`docs/04_EXTERNAL_SKILLS_POLICY.md`](docs/04_EXTERNAL_SKILLS_POLICY.md)에 기록합니다. 선택 설치 방법은 [`docs/06_EXTERNAL_INSTALLATION.md`](docs/06_EXTERNAL_INSTALLATION.md)를 참고합니다.

```bash
python scripts/install_upstreams.py --list
python scripts/install_upstreams.py --stage 08 --dry-run
```

## 저장소 구조

```text
skills/       실제 사용 순서로 번호가 붙은 Agent Skills
templates/    게임 계약, 작업 계약, 사건, 플레이테스트, 출시 증거 템플릿
schemas/      자동 검증용 JSON Schema
scripts/      프로젝트 초기화와 저장소·위키·작업 계약 검증기
external/     외부 스킬 버전 고정 정보와 연결 정책
docs/         운용 규칙과 아키텍처
examples/     최소 예제
tests/        표준 라이브러리 기반 검증 테스트
```

## 검증

외부 패키지 없이 Python 3.10 이상에서 실행됩니다.

```bash
python scripts/validate_repository.py
python scripts/validate_work_order.py examples/tactical-dungeon/work-order.json
python scripts/wiki_lint.py examples/tactical-dungeon/.game-wiki
python scripts/install_upstreams.py --list
python -m unittest discover -s tests -v
```

## 라이선스

GamePlanner가 직접 작성한 코드와 문서는 MIT License입니다. 외부 프로젝트는 각 원본 라이선스를 따르며 이 저장소에 원문을 번들하지 않습니다. 자세한 내용은 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)를 참고합니다.
