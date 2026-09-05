# 5단계 — 파일 구조와 브라우저 검증

판정: **PASS** · 검증일 2026-09-05

## 4단계 완료 게이트

HTML 파싱 성공, 한국어 lang·viewport·단일 h1·12개 section 확인. CSS, 두 JavaScript, 썸네일 및 세 작업 명세의 로컬 경로가 존재한다. 4단계 산출물 생성 및 정적 확인을 마친 뒤 이 단계 브라우저 검증을 실행했다.

## 검증 환경과 측정

- 로컬 URL: http://127.0.0.1:8861/
- macOS / 설치된 Google Chrome / Playwright, headless, reduced motion.
- 1440×1000 데스크톱, 390×844 모바일, 추가 320·768px 폭.
- 각 폭에서 scrollWidth == clientWidth: 1440/1440, 390/390, 320/320, 768/768. 페이지 수평 오버플로 0px. 넓은 표는 내부 스크롤.
- 영상 썸네일 자연 크기 1280×720, 로드 성공. 누락된 앵커 0, 중복 ID 0.
- HTTP 오류 0, 브라우저 콘솔/런타임 오류 0.

## 실제 실행한 상호작용

| 검사 | 결과 |
|---|---|
| 주장 필터 | 전체24, 공식 확인10, 영상 주장5, 미확정4, 보정4, 분석/권고1 |
| 숨겨진 주장 앵커 | 미확정 필터 후 C03 링크를 누르면 전체 복원·해당 주장 표시 |
| 세 작업 명세 선택 | 제목·본문·현재 다운로드 링크 모두 동기화 |
| 복사·다운로드 | 세 명세 모두 표시 본문 = 실제 클립보드 = HTTP200 Markdown 내용 |
| 권한 설명 선택 | Read only / Full access / Guard 설명 변경, 세 모드 정적 표 유지 |
| 체크리스트 | 1 / 7 완료 → 초기화 0 / 7 완료 |
| 타임라인 | 첫 구간 details 열림 |
| 모바일 목차 | 수평 목차에서 작업 명세 링크 이동 |
| 모바일 선택·필터 | Gmail 명세 전환 및 보정4개 표시 |
| 키보드 | 첫 Tab은 본문 건너뛰기, Enter로 #main 이동 |
| JavaScript 비활성 | 24개 주장·기본 상품 명세·세 Markdown 다운로드 링크 보존 |

## 시각 확인과 수정 내역

`desktop-hero.png`, `mobile-hero.png`, `desktop-data-flow.png`를 실제 이미지로 열어 확인했다. 한글 제목·버튼·썸네일·통계 카드·개념도에서 겹침과 잘림이 없고, 데스크톱 두 열이 모바일 한 열로 전환된다. 전체 페이지 캡처도 함께 보존했다.

브라우저 첫 검증이 통과해 이 단계에서 실패 수정·재검사는 없었다. 작성 중 로컬 데이터 JavaScript를 추가해 fetch 없이 명세를 바꿀 수 있게 했으며, 숨겨진 주장에 같은 해시로 다시 접근할 때도 링크 클릭 시 필터를 복원한다.

## 재현·증거

- `static.json`: 주 스킬의 validate_report.py 결과
- `browser.json`: 전체 측정 및 실제 기능 실행 결과
- `desktop.png`, `mobile.png`: 전체 페이지 캡처
- `desktop-hero.png`, `mobile-hero.png`, `desktop-data-flow.png`: 부분 캡처
- `file_tree.txt`: 검증 시점 0~5단계 파일 목록
- `manifest.sha256`: 0~4단계 파일 SHA-256 (로컬 전용 원본 info.json 포함; 공개 저장소에서는 제외)
- 실행기: 저장소 `scripts/verify_browser.cjs`, `scripts/finalize_validation.py`

이 검사는 보고서의 표시와 동작을 검사한다. Aside 앱 설치·로그인·쿠팡/Sheets/Gmail/Calendar 실제 작업은 수행하지 않았으며, 원본 시연의 성공률을 검증하는 테스트가 아니다.

5단계 완료 게이트: **PASS**. 게시 단계로 진행 가능.
