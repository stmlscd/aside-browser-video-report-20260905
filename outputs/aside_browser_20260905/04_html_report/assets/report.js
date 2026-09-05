'use strict';
const claims = [...document.querySelectorAll('.claim')];
const filters = [...document.querySelectorAll('[data-filter]')];
function setFilter(value) {
  filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === value)));
  claims.forEach(claim => { claim.hidden = value !== '전체' && claim.dataset.status !== value; });
  document.getElementById('filter-count').textContent = `${claims.filter(claim => !claim.hidden).length}개 주장 표시`;
}
filters.forEach(button => button.addEventListener('click', () => setFilter(button.dataset.filter)));
function revealClaim(id) {
  const target = document.getElementById(id);
  if (target?.classList.contains('claim') && target.hidden) { setFilter('전체'); target.scrollIntoView(); }
}
window.addEventListener('hashchange', () => revealClaim(location.hash.slice(1)));
document.querySelectorAll('a[href^="#C"]').forEach(a => a.addEventListener('click', () => revealClaim(a.hash.slice(1))));
revealClaim(location.hash.slice(1));
const prompts = window.REPORT_PROMPTS;
const promptButtons = [...document.querySelectorAll('[data-prompt]')];
promptButtons.forEach(button => button.addEventListener('click', () => {
  const prompt = prompts[button.dataset.prompt];
  document.getElementById('prompt-title').textContent = prompt.title;
  document.getElementById('prompt-text').textContent = prompt.text;
  document.getElementById('download-prompt').setAttribute('href', `assets/${prompt.file}`);
  document.getElementById('copy-status').textContent = '';
  promptButtons.forEach(b => b.setAttribute('aria-pressed', String(b === button)));
}));
document.getElementById('copy-prompt').addEventListener('click', async () => {
  const element = document.getElementById('prompt-text');
  const status = document.getElementById('copy-status');
  try { await navigator.clipboard.writeText(element.textContent); status.textContent = '작업 명세를 복사했습니다.'; }
  catch { const range = document.createRange(); range.selectNodeContents(element); const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range); status.textContent = '본문을 선택했습니다. 복사 단축키를 누르세요.'; }
});
const modeExplanations = {
  read: ['Read only · 맥락 확인부터', '브라우저·파일 맥락을 살피며 파일을 바꾸지 않는 모드입니다. 작업 폴더에만 접근한다는 뜻으로 해석하지 말고, 웹서비스 동작은 별도 도구 정책과 실제 확인 흐름을 살피세요.'],
  guard: ['Guard · 승인된 폴더부터', '정한 작업 폴더에서 파일 작업을 하고 다른 폴더에 접근할 때 질문하는 기본 모드입니다. 웹서비스에 입력·전송할 범위는 작업 지시와 도구 권한, 실제 확인 동작을 함께 점검하세요.'],
  full: ['Full access · 파일 읽기·쓰기 범위 확대', '컴퓨터 전체의 파일 읽기·쓰기 범위가 열립니다. 비밀번호 원문을 모델에 보여 주거나 모든 메일 전송·결제를 자동 허용한다는 의미는 아닙니다. 도구와 자격증명 정책을 별도로 확인하세요.']
};
document.getElementById('permission-mode').addEventListener('change', event => {
  const [title, text] = modeExplanations[event.target.value];
  document.querySelector('#permission-explanation strong').textContent = title;
  document.querySelector('#permission-explanation p').textContent = text;
});
const checks = [...document.querySelectorAll('.check')];
function updateChecks() { document.getElementById('check-count').textContent = `${checks.filter(x => x.checked).length} / ${checks.length} 완료`; }
checks.forEach(check => check.addEventListener('change', updateChecks));
document.getElementById('reset-checks').addEventListener('click', () => { checks.forEach(x => { x.checked = false; }); updateChecks(); });
