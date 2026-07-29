---
name: game-prototype-gate
description: Design the cheapest credible prototype for one risky gameplay or technical assumption and produce a keep, redesign, or kill verdict.
---

# Game Prototype Gate

프로토타입의 목적을 “게임 일부를 먼저 제작”이 아니라 **가장 위험한 가정 하나를 저비용으로 판정**하는 것으로 제한한다.

## 사용 시점

- 핵심 재미가 문서만으로 판단되지 않을 때
- 로컬 LLM, 물리, 네트워크, AI, 절차 생성 등 기술 위험이 클 때
- 콘텐츠를 대량 제작하기 전 반복 루프를 확인해야 할 때
- 두 설계안 중 실제 반응으로 선택해야 할 때

## 입력

- `docs/foundation/PROTOTYPE_BRIEF.md`
- 검증할 단일 가설
- 대상 플레이어 또는 기술 환경
- 허용하는 임시 자산·코드 수준
- 유지, 재설계, 폐기 기준

## 절차

1. **질문 하나로 축소**
   - “게임이 재미있는가”가 아니라 관찰 가능한 질문으로 바꾼다.
2. **증거 수준 선택**
   - 기술 가정은 자동 로그와 반복 실행, 재미 가정은 실제 입력과 플레이 관찰이 필요하다.
3. **최소 프로토타입 설계**
   - 질문과 무관한 메타게임, 저장, 최종 UI, 콘텐츠 다양성을 제거한다.
4. **코드 운명 결정**
   - `throwaway`: 폐기 전제
   - `evolutionary`: 제품 코드 승격 가능, 테스트와 구조 요구
5. **계측 추가**
   - 성공률, 완료 시간, 선택 분포, 실패 원인, 성능 지표를 기록한다.
6. **실행과 판정**
   - 사전에 정한 임계치로 `KEEP`, `REDESIGN`, `KILL`, `INCONCLUSIVE`를 판정한다.
7. **후속 계약 갱신**
   - 결과가 Game Contract나 Risk Register를 바꾸면 `02`와 `17`에 전달한다.

## 하드 게이트

- 한 프로토타입에 독립 가설을 여러 개 넣지 않는다.
- 임시 자산의 시각 완성도로 핵심 루프의 재미를 대신 판단하지 않는다.
- 프로토타입 코드를 검토 없이 제품 코드로 승격하지 않는다.
- 결과를 보고 임계치를 사후 변경해 성공으로 만들지 않는다.
- 실패한 가정을 “조금 더 만들면 좋아질 것”이라는 근거 없는 이유로 유지하지 않는다.

## 산출물

```text
docs/game-planner/experiments/EXP-<id>-PROTOTYPE.md
evidence/prototypes/<id>/
```

문서에는 다음을 포함한다.

```yaml
hypothesis: ""
observable_behavior: ""
excluded_features: []
prototype_fate: throwaway
metrics: []
keep_if: []
redesign_if: []
kill_if: []
result: INCONCLUSIVE
raw_evidence: []
next_decision: ""
```

## 완료 게이트

- 한 문장 가설과 반증 가능한 기준이 있다.
- 질문과 무관한 제작이 제거됐다.
- 원시 증거가 보존됐다.
- 판정이 사전 기준에 연결됐다.
- 다음 단계가 `05`, 재프로토타입, 또는 중단 중 하나로 명확하다.
