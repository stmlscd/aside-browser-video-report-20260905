from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]/'outputs/aside_browser_20260905';D=P/'03_source_map_outline';D.mkdir(exist_ok=True)
rows=[
('S01','영상·한국어 자동 자막','영상 원자료','https://www.youtube.com/watch?v=9ZzF5iGj0BM','9ZzF5iGj0BM.ko-orig.vtt','자동 자막 발화 대조. 화면·오디오 직접 시청 및 결과 재현 아님.'),
('S02','사용자 제공 설명·수집 설명란','제작자·사용자 제공','https://www.youtube.com/watch?v=9ZzF5iGj0BM','9ZzF5iGj0BM.description','핵심 주제·타임라인·공식 URL. 오픈채팅의 별도 가이드는 미수집.'),
('S03','공개 영상 메타데이터','플랫폼 자료','https://www.youtube.com/watch?v=9ZzF5iGj0BM','public-metadata.json','15:10·게시일·채널·13개 챕터.'),
('S04','Get started','공식 도움말','https://docs.aside.com/help/get-started','official/get-started.md','macOS15+·계정·프로필 가져오기.'),
('S05','Run tasks','공식 도움말','https://docs.aside.com/help/tasks','official/tasks.md','사이트·파일·여러 단계·권한·Steer/Queue.'),
('S06','Set agent permissions','공식 도움말','https://docs.aside.com/help/security','official/security.md','Read only·Guard·Full access와 Allow/Ask/Deny.'),
('S07','Manage memory','공식 도움말','https://docs.aside.com/help/memory','official/memory.md','Overview·History·Configure와 기억 보존 기간.'),
('S08','Use Password Manager','공식 도움말','https://docs.aside.com/help/password-manager','official/password-manager.md','자동 채우기·URL 검사·MFA 등 사람 단계.'),
('S09','Configure password autofill','공식 도움말','https://docs.aside.com/help/passwords','official/passwords.md','AI 접근 정책·가져오기·암호화 동기화.'),
('S10','Configure AI providers','공식 도움말','https://docs.aside.com/help/ai','official/ai.md','Aside·Subscription·API의3가지 경로.'),
('S11','Manage your Aside subscription','공식 도움말','https://docs.aside.com/help/subscription','official/subscription.md','Aside 크레딧과 연결 제공자 비용을 구분.'),
('S12','Use routines','공식 도움말','https://docs.aside.com/help/automation','official/automation.md','Cron·Heartbeat·중첩 건너뛰기·제안 활성화.'),
('S13','Privacy Policy','공식 정책','https://aside.com/policy/privacy','official/privacy-policy.html','2026-06-23 정책. §4 모델이 보는 작업 맥락의 전송, §1 동기화·분석 시스템.'),
('S14','Manage privacy and local data','공식 도움말','https://docs.aside.com/help/privacy','official/privacy.md','Analytics sharing 기본 on, 기록·쿠키·기타 설정.'),
('S15','Use Aside as your browser','공식 도움말','https://docs.aside.com/help/browser-basics','official/browser-basics.md','Ask AI·페이지 선택·분할탭·단축키.'),
('S16','Use the side panel','공식 도움말','https://docs.aside.com/help/side-panel','official/side-panel.md','페이지 첨부와 요약·초안의 중지 경계 예시.'),
('S17','Use the CLI, MCP, and REPL','공식 도움말','https://docs.aside.com/help/developers','official/developers.md','aside 명령·aside mcp 서버·aside repl.'),
('S18','Components changelog','공식 변경 기록','https://docs.aside.com/changelog/components','official/changelog-components.md','2026-09-02 CLI skill 설치, 2026-07-11 외부 MCP 서버 설정.'),
('S19','Aside Browser changelog','공식 변경 기록','https://docs.aside.com/changelog/native','official/changelog-native.md','Windows 관련 구현 기록과 keep-tasks-running 설정 기록. 일반 출시 완료 증거와 구분.'),
('S20','Aside 홈페이지','공식 제품 소개','https://aside.com/','official/home.html','Real Work·자동 로그인·로컬 중심·벤치마크 홍보. 상세 도움말·정책을 우선 대조.'),
('S21','Aside 다운로드 안내','공식 배포 안내','https://aside.com/download','official/download.html','조회 시 macOS DMG 설치 안내. Windows 일반 배포 시점 확인되지 않음.')]
sources=[dict(id=i,title=t,grade=g,url=u,path='01_source_inventory/raw/'+p,note=n,checked='2026-09-05') for i,t,g,u,p,n in rows]
claims=[
('C01','Real Work는 여러 웹서비스의 실제 작업을 잇는 방향','공식 확인',['S05','S20'],90,'공식 자료는 웹 탐색·파일·로그인·승인을 포함하는 여러 단계 작업을 설명한다. 모든 사이트에서 모든 일이 성공한다는 보장은 아니다.'),
('C02','쿠팡 제품3개를 Sheets에 정리하는 시연','영상 주장',['S01','S02'],35,'20만 원대 무선 청소기3개의 가격·평점·리뷰·특징을 표로 만드는 시연을 설명한다. 현재 상품 가격이나 원본 Sheet의 정확성을 이 보고서가 재검증하지는 않았다.'),
('C03','공식 시작 안내의 지원 조건은 macOS15+','공식 확인',['S04','S21'],195,'Aside 계정과 브라우저 구성요소가 필요하며 공식 시작 문서는 macOS15.0 이상을 명시한다. 다운로드 페이지도 DMG 설치를 안내한다.'),
('C04','Windows의 9월 초 출시 목표는 확정할 수 없다','미확정',['S01','S04','S19','S21'],225,'영상은 9월 초 출시 목표를 말한다. 변경 기록에는 더 이른 Windows 관련 구현 항목이 있으나 현재 시작·다운로드 안내에서 일반 배포 완료와 정확한 출시일을 확인하지 못했다.'),
('C05','가로·세로 탭 스타일 명칭은 시연 기준','영상 주장',['S01','S02','S15'],280,'영상은 San Francisco를 가로 탭, New York을 세로 탭으로 설명한다. 수집한 현재 도움말에서 이 두 명칭을 별도 확인하지 못했으므로 실제 설치 버전의 UI를 확인한다.'),
('C06','모델 연결은 Aside·Subscription·API로 나뉜다','공식 확인',['S10'],233,'Settings > Models > Providers에서 연결한다. Aside 문서는 ChatGPT Plus/Pro, Claude Pro/Max 등 구독의 OAuth 연결과 API 키 제공자를 안내한다. 이는 Aside의 지원 설명이며 다른 제공자의 정책 승인 여부를 별도로 판정한 것은 아니다.'),
('C07','구독 연결과 Aside 사용량은 하나의 무료 한도가 아니다','보정',['S10','S11'],307,'Aside 크레딧, 외부 구독 사용량, API 계정 과금은 구분된다. 사용할 모델·플랜의 현재 한도와 결제 주체를 확인한다. 특정 월 구독료나 무제한 사용을 단정하지 않는다.'),
('C08','Memory는 저장 내용과 보존 기간을 관리할 수 있다','공식 확인',['S07'],335,'Settings > Memory에서 Overview·History·Configure를 제공한다. 기억 생성 여부와 Never forget/30days/90days 보존 기간을 설정한다. 기억을 끄는 것을 기존 저장 데이터 전체 삭제로 해석하지 않는다.'),
('C09','로컬 저장은 외부 모델 전송이 없다는 뜻이 아니다','보정',['S01','S13','S20'],367,'정책 §4는 호스팅된 모델이 프롬프트·도구 결과·선택한 페이지 스냅샷·스크린샷·파일 등 작업에 필요한 맥락을 받는다고 명시한다. 홈페이지의 넓은 비공유 문구보다 데이터 종류와 실행 경로를 나누어 이해해야 한다.'),
('C10','비밀번호 원문을 모델에 주지 않는 자동 채우기 구조','공식 확인',['S08','S09'],414,'공식 문서상 에이전트는 raw password를 받지 않고 허용된 자격증명을 대상 URL에 자동 채운다. 이 제품 설계 설명은 독립 보안 감사나 로그인 뒤 모든 페이지 데이터의 비노출 보장이 아니다.'),
('C11','자동 로그인에도 정책과 사람의 인증 단계가 남는다','보정',['S08','S09'],414,'Always allow·While unlocked·Never와 항목별 정책을 확인한다. MFA·CAPTCHA·신원 확인은 사람의 조작이 필요할 수 있다. 시크릿 작업에서 에이전트의 Password Manager 접근은 지원하지 않는다고 도움말이 명시한다.'),
('C12','Read only는 작업 폴더 제한보다 파일 변경 금지가 핵심','보정',['S01','S05','S06'],535,'공식 문서는 Read only를 브라우저·파일 맥락을 검사하되 파일을 바꾸지 않는 모드, Guard를 승인된 폴더 작업과 다른 폴더 접근 전 질문, Full access를 컴퓨터 전체 읽기·쓰기로 설명한다.'),
('C13','세션 모드와 도구·폴더 권한은 함께 적용된다','공식 확인',['S06'],524,'기본값은 Guard. Settings > Agents의 Sandbox·File·Tool permissions와 작업별 설정을 함께 확인한다. Allow/Ask/Deny 중 Deny가 우선하며 Full access도 저장된 비밀번호 원문을 드러내지는 않는다.'),
('C14','Final confirm의 현재 세부 범위는 미확정','미확정',['S01','S08','S20'],555,'영상은 켜면 전송·결제·삭제·제출 전 확인한다고 설명한다. 공식 사이트도 민감 작업 확인을 강조하지만 수집한 도움말·변경 기록에서 이 토글의 현재 위치·기본값·모든 적용 예외를 확인하지 못했다. 앱에서 실제 동작을 검사해야 한다.'),
('C15','Gmail 시연의 요청은 발송이 아니라 초안 작성','영상 주장',['S01','S02'],568,'내일 오후3시 미팅 확인 메일을 작성하되 전송하지 말라고 명시한다. 보고서에서도 초안 작성 완료와 외부 발송을 분리한다.'),
('C16','다른 탭에서 일할 수 있다는 백그라운드 시연','영상 주장',['S01','S02','S05'],590,'별도 탭에서 에이전트가 작업해 사용자의 현재 화면 포커스를 빼앗지 않는다고 설명한다. 본 보고서는 그 동작을 직접 시험하지 않았다.'),
('C17','Gmail의 일정 정보를 Calendar로 옮기는 다단계 요청','영상 주장',['S01','S02'],621,'메일 날짜·시간·장소·주요 내용을 일정에 넣었다고 설명한다. 저장 결과·초대 메일·중복 여부는 원본 계정 자료 없이 독립 확인할 수 없다.'),
('C18','Routine은 새 작업 실행과 기존 대화 이어가기를 구분','공식 확인',['S12'],727,'Cron은 예약 시 새 작업을 시작하고 Heartbeat는 기존 대화를 깨운다. 겹친 실행은 건너뛰며 대상 대화가 없으면 일시 중지한다. 추천 Routine은 활성화하기 전까지 초안이다.'),
('C19','브라우저 종료·기기 잠자기 중 Routine 실행은 미확정','미확정',['S05','S12','S19'],727,'변경 기록에는 keep-tasks-running 제어가 있으나 이 옵션의 종료·잠자기·재부팅 동작과 무인 실행 보장까지 수집 문서가 설명하지 않는다. 해당 환경에서 직접 실행·실패·누락을 검사한다.'),
('C20','MCP 연결은 안으로 가져오기와 밖으로 제공하기를 구분','공식 확인',['S17','S18'],799,'개발자 문서의 aside mcp는 외부 에이전트가 Aside를 사용하는 서버 경로다. 2026-07-11 변경 기록은 Aside 내부에서 외부 MCP 서버를 연결하는 설정도 안내한다. 두 방향의 설정과 권한은 따로 확인한다.'),
('C21','CLI를 통한 브라우저 skill 설치도 공식 변경 기록에 있다','공식 확인',['S17','S18'],786,'2026-09-02 기록은 aside skills install로 지원 도구에 aside-browser skill을 설치하고 list/show로 확인하는 기능을 설명한다. 영상의 내장 스킬 전체 목록·임의 스킬의 호환성을 보장하는 뜻은 아니다.'),
('C22','체감 속도·제품 벤치마크를 실제 업무 성공률로 바꾸지 않는다','미확정',['S01','S20'],818,'영상의 빠르다는 평가는 개인 경험이다. 홈페이지 수치도 제조사 주장으로, 이 보고서는 동일 조건 독립 실험을 하지 않았으므로 도입 효과·속도 우위를 확정하지 않는다.'),
('C23','처음에는 조사→초안→검토 가능한 변경 순서로 시험','분석/권고',['S02','S05','S16'],818,'상품 조사에는 URL·옵션·조사 시각을, 메일에는 수신자·발송 경계를, 일정에는 시간대·중복·초대 여부를 적는다. 종료 지점과 확인할 결과를 정한 뒤 같은 샘플로 재검사한다.'),
('C24','분석 전송 설정도 별도로 확인할 수 있다','공식 확인',['S13','S14'],367,'현재 도움말은 Analytics sharing의 기본값을 on으로 설명한다. Settings > Security & Privacy에서 확인하고, 계정·동기화·분석·호스팅 모델 처리의 범위를 각각 검토한다.')]
c=[dict(id=i,title=t,status=g,sources=ss,seconds=n,conclusion=x) for i,t,g,ss,n,x in claims]
for x in sources:assert (P/x['path']).is_file()
for x in c:assert set(x['sources'])<={x['id'] for x in sources}
(D/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n');(D/'claims.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
text='''# 3단계 · 소스맵·목차

결과 PASS · 24개 주장 / 21개 출처. 공식 문서는 조회일2026-09-05 기준이며 제품 소개, 도움말, 변경 기록, 정책은 서로 다른 증거 역할을 갖는다.

## 논지·독자
브라우저에서 반복 업무를 처리하는 실무자가 ‘어떤 작업을 맡길지’와 ‘무엇을 읽고 쓰고 전송할지’를 구체적으로 결정하도록 돕는다. 단순 기능 나열을 넘어 입력·처리·승인·검증의 경계를 보여준다.

## 근거 우선순위
정확한 권한·데이터 처리에는 상세 도움말과 개인정보 정책을 우선한다. 변경 기록은 특정 버전 기능의 근거이며 현재 일반 배포 범위와 같다고 추정하지 않는다. 제조사 보안·성능 문구는 독립 검증 결과가 아니다. 영상은 시연 발화를 확인하는 원자료로 사용하며 화면을 본 것처럼 표현하지 않는다.

## 보고서 구조
1. Hero: ‘탭 사이의 일을, 하나의 요청으로.’ 메타데이터·원문·핵심 경계.
2. 활용 지도: 상품 조사→Sheets, Gmail 초안, Gmail→Calendar. 입력·결과·검토점.
3. 설치·모델: macOS15+ 확인, Windows 출시 불확실성, 데이터 가져오기, 모델 연결과 비용 경계.
4. 권한 비교: Read only/Guard/Full access, 파일·도구 규칙·Final confirm 관계. 실제 앱을 제어하지 않는 설명용 선택 UI.
5. 데이터 흐름: 로컬 기록 / 모델용 작업 맥락 / 자격증명 자동 채우기 / 대상 웹서비스, 정책 기반 개념도.
6. Memory·Password Manager: 관리 위치와 보존·접근 설정. 자동 로그인 예외.
7. Routine·확장: Cron/Heartbeat, 중복·대화 부재·종료/잠자기 한계; MCP 양방향·CLI.
8. 바로 쓰는 작업 명세: 상품·메일·일정 프롬프트 선택·복사·다운로드. 원본 영상 명령을 재구성한 작성자 예시 표시.
9. 팩트체크: C01–C24 판정 필터, 출처·관련 시간 링크.
10. 타임라인15구간: 원본 이동, ASR2초 길이 차이 표시.
11. 첫 실행 체크리스트와 출처·방법론.

## 시각·접근성 설계
아주 연한 회색 종이색, 짙은 남색, 밝은 청록 계열로 브라우저 업무의 흐름을 표현한다. 가상 브라우저 개념도는 ‘개념도’로 명시하며 실제 앱 스크린샷처럼 꾸며 증거로 사용하지 않는다. 실제 썸네일은 출처 링크와 함께 사용. 카드보다 긴 흐름·비교표·파일 명세를 중심으로 배치한다.

외부 폰트·CDN 없음, 로컬 상대 자산. 반응형1440/390px, 대비·키보드 포커스·감소 모션·표 내부 스크롤. JS가 없어도 본문·출처·전체 권한표·기본 프롬프트가 보인다. 선택 UI는 분석 보조이며 Aside의 권한을 실제 변경하지 않는다.

수치카드: 15:10·게시일 S03, 원시791→정제396은 단계2 기록,13챕터→15구간은 편집 기록.3제품 S01/S02. 비용 숫자·성능 점수는 카드화하지 않는다. macOS15+ 및 메모리 보존30/90일 등은 공식 출처를 인접 표기.

## 작성 경계
Aside 설치·구독 가입·계정 연결·로그인·Gmail 발송·일정 등록·구매·Routine 생성은 하지 않는다. 보고서와 가상 선택 UI, 프롬프트 예시만 제작한다. 세무·법률 해석이나 타 모델 제공자의 별도 정책 승인을 판단하지 않는다.

## 출처
'''
for s in sources:text+=f"- **{s['id']} · {s['grade']} · [{s['title']}]({s['url']})** — `{s['path']}`. {s['note']}\n"
text+='\n## 주장 지도\n\n|ID|판정|주장·표현|근거|\n|---|---|---|---|\n'
for x in c:text+=f"|{x['id']}|{x['status']}|{x['title']} — {x['conclusion']}|{', '.join(x['sources'])}; 영상{x['seconds']}초|\n"
text+='\n## 완료 게이트\n\n모든 출처 파일과 주장 ID 연결 확인. 후속 공식 확인으로 stage2의 ‘스킬 설치 세부 미확인’은 C20/C21에서 버전 근거를 붙여 보완하며 ASR 정제본을 바꾸지 않는다. HTML에 모든 핵심 결론을 근거와 연결할 구조 확정.\n'
(D/'03_source_map_and_outline.md').write_text(text)
from collections import Counter
print('stage3 PASS',len(c),'claims',len(sources),'sources',dict(Counter(x['status'] for x in c)))
