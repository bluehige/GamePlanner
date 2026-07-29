# External Skill Integrations

이 디렉터리는 외부 프로젝트의 복사본이 아니다. GamePlanner가 어느 단계에서 어떤 원본을 연결하는지와 검토한 commit SHA를 기록한다.

## 사용 방식

1. `UPSTREAMS.lock.json`에서 대상 upstream과 ref를 확인한다.
2. 원본 저장소의 설치 문서를 따라 별도로 설치한다.
3. GamePlanner의 해당 번호 어댑터가 요구하는 입력 계약을 먼저 충족한다.
4. upstream 결과를 GamePlanner 산출물 형식으로 정규화한다.
5. 프로젝트 계약과 충돌하면 프로젝트 계약을 우선한다.

## 갱신

`main` 또는 `HEAD`를 그대로 추적하지 않는다. 새 commit으로 바꿀 때는 다음을 확인한다.

- 라이선스 변경
- 스킬 이름·경로 변경
- 출력 형식 변경
- 자동 실행 또는 파일 쓰기 범위 변경
- GamePlanner 하드 게이트를 우회하는 동작 추가 여부

Karpathy의 Gist는 명시적 라이선스가 없으므로 개념만 참고하며 원문을 번들하지 않는다.
