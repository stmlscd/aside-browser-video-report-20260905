from pathlib import Path
import json,hashlib,subprocess,datetime
R=Path(__file__).resolve().parents[1];P=R/'outputs/aside_browser_20260905';V=P/'06_publish';site=Path('/private/tmp/codex-utilization-aside-20260905')
run=json.loads((V/'workflow.json').read_text());http=json.loads((V/'http.json').read_text());live=json.loads((V/'live/browser.json').read_text());pre=json.loads((V/'prepublish/browser.json').read_text())
assert run['status']=='completed' and run['conclusion']=='success' and http['pass'] and live['pass'] and pre['pass']
sha=subprocess.check_output(['git','-C',str(site),'rev-parse','HEAD'],text=True).strip();assert run['headSha']==sha
status=subprocess.check_output(['git','-C',str(site),'status','--short'],text=True).strip();assert not status
archiveInitial=subprocess.check_output(['git','-C',str(R),'rev-list','--max-parents=0','HEAD'],text=True).strip()
rows='\n'.join(f"| `{x['path']}` | {x['status']} | {x['bytes']:,} | 일치 |" for x in http['files'])
(V/'06_publish_record.md').write_text(f'''# 6단계 — GitHub Pages 게시 기록

최종 판정: **PASS** · 확인 시각 {http['checked_at']}

## 공개 위치와 저장소

- 공개 URL: https://stmlscd.github.io/codex_utilization/aside-browser-20260905/
- 공개 목록: https://stmlscd.github.io/codex_utilization/ (HTTP200·신규 링크 존재)
- **새 산출물 저장소**: https://github.com/stmlscd/aside-browser-video-report-20260905
- 게시 저장소: https://github.com/stmlscd/codex_utilization
- 신규 보관소 로컬 경로: `{R}`
- 게시 작업 clone: `{site}`
- 사용자가 주 스킬·0→6 순차 수행·새 저장소 저장·기존 Pages 게시를 명시한 요청에 따라 실행했다.

## Git와 배포

- Pages branch/source: `main` / `docs` · build_type `legacy`.
- 게시 커밋: `{sha}`
- 커밋 메시지: `Publish Aside AI browser evidence report and practical task templates`
- 커밋 링크: https://github.com/stmlscd/codex_utilization/commit/{sha}
- 배포 작업: `{run['databaseId']}` · `{run['name']}` · `{run['status']}` / `{run['conclusion']}`.
- 작업 링크: {run['url']}
- 최초 산출물 보관 커밋: `{archiveInitial}` (0~5단계·게시 사전 확인). 라이브 검증과 이 게시 기록은 후속 커밋으로 저장한다. 최종 보관 커밋은 저장소 main 기록에서 확인할 수 있다.
- 게시 완료 뒤 사이트 clone `git status --short`: 빈 출력, **clean**.
- Git add는 신규 docs/reports 번들·README·목록으로 한정했다. `git diff --cached --check` 통과.
- 게시 clone과 새 저장소 모두 force push·reset 없이 main으로 push했다.

## HTTP와 파일 동일성

모든 응답은 공개 URL에서 직접 확인했다. 본문·CSS·두 JS·이미지·세 Markdown·JSON 총9개가 로컬4단계 산출물과 바이트 동일하다.

| 파일 | HTTP | 바이트 | 로컬 SHA-256 비교 |
|---|---:|---:|---|
{rows}

개별 전체 SHA-256과 요청 URL: `http.json`. 배포 전 번들 해시: `bundle.json`. docs/ 및 reports/ 보존 사본은 모두 4단계 원본과 바이트 동일하다.

## 배포 전·후 브라우저 검증

- 게시 경로 재현: `http://127.0.0.1:8862/codex_utilization/aside-browser-20260905/` PASS (`prepublish/browser.json`).
- 공개 사이트: 위 공개 URL을 실제 Google Chrome / Playwright에서 열어 PASS (`live/browser.json`).
- title: `{live['desktop']['title']}` · lang `ko`.
- 데스크톱1440×1000, 모바일390×844 및320·768px에서 페이지 가로 넘침0px.
- 이미지 자연 크기1280×720, 누락0. 깨진 내부 앵커0, 중복ID0, 콘솔·런타임 오류0, HTTP 오류0.
- 24개 주장 필터·숨긴 주장 앵커 복원·권한 설명3종·세 명세 선택과 실제 복사·다운로드 일치·체크 초기화·타임라인·모바일 목차·키보드 건너뛰기 모두 통과.
- JavaScript가 없어도 24개 주장·기본 명세·명세3개 다운로드 링크 유지.
- `live/desktop-hero.png`, `live/mobile-hero.png`, `live/desktop-data-flow.png` 및 전체 화면 스크린샷 보존. 로컬과 같은 레이아웃이며 라이브 부분 캡처도 이미지로 확인했다.

## 보관 범위와 한계

0→6 산출물이 새 저장소의 `outputs/aside_browser_20260905/`에 있다. `file_tree.txt`는 전체 공개 파일 목록, `public-manifest.sha256`은 자신의 파일을 제외한 공개 보관 파일 해시다. 원본 자동 자막과 자료는 내용 보존을 우선해 줄끝 공백을 바꾸지 않았다.

서명된 미디어 URL이 포함된 전체 `*.info.json`은 로컬에서만 보존하고 Git에서 제외했다. 공개 메타데이터와 원본 해시는 별도 파일로 남겼다. 인증 정보·쿠키·API 키는 수집하거나 보관하지 않았다.

영상 자막·공식 자료 검증 보고서로서 Aside 앱의 실제 계정 작업이나 보안·성능을 재현한 결과는 아니다. 미확정 항목은 HTML과 소스맵에서 유지했다.

6단계 완료 게이트: **PASS**. 공개 HTML·모든 번들 자산 HTTP200 및 라이브 브라우저 검증 완료.
''')
# Include all intended public files (existing and newly written), excluding local runtime and raw signed metadata.
files=[]
for f in sorted(R.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(R)
 if any(x in rel.parts for x in ['.git','node_modules','__pycache__']) or f.name=='.DS_Store' or f.suffix=='.pyc' or f.name.endswith('.info.json') or f.name=='public-manifest.sha256':continue
 files.append(f)
tree=V/'file_tree.txt';tree.write_text('\n'.join(str(f.relative_to(R)) for f in files if f!=tree)+'\noutputs/aside_browser_20260905/06_publish/file_tree.txt\noutputs/aside_browser_20260905/06_publish/public-manifest.sha256\n')
if tree not in files:files.append(tree)
(V/'public-manifest.sha256').write_text(''.join(f'{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.relative_to(R)}\n' for f in sorted(files)))
print('Publication PASS;',sha,';',len(files),'public file hashes')
