from pathlib import Path
import re,csv,html,json,hashlib
from normalize_vtt import parse_vtt
P=Path(__file__).resolve().parents[1]/'outputs/aside_browser_20260905';D=P/'02_refined_transcript';rawpath=P/'01_source_inventory/raw/9ZzF5iGj0BM.ko-orig.vtt';raw=rawpath.read_text();cues=list(csv.DictReader((D/'cleaned_cues.tsv').open(),delimiter='\t'));full=' '.join(c['text'] for c in cues)
payload=[];empty=[]
for block in re.split(r'\n\n+',raw):
 b=block.splitlines()
 for i,line in enumerate(b):
  if '-->' in line:
   lines=[' '.join(html.unescape(re.sub('<[^>]*>','',x)).split()) for x in b[i+1:]];lines=[x for x in lines if x]
   if not lines:empty.append(line)
   payload.extend(lines)
missing=[x for x in payload if x not in full];assert not missing
parsed,rolling=parse_vtt(rawpath)
stats=dict(raw_cues=raw.count('-->'),parsed_nonempty_cues=len(parsed),empty_cues=len(empty),empty_timings=empty,cleaned_cues=len(cues),reduction_from_raw_percent=round((1-len(cues)/raw.count('-->'))*100,2),reduction_from_nonempty_percent=round((1-len(cues)/len(parsed))*100,2),payload_lines=len(payload),unmatched_payload_lines=missing,first_start=cues[0]['start'],last_end=cues[-1]['end'],metadata_duration_seconds=910,asr_overrun_seconds=2,review='396 cues read in order; all raw nonempty payload lines matched. No direct audio/frame verification.')
(D/'normalization_stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
segments=[
(0,35,'브라우저 안의 반복 업무','브라우저의 검색·이동·입력을 AI에게 맡기는 사용 장면을 소개한다.','AI 브라우저라는 분류의 설명. 모든 업무 자동 완료를 보장하지 않는다.'),
(35,90,'쿠팡 조사 → Google Sheets','20만 원대 무선 청소기 중 리뷰가 많은 제품 3개를 골라 제품명·가격·평점·리뷰·특징을 Sheets에 정리하도록 요청한다.','작업 완료를 설명하는 발화 확인. 원본 Sheet와 상품별 조건·가격·실제 속도는 독립 검증하지 않았다.'),
(90,195,'AI 브라우저와 Real Work','로그인된 웹서비스를 직접 오가며 여러 단계의 업무를 수행하는 제품 방향을 설명한다. 다른 AI도 브라우저 조작 기능을 제공할 수 있다고 언급한다.','Real Work는 제품이 강조하는 사용 방향이다. 장시간 성공률이나 우위의 측정치가 아니다.'),
(195,250,'설치·가져오기·모델 연결','공식 홈페이지 설치, 방문 기록·쿠키·북마크 가져오기, 기존 AI 구독이나 API 키 연결을 안내한다. macOS만 지원하고 Windows는 9월 초 목표라고 말한다.','공식 시작 문서는 macOS15+를 안내. Windows 출시일 확정 근거는 미확인. Aside 제공 모델·외부 구독·API 비용을 구분한다.'),
(250,335,'탭 스타일과 모델 설정','San Francisco는 가로 탭, New York은 세로 탭으로 설명하고 Models 설정을 소개한다.','명칭과 배치는 시연 설명이다. 현재 도움말에서 해당 탭 스타일 명칭을 별도 확인하지 못했다.'),
(335,388,'Memory와 과거 맥락','이전 페이지·작업 맥락을 활용하는 예와 로컬 중심 저장, Memory 설정을 설명한다.','로컬에 저장된다고 작업 맥락의 외부 모델 전송이 없다는 뜻은 아니다. 개인정보 정책의 모델 전송 조항과 구분한다.'),
(388,462,'Password Manager','저장된 로그인으로 인증하되 비밀번호 값을 모델에 직접 보여주지 않는 자동 채우기 구조를 설명한다.','공식 문서에서 URL·접근 정책 검사와 raw password 비노출 확인. MFA·CAPTCHA 등 사람이 처리할 단계는 남는다.'),
(462,524,'Ask Aside와 사이트 탐색','현재 페이지 요약과 여러 페이지에서 요금·정책을 찾는 요청을 설명한다.','조사할 사이트·결과물·제외할 행동을 지정하는 방법으로 활용한다. 이 보고서에서 요금·환불을 대리 결정하지 않는다.'),
(524,568,'권한과 Final confirm','Read only·Guard·Full access와 최종 실행 전 확인 설정을 설명한다.','Read only는 파일 변경을 하지 않는 검토 모드로 공식 문서에 명시. 작업 폴더 제한만으로 설명하지 않는다. Final confirm의 현재 전체 적용 범위는 별도 확인 필요.'),
(568,621,'Gmail 초안과 백그라운드 작업','내일 오후3시 미팅 확인 메일을 실제로 전송하지 말고 작성까지만 하도록 요청한다. 다른 탭을 쓰며 진행을 볼 수 있다고 설명한다.','메일 발송 시연이 아니다. 백그라운드 동작과 종료·잠자기 상태에서의 실행 보장은 다르다.'),
(621,727,'Gmail → Google Calendar','메일에서 날짜·시간·장소·주요 내용을 읽어 캘린더 일정으로 옮기는 다단계 요청과 결과를 설명한다.','원본 메일·캘린더를 확인하지 않았다. 초대 여부·시간대·중복·최종 저장은 실제 업무에서 별도로 검증한다.'),
(727,786,'Routine과 반복 실행','설정에서 직접 만들기, 반복 작업 제안, 대화에서 루틴 요청을 안내한다.','공식 Cron은 새 작업, Heartbeat는 기존 대화를 이어간다. 제안은 활성화 전 초안. 앱 종료·기기 잠자기 중 실행은 수집 자료로 확정하지 않는다.'),
(786,818,'Skills·MCP·CLI 확장','내장·추가 스킬, 외부 도구 연결, CLI를 통한 에이전트의 브라우저 사용 가능성을 소개한다.','공식 문서에서 Aside를 MCP 서버로 연결하는 방향을 확인. 모든 외부 MCP 연결 방식·스킬 설치 세부는 미확인.'),
(818,887,'체감 속도와 적합한 사용자','빠르게 느꼈다는 후기와 여러 서비스 간 이동·정리가 잦은 사용자에게 유용할 수 있다는 의견, 결과 검토 필요성을 제시한다.','체감 속도는 발표자의 경험이다. 동일 조건 벤치마크나 업무별 성공률로 인용하지 않는다.'),
(887,910,'마무리','주요 기능과 실제 활용 방식 소개를 정리하고 구독·다음 영상 안내로 마무리한다.','메타데이터 길이는15:10이나 마지막 자동 자막 종료는15:12.000이다. 2초 차이를 보존하고 타임코드는 영상 길이 안에서 제공한다.')]
def sec(t):h,m,s=t.split(':');return int(h)*3600+int(m)*60+float(s)
records=[]
for start,end,title,summary,note in segments:
 ids=[i+1 for i,c in enumerate(cues) if sec(c['start'])<end and sec(c['end'])>start]
 records.append(dict(start=start,end=end,title=title,summary=summary,note=note,cue_ids=ids))
assert set(i for r in records for i in r['cue_ids'])==set(range(1,len(cues)+1))
(D/'timeline.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
fmt=lambda x:f'{x//60:02d}:{x%60:02d}'
s=f'''# 2단계 · 정제와 시간대별 대조

결과 PASS · 자동 한국어 자막 전체396큐를 읽고 원시 비공백 payload {len(payload)}행의 정제 본문 포함을 확인했다.

원시791타이밍 블록 → 비공백788큐(공백만 있는3개 제외) → 정제396큐. 전체 블록 기준49.94%, 유효 큐 기준49.75% 감소. 의미 정보 손실률이 아닌 롤링 표시 중복 감소율이다.

주 스킬 normalize_vtt.py를 바탕으로 앞선 보고서에서 확인한 공백 행 처리 보정본을 재사용했다. VTT 타임태그 제거·HTML entity 해석·연속 공백 정리·연속 반복 합치기 수행. 원시 payload 전부 대조하여 누락0 확인.

시작00:00.320, 마지막 종료15:12.000. 플랫폼 길이15:10과 2초 불일치. 원본 큐를 강제 자르지 않았으며 최종 타임라인은 영상 길이에 맞춰15:10으로 표시하고 차이를 명시한다.

제작자 챕터13개를 유지 가능한 경계로 삼고, Memory/Password Manager 및 권한/Gmail 설명을 분리해15개 의미 구간으로 정리했다. 경계에 걸친 큐는 양쪽 구간에 연결할 수 있으며396큐 모두 포함한다.

## 용어 교정 메모
‘업사이드/여사이드’는 Aside, ‘메고OS’는 macOS, ‘채치T/채치피pt’는 ChatGPT, ‘G/GL/Gma’는 Gmail, ‘파이널 컨펌’은 Final confirm으로 의미 요약에서 표기한다. 사용자 설명과 문맥에 근거한 표기이며 TSV 원문은 바꾸지 않는다. 오디오나 화면을 확인한 교정으로 주장하지 않는다.

'''
for r in records:s+=f"## [{fmt(r['start'])}–{fmt(r['end'])}](https://www.youtube.com/watch?v=9ZzF5iGj0BM&t={r['start']}s) · {r['title']}\n\n{r['summary']}\n\n검증 메모: {r['note']}\n\n정제 큐 {min(r['cue_ids'])}–{max(r['cue_ids'])}.\n\n"
s+='## 완료 게이트\n\n원시·정제본 추적, 전체 대조, 시간 구간·교정 메모·2초 길이 차이 보존 완료. 다음은 소스맵·목차.\n';(D/'02_timeline_refined.md').write_text(s)
print(json.dumps(stats,ensure_ascii=False,indent=2))
