# Skill Catalog

| 번호 | 스킬 | 기본 호출 시점 | 성격 | 주요 산출물 |
|---:|---|---|---|---|
| 00 | `game-production-router` | 모든 요청 시작 | 내부 | Route Packet |
| 01 | `game-idea-portfolio-router` | 아이디어가 미정이거나 후보가 필요할 때 | 외부 어댑터 | 후보 포트폴리오 |
| 02 | `game-foundation-director` | 큰 기둥을 확정하기 전 | 내부+외부 원칙 | Game Contract, Risk Register |
| 03 | `game-foundation-project-builder` | 기획 계약 승인 직후 | 내부 | 게임별 전용 Skill |
| 04 | `game-prototype-gate` | 재미·기술 가정의 위험이 클 때 | 내부 | Prototype Verdict |
| 05 | `game-design-spec` | 프로덕션 계획 전 | 내부+외부 어댑터 | GDD, System Contracts, Traceability |
| 06 | `game-work-order` | 모든 구현·수정 작업 전 | 내부 | Work Order |
| 07 | `game-change-impact-auditor` | 중·고위험 변경 전 | 내부 | Impact Report, Regression Plan |
| 08 | `game-ui-ux-bridge` | UI·HUD·메뉴·입력 UX 작업 | 외부 어댑터 | Screen Contract, UI Evidence Plan |
| 09 | `game-art-director` | 그래픽 리소스 생산 전 | 내부 | Art Direction, Style Bible |
| 10 | `game-asset-producer` | 승인된 자산 생산 | 내부+외부 어댑터 | Asset Contract, Import Evidence |
| 11 | `gameplay-balance-lab` | 전투·경제·성장 수치 설계 | 내부 | Balance Model, Golden Scenarios |
| 12 | `game-implementation-director` | 승인된 작업 구현 | 외부 어댑터 중심 | Implementation Plan, Commits |
| 13 | `systematic-game-debugging` | 버그·오작동·성능 이상 | 내부+외부 연동 | Reproduction, Root Cause, Fix Evidence |
| 14 | `content-save-validator` | 콘텐츠·데이터·저장 변경 | 내부 | Data/Save Validation Report |
| 15 | `game-verification-gate` | 모든 완료 주장 직전 | 내부 | Verification Evidence Pack |
| 16 | `playtest-experiment-director` | 프로토타입·마일스톤·출시 후보 | 내부+외부 참고 | Playtest Plan, Decision |
| 17 | `game-dev-memory` | 세션 시작·종료와 사건 발생 시 | 내부, LLM Wiki 패턴 | Incident, Decision, Handoff, Rule |
| 18 | `performance-release-gate` | 출시 후보 빌드 | 내부 | Performance Budget, Release Verdict |
| 90 | `skill-quality-auditor` | GamePlanner 스킬 변경 시 | 내부 | Skill Audit Report |

## 반복 루프

실제 개발 중에는 `06 → 07 → 12 → 15 → 17`이 기본 반복 단위다. 문제가 생기면 `13`을 삽입하고, 데이터나 저장을 건드렸다면 `14`, 플레이 경험 판단이 필요하면 `16`을 삽입한다.
