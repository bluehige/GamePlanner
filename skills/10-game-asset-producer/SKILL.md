---
name: game-asset-producer
description: Produce, post-process, export, import, and verify game art assets from approved asset contracts for 2D, 3D, animation, VFX, and UI pipelines.
---

# Game Asset Producer

승인된 Art Direction을 개별 자산 계약으로 바꾸고 생성·모델링·후처리·내보내기·엔진 검증까지 연결한다.

## 사용 시점

- `09-game-art-director`가 승인된 뒤 실제 자산을 만들 때
- AI 이미지 생성 결과를 스프라이트·맵·UI 자산으로 규격화할 때
- Blender 자산을 Godot, Unity, Unreal로 내보낼 때
- 기존 자산의 피벗, 스케일, 충돌, LOD, 텍스처를 정리할 때

## 입력

- Art Direction과 Asset Budget
- Asset Contract
- 대상 엔진과 import profile
- 카메라·월드 스케일·피벗 규칙
- source file과 provenance 정보
- 예상 플레이 상황과 검증 씬

## 절차

1. **Asset Contract 작성**
   - 게임 역할, 화면 크기, 실루엣, 색 역할, 금지 표현, 기술 사양, 엔진 경로, 수용 기준을 기록한다.
2. **파이프라인 선택**
   - `2d-sprite`, `2d-map`, `ui-graphic`, `3d-character`, `3d-environment`, `3d-prop`, `animation`, `vfx`
3. **원본 생산**
   - AI 생성, 수작업, 모델링, 외부 라이선스 자산 중 출처를 기록한다.
4. **결정론적 후처리**
   - 크롭, 프레임 분리, 정렬, 투명화, 이름, 포맷, 텍스처 규격, LOD를 자동화한다.
5. **내보내기**
   - 축, 단위, 위치 정책, 피벗, 재질, 텍스처, 애니메이션을 manifest에 남긴다.
6. **엔진 import**
   - 실제 프로젝트 import profile과 대상 씬에서 로드한다.
7. **V0~V4 검증**
   - V0 계약, V1 원본, V2 후처리, V3 엔진 렌더, V4 실제 플레이 가독성·성능
8. **등록**
   - 자산 카탈로그, provenance, 버전, 사용 위치를 갱신한다.

## 외부 연동

### 2D

`jay6697117/agent-sprite-forge-codex-skill`의 `generate2dsprite`, `generate2dmap`을 선택적으로 사용한다. 창의 생성과 결정론적 후처리를 분리하고, 프레임 기준점·공통 스케일·가장자리 접촉을 검사한다.

### 3D

`bluehige/blender_exprorter_for_Engine`을 별도 설치해 Blender 4.5.4~5.2 자산의 Godot·Unity·Unreal 내보내기와 sidecar manifest를 사용할 수 있다. GPL 도구 자체를 GamePlanner에 복사하지 않는다.

## Asset Contract 최소 필드

```yaml
asset_id: ENV-001
gameplay_role: ""
expected_screen_size_px: [64, 192]
silhouette_rule: ""
palette_role: ""
forbidden_visuals: []
technical:
  world_scale_m: []
  origin: bottom-center
  pivot: placement-base
  collision: simplified
  texture_size: 1024
  material_slots_max: 2
  export: glb
integration:
  engine_path: ""
  import_profile: ""
provenance:
  source_type: ai-generated
  source_ref: ""
acceptance: []
```

## 하드 게이트

- Art Direction이 없는 상태에서 대량 자산을 생산하지 않는다.
- 원본 생성 이미지를 검수 없이 최종 엔진 자산으로 사용하지 않는다.
- 자산의 시각 경계와 충돌 경계가 의미 있게 다르면 승인하지 않는다.
- 애니메이션 프레임마다 크기와 발 위치가 흔들리면 통과시키지 않는다.
- AI 생성 모델, 프롬프트, 라이선스, 외부 자산 출처를 누락하지 않는다.
- V3 이전 결과를 “게임 적용 완료”, V4 이전 결과를 “플레이 가독성 승인”으로 부르지 않는다.

## 산출물

```text
assets/source/
assets/runtime/
assets/manifests/
docs/game-planner/art/ASSET_CATALOG.md
evidence/assets/<asset-id>/
```

## 완료 게이트

- Asset Contract가 존재하고 Art Direction에 연결된다.
- 원본과 runtime 자산이 분리됐다.
- 내보내기·import 설정과 provenance가 기록됐다.
- 실제 엔진 렌더 V3가 통과했다.
- 최종 자산으로 승인하려면 실제 플레이 V4의 가독성·성능 기준을 통과했다.
