# 06. 외부 스킬 설치

GamePlanner는 외부 저장소를 내부에 복제하지 않는다. 필요한 프로젝트만 `external/UPSTREAMS.lock.json`에 고정된 commit으로 별도 설치한다.

## 목록 확인

```bash
python scripts/install_upstreams.py --list
```

## 단계 또는 프로젝트 선택 설치

```bash
# UI/UX 단계만 설치
python scripts/install_upstreams.py --stage 08

# 구현 워크플로와 엔진 지식 팩 설치
python scripts/install_upstreams.py --id superpowers \
  --id awesome-gamedev-agent-skills

# 설치 명령만 확인
python scripts/install_upstreams.py --stage 10 --dry-run
```

기본 설치 위치는 `.game-planner/upstreams/`다. 저장소마다 로딩 방식이 다르므로 설치 뒤 각 upstream의 공식 설치 문서를 따른다. `--all`은 다운로드 규모와 실행 환경이 서로 다른 저장소를 모두 받으므로 기본 권장값이 아니다.

## 갱신

```bash
python scripts/install_upstreams.py --id superpowers --update
```

lock 파일의 SHA를 먼저 변경하지 않는다. 새 upstream 변경 내역과 라이선스, 스킬 경로, 쓰기 범위를 검토한 뒤 `90-skill-quality-auditor`를 실행하고 SHA를 갱신한다.

## 설치하지 않는 항목

명시적 라이선스가 없는 개념 참고 자료와 `concept-only` 항목은 설치 스크립트가 제외한다. GamePlanner 내부 문서는 해당 아이디어를 독립적으로 재구성하며 원문을 번들하지 않는다.
