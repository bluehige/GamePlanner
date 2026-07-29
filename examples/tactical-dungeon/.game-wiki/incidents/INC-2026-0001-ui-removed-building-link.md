---
incident_id: INC-2026-0001
title: "UI 교체 중 기존 건물 연결 제거"
status: closed
severity: major
occurred_at: 2026-07-29
engine: "Godot 4.5"
branch: "example/ui"
baseline_sha: "abc1234"
fixed_sha: "def5678"
build_id: "example-1"
tags: [ui, regression]
---

# UI 교체 중 기존 건물 연결 제거

## 요청과 해석

### 사용자 요청 또는 원문 참조

배치 UI만 단순화한다.

### Agent 해석

화면 교체 과정에서 기존 건물 연결도 정리 대상으로 판단했다.

### 누락되거나 잘못된 가정

게임 규칙과 UI 경계를 읽지 않았다.

## 기대와 관찰

### 기대

기존 건물 기능을 유지한다.

### 관찰

업그레이드 경로가 단절됐다.

## 재현

- 환경: example-1
- 절차: 건물 선택 후 업그레이드
- 재현률: 100%
- 증거: example-log

## 근본 원인

- 분류: stale_context
- 최초 이상 경계: UI → game state
- 설명: 기준 기능 계약을 읽지 않았다.

## 수정

- 변경: 기존 신호 연결 복원
- 의도적으로 변경하지 않은 범위: 전투 공식과 저장
- 관련 커밋: def5678

## 검증

- 원증상: 통과
- 회귀: Day 1~5 건물 동작 통과
- 결과: PASS
- 증거 수준: E3

## 예방

- 규칙 후보: UI 변경은 게임 규칙과 데이터 연결을 보존한다.
- 자동 회귀 검사: 건물 신호 연결 테스트
- 승격 상태: closed

## 관련 문서

- Work Order: WO-2026-0001
