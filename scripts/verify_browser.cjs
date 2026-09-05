const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
(async()=>{
 const url=process.argv[2]||'http://127.0.0.1:8861/';
 const out=path.resolve(process.argv[3]||path.join(__dirname,'../outputs/aside_browser_20260905/05_validation'));fs.mkdirSync(out,{recursive:true});
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const context=await browser.newContext({permissions:['clipboard-read','clipboard-write'],reducedMotion:'reduce'});const page=await context.newPage();
 const errors=[],bad=[];page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});page.on('response',r=>{if(r.status()>=400)bad.push([r.url(),r.status()])});
 const metrics=()=>page.evaluate(()=>({title:document.title,lang:document.documentElement.lang,clientWidth:document.documentElement.clientWidth,scrollWidth:document.documentElement.scrollWidth,images:[...document.images].map(i=>({src:i.getAttribute('src'),width:i.naturalWidth,height:i.naturalHeight,loaded:i.complete&&i.naturalWidth>0})),brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.hash),duplicateIds:[...document.querySelectorAll('[id]')].map(x=>x.id).filter((v,i,a)=>a.indexOf(v)!==i)}));
 await page.setViewportSize({width:1440,height:1000});const response=await page.goto(url,{waitUntil:'networkidle'});const desktop=await metrics();
 await page.screenshot({path:path.join(out,'desktop-hero.png')});await page.screenshot({path:path.join(out,'desktop.png'),fullPage:true});
 const filterCounts={};for(const name of ['보정','미확정','공식 확인','영상 주장','분석/권고','전체']){await page.locator(`[data-filter="${name}"]`).click();filterCounts[name]=await page.locator('.claim:visible').count();}
 await page.locator('[data-filter="미확정"]').click();await page.locator('#setup a[href="#C03"]').first().click();await page.locator('#C03').waitFor({state:'visible',timeout:5000});const hiddenClaimRevealed=await page.locator('#C03').isVisible();
 const prompts={};for(const key of ['research','email','calendar']){
  await page.locator(`[data-prompt="${key}"]`).click();const expected=await page.locator('#prompt-text').textContent();const href=await page.locator('#download-prompt').getAttribute('href');const download=await context.request.get(new URL(href,url).href);
  await page.locator('#copy-prompt').click();await page.waitForFunction(()=>document.getElementById('copy-status').textContent==='작업 명세를 복사했습니다.');const copied=await page.evaluate(()=>navigator.clipboard.readText());
  prompts[key]={title:await page.locator('#prompt-title').textContent(),href,status:download.status(),bodyNonempty:expected.length>100,downloadExact:(await download.text())===expected,clipboardExact:copied===expected,pressed:await page.locator(`[data-prompt="${key}"]`).getAttribute('aria-pressed')};
 }
 const modes={};for(const mode of ['read','full','guard']){await page.locator('#permission-mode').selectOption(mode);modes[mode]=await page.locator('#permission-explanation strong').textContent();}
 const tableModes=await page.locator('#permissions tbody th').allTextContents();
 await page.locator('.check').first().check();const checked=await page.locator('#check-count').textContent();await page.locator('#reset-checks').click();const reset=await page.locator('#check-count').textContent();
 await page.locator('#timeline summary').first().click();const timelineOpens=await page.locator('#timeline details').first().getAttribute('open')!==null;
 await page.locator('#data').screenshot({path:path.join(out,'desktop-data-flow.png')});
 await page.setViewportSize({width:390,height:844});await page.goto(url,{waitUntil:'networkidle'});const mobile=await metrics();await page.screenshot({path:path.join(out,'mobile-hero.png')});await page.screenshot({path:path.join(out,'mobile.png'),fullPage:true});
 await page.locator('.contents a[href="#prompts"]').click();const mobileMenuWorks=(await page.evaluate(()=>location.hash))==='#prompts';await page.locator('[data-prompt="email"]').click();const mobilePrompt=(await page.locator('#download-prompt').getAttribute('href'))==='assets/gmail-draft-prompt.md';
 await page.locator('[data-filter="보정"]').click();const mobileFilter=await page.locator('.claim:visible').count();await page.locator('[data-filter="전체"]').click();
 await page.goto(url);await page.keyboard.press('Tab');const keyboardFirst=await page.evaluate(()=>document.activeElement.textContent);await page.keyboard.press('Enter');const skipWorks=(await page.evaluate(()=>location.hash))==='#main';
 const responsive=[];for(const width of [320,768]){await page.setViewportSize({width,height:900});responsive.push(await metrics());}
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});const np=await nojs.newPage();await np.goto(url);const nojsClaims=await np.locator('.claim:visible').count();const nojsPrompt=await np.locator('#prompt-text').textContent();const nojsDownloads=await np.locator('.all-downloads a').count();
 const expectedCounts={'전체':24,'보정':4,'미확정':4,'공식 확인':10,'영상 주장':5,'분석/권고':1};
 const pass=response.status()===200&&[desktop,mobile,...responsive].every(m=>m.clientWidth===m.scrollWidth&&m.images.every(i=>i.loaded)&&!m.brokenAnchors.length&&!m.duplicateIds.length)&&!errors.length&&!bad.length&&Object.entries(expectedCounts).every(([k,v])=>filterCounts[k]===v)&&Object.values(prompts).every(x=>x.status===200&&x.bodyNonempty&&x.downloadExact&&x.clipboardExact&&x.pressed==='true')&&modes.read.includes('Read only')&&modes.full.includes('Full access')&&modes.guard.includes('Guard')&&tableModes.length===3&&checked==='1 / 7 완료'&&reset==='0 / 7 완료'&&timelineOpens&&mobileMenuWorks&&mobilePrompt&&mobileFilter===4&&skipWorks&&hiddenClaimRevealed&&nojsClaims===24&&nojsPrompt.includes('상품 조사 작업 명세')&&nojsDownloads===3;
 const result={pass,url,http:response.status(),environment:'Playwright + Google Chrome / macOS; reduced motion',desktop,mobile,responsive,interactions:{filterCounts,hiddenClaimRevealed,prompts,modes,tableModes,checked,reset,timelineOpens,mobileMenuWorks,mobilePrompt,mobileFilter,keyboardFirst,skipWorks,nojsClaims,nojsPromptPresent:nojsPrompt.includes('상품 조사 작업 명세'),nojsDownloads},errors,bad};
 fs.writeFileSync(path.join(out,'browser.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));await browser.close();if(!pass)process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1)});
