# Aside AI 브라우저 — 단계별 영상 검증 보고서

[공개 HTML 보고서](https://stmlscd.github.io/codex_utilization/aside-browser-20260905/) · [원본 영상](https://www.youtube.com/watch?v=9ZzF5iGj0BM)

Aiden의 친절한 AI의 「요즘 AI 브라우저는 어디까지 할까? Aside 직접 써봤습니다」를 한국어 자동 자막 전체와 공식 도움말·변경 기록·개인정보 정책으로 대조한 독립 분석 보고서다. Sheets·Gmail·Calendar 작업 흐름, 권한, Memory, 자동 로그인, Routine, MCP·CLI를 정리하고 검토 가능한 작업 명세 세 개를 제공한다.

주 스킬 `staged-video-report-publisher`의 [0→6 산출물 계약](references/stage-contract.md)을 순서대로 적용했다. 원본 수집·정제·소스맵·HTML·브라우저 검증·게시 기록을 이 **새 저장소**의 실제 `outputs/` 디렉터리에 보존한다. 공개 사이트의 기존 콘텐츠 저장소는 [stmlscd/codex_utilization](https://github.com/stmlscd/codex_utilization)이며, 이 저장소는 독립된 산출물 보관소다.

| 단계 | 산출물 |
|---|---|
| 0 활용 분류 | [00_usage_classification.md](outputs/aside_browser_20260905/00_usage_classification/00_usage_classification.md) |
| 1 원본·자막 상태 | [자료 목록](outputs/aside_browser_20260905/01_source_inventory/01_source_inventory_and_subtitle_status.md) |
| 2 전체 자막 정제 | [15개 시간 구간](outputs/aside_browser_20260905/02_refined_transcript/02_timeline_refined.md), [396개 정제 큐](outputs/aside_browser_20260905/02_refined_transcript/cleaned_cues.tsv) |
| 3 주장과 출처 | [24개 주장·21개 출처](outputs/aside_browser_20260905/03_source_map_outline/03_source_map_and_outline.md) |
| 4 HTML | [index.html](outputs/aside_browser_20260905/04_html_report/index.html) 및 로컬 assets |
| 5 검증 | [브라우저 검증 보고서](outputs/aside_browser_20260905/05_validation/05_validation_report.md)·JSON·스크린샷·해시 |
| 6 게시 | [게시 기록](outputs/aside_browser_20260905/06_publish/06_publish_record.md)·배포·라이브 검증 |

## 읽는 방법과 검증 범위

- HTML의 출처 ID는 `S01…S21`, 주장 ID는 `C01…C24`로 연결된다. 공식 확인10·영상 주장5·보정4·미확정4·분석/권고1을 구분했다.
- 표시용 자동 자막의 반복을 제거했다. 원본791블록(공백3), 비공백788큐 →396큐. 비공백 원문1,180행을 정제 본문과 대조했다. 영상15:10과 ASR 마지막15:12의2초 차이를 숨기지 않았다.
- 이 보고서는 Aside를 설치해 재현한 사용 후기가 아니다. 실제 상품 조사·메일 발송·일정 등록을 실행하지 않았다. 영상 화면·오디오 직접 검토와 독립 보안·성능 실험도 하지 않았다.
- Windows 출시일, Final confirm 토글의 현행 세부 범위, 앱 종료·잠자기 상태에서 Routine 실행, 제조사 속도 주장에는 확인 한계를 표시했다.
- 원본 영상·썸네일·자막 및 공식 문서의 권리는 각 제작자에게 있다. 출처·획득 시각·원문 해시를 보존한다.

## 로컬 보기와 재현

Python3로 `outputs/aside_browser_20260905/04_html_report`를 루트로 정적 서버를 실행한다. 외부 CDN·폰트·서비스 연결 없이 로컬 자산만으로 표시된다. JavaScript가 없어도 본문·출처·상품 명세·모든 명세 다운로드 링크를 읽을 수 있다.

`scripts/build_report.py`는 정제된 소스맵·타임라인에서 HTML·명세 데이터를 만든다. CSS와 동작 JavaScript는 `04_html_report/assets/`에 보존된 원본을 사용한다. `scripts/verify_browser.cjs [URL] [출력폴더]`는 Playwright와 설치된 Google Chrome으로 실제 인터랙션을 검사한다. Python 스크립트는 표준 라이브러리를 사용한다.

수집 과정에서 생성된 전체 `*.info.json`은 서명된 미디어 URL이 있어 로컬에만 보관하고 Git에서 제외했다. 공개용 `public-metadata.json`에는 제목·채널·길이·챕터 등 필요한 공개 필드가 있다. 1단계 원본 해시와 5단계 manifest에는 로컬 전용 파일의 해시도 포함되며, 공개 저장소 범위의 해시는 6단계 `public-manifest.sha256`을 사용한다.
