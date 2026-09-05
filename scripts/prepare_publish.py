from pathlib import Path
import shutil,json,hashlib
P=Path(__file__).resolve().parents[1]/'outputs/aside_browser_20260905';R=Path('/private/tmp/codex-utilization-aside-20260905');slug='aside-browser-20260905';bundle=P/'04_html_report'
for folder in ['docs','reports']:
 dest=R/folder/slug
 if dest.exists(): raise SystemExit(f'Collision: {dest}')
 shutil.copytree(bundle,dest)
readme=R/'README.md';text=readme.read_text();entry='[Aside AI 브라우저 — 탭 사이의 일을, 하나의 요청으로](https://stmlscd.github.io/codex_utilization/aside-browser-20260905/) · 한국어 자동 자막 전체와 공식 자료를 대조한 0–6단계 보고서. 24개 주장 검증, 권한·데이터 흐름, Sheets·Gmail·Calendar 작업 명세를 담았습니다. [새 산출물 저장소](https://github.com/stmlscd/aside-browser-video-report-20260905)\n\n';assert text.startswith('# codex_utilization\n\n');readme.write_text(text.replace('# codex_utilization\n\n','# codex_utilization\n\n'+entry,1))
index=R/'docs/index.html';text=index.read_text();needle='          <article class="source-card">\n            <h3>AI에게 업무를 맡기는 5단계</h3>'
card='''          <article class="source-card">
            <h3>Aside — 탭 사이의 일을, 하나의 요청으로</h3>
            <p>Aiden의 친절한 AI의 15분 10초 영상을 자동 자막과 공식 자료로 대조했습니다. 권한·Memory·로그인·Routine, 24개 주장 판정과 세 가지 실무 작업 명세를 담았습니다.</p>
            <p><a class="report-link" href="./aside-browser-20260905/">Aside AI 브라우저 검증 보고서 →</a></p>
          </article>
''';assert text.count(needle)==1;index.write_text(text.replace(needle,card+needle,1))
rows=[]
for f in sorted(bundle.rglob('*')):
 if f.is_file():
  rel=f.relative_to(bundle);assert f.read_bytes()==(R/'docs'/slug/rel).read_bytes()==(R/'reports'/slug/rel).read_bytes()
  rows.append({'path':str(rel),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
V=P/'06_publish';V.mkdir(exist_ok=True);(V/'bundle.json').write_text(json.dumps(rows,indent=2)+'\n')
(V/'06_publish_preflight.md').write_text('''# 6단계 게시 사전 확인

- 사용자가 GitHub Pages 실제 게시와 새 저장소 저장을 명시적으로 요청했다.
- 0→5단계 완료·브라우저 검증 PASS 후 게시를 준비했다.
- 원격: https://github.com/stmlscd/codex_utilization.git · main · 작업 시작 HEAD 55f2224d3491b63ae31454938f365a1193a366bf.
- 기존 clone 원격·작업 트리·최근 기록을 확인한 뒤 /private/tmp/codex-utilization-aside-20260905에 새 clone을 만들었다. git pull --ff-only: Already up to date. 초기 작업 트리 깨끗함.
- 저장소 AGENTS.md 전체를 읽었다. docs/·reports/ 하위 AGENTS.md 없음. 토큰·비밀번호·쿠키 제외와 명시적 파일 스테이징 규칙 적용.
- AGENTS.md는 이전 youtube-video-report-0to6-publisher 및 stage-00-* helper 구조를 지정하지만, 이번 사용자가 명시한 staged-video-report-publisher와 새 저장소 outputs/의 00_* 계약을 우선 적용했다. 다른 구조를 초기화하는 helper로 완료된 단계 산출물을 중복 생성하지 않았다.
- Pages: main /docs · legacy Pages build. 신규 slug aside-browser-20260905 충돌 없음.
- 게시용 docs/aside-browser-20260905와 저장소 관례의 reports/aside-browser-20260905 사본은 4단계 원본과 바이트 동일.
- 변경 범위: 위 두 번들, docs/index.html의 카드 1개, README.md의 링크·설명 1개.
- 신규 보관 저장소: stmlscd/aside-browser-video-report-20260905. 전체 수집 info.json은 로컬 전용이며 .gitignore로 제외. 공개 메타데이터 별도 보존.

배포 완료 정보·HTTP·라이브 브라우저 결과는 06_publish_record.md에 기록한다.
''')
print('Prepared',len(rows),'files in each of docs/reports; catalog + README updated')
