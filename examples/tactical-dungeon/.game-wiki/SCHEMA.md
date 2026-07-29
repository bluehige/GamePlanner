# Game Wiki Schema

## Layers

1. `raw/`: 원문·로그·캡처. 수정하지 않고 참조한다.
2. 구조화 Wiki: 결정·사건·실험·검증·릴리스. 지속적으로 갱신한다.
3. 이 스키마: 문서 유형, 상태, 필수 필드, 승격 규칙을 정의한다.

## Required roots

- `index.md`
- `log.md`
- `current-state.md`
- `raw/`
- `project/`
- `decisions/`
- `incidents/`
- `rules/`
- `experiments/`
- `playtests/`
- `verifications/`
- `releases/`
- `handoffs/`
- `_archive/`

## Incident states

`draft → reproduced → root-caused → fixed → verified → rule-candidate → active-rule | closed | superseded`

## Source policy

- 사실에는 출처 또는 증거를 연결한다.
- 추론과 미확인은 명시한다.
- 모순은 삭제하지 않고 supersedes 관계를 기록한다.
- 비밀·개인정보·비공개 자료는 원문 복사를 금지한다.

## Rule promotion

규칙은 재현된 사건, 근본 원인, 검증된 수정, 재발 방지 가능성을 모두 가져야 `active-rule`이 될 수 있다.
