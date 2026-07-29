---
name: performance-release-gate
description: Validate target-hardware performance, packaging, installation, save/update compatibility, platform requirements, rollback, and release evidence before shipping a game build.
---

# Performance and Release Gate

릴리스 후보를 개발 PC에서 실행되는 빌드가 아니라 **대상 환경에서 설치·실행·업데이트·복구 가능한 제품**으로 검증한다.

## 사용 시점

- 수직 슬라이스, 데모, 외부 테스트, 스토어 출시 후보
- 엔진·렌더러·대형 자산·저장 구조 변경 후
- 플랫폼별 패키지와 패치를 배포하기 전

## 입력

- 고정된 release candidate 빌드 ID, branch, SHA
- 최소·권장 사양과 대상 플랫폼
- 프레임·메모리·로딩·패키지 크기 예산
- 이전 공개 빌드와 저장 샘플
- 설치·업데이트·제거·롤백 절차
- 스토어·플랫폼 체크리스트
- 알려진 문제와 허용 근거

## 절차

1. 대상 장면, 세이브, 플레이 구간, 하드웨어 매트릭스를 고정한다.
2. 콜드 스타트, 첫 로드, 반복 로드, 최악 구간을 측정한다.
3. 평균 FPS뿐 아니라 프레임타임 분포와 스파이크를 확인한다.
4. CPU, GPU, 메모리, VRAM, 드로우콜, 로딩, 저장 시간을 프로파일한다.
5. 장시간 플레이에서 누수와 누적 저하를 확인한다.
6. 깨끗한 환경에 설치하고 최초 실행을 검증한다.
7. 이전 버전에서 업데이트하고 저장 호환을 검증한다.
8. 네트워크 단절, 디스크 부족, 권한 문제, 중단된 업데이트를 점검한다.
9. 제거·재설치·롤백 정책을 검증한다.
10. 플랫폼 요구사항, 라이선스, 크레딧, 개인정보, 접근성 문서를 확인한다.
11. 최종 패키지 해시와 증거 인덱스를 작성한다.
12. READY, CONDITIONAL, BLOCK 중 하나로 판정한다.

## 최소 성능 증거

- 평균, 중앙값, P95·P99 프레임타임
- 최저 구간과 스파이크 원인
- 시스템 메모리와 VRAM 최고치
- 콜드·웜 로딩 시간
- 세이브·로드 시간과 파일 크기
- 설치 패키지와 패치 크기
- 최소 사양 장시간 세션 결과

## 하드 게이트

- 개발 에디터 성능을 최종 패키지 성능으로 대체하지 않는다.
- 평균 FPS만으로 끊김이 없다고 판단하지 않는다.
- 권장 사양 한 대만 측정하고 최소 사양 지원을 선언하지 않는다.
- 이전 저장을 실제로 열지 않고 호환된다고 주장하지 않는다.
- 출시 후보를 만든 뒤 검증 중인 바이너리를 교체하지 않는다.
- 차단 버그를 “알려진 문제” 목록으로 이동해 우회하지 않는다.

## 산출물

```text
docs/game-planner/releases/<version>/
├── RELEASE_MANIFEST.md
├── PERFORMANCE_MATRIX.md
├── INSTALL_UPDATE_REPORT.md
├── SAVE_COMPATIBILITY.md
├── KNOWN_ISSUES.md
├── ROLLBACK_PLAN.md
└── RELEASE_VERDICT.md
```

## 완료 게이트

- 검증한 바이너리와 배포할 바이너리의 해시가 같다.
- 최소 사양과 최악 시나리오의 증거가 있다.
- 설치, 업데이트, 저장, 제거, 롤백 경로를 실행했다.
- 플랫폼 필수 항목과 제3자 고지가 확인됐다.
- 차단 항목 0건이며 조건부 항목은 책임자와 기한이 있다.
