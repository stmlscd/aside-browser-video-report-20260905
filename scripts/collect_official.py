from pathlib import Path
from urllib.request import urlopen,Request
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,datetime
P=Path(__file__).resolve().parents[1]/'outputs/aside_browser_20260905/01_source_inventory/raw/official';P.mkdir(parents=True,exist_ok=True)
items=[(x,'https://docs.aside.com/help/'+x+'.md') for x in ['get-started','subscription','browser-basics','tasks','side-panel','automation','memory','password-manager','passwords','ai','privacy','security','troubleshooting','developers']]+[('home','https://aside.com/'),('privacy-policy','https://aside.com/policy/privacy'),('terms','https://aside.com/policy/terms'),('docs-index','https://docs.aside.com/llms.txt')]
def fetch(pair):
 slug,url=pair
 with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:data=r.read();status=r.status;final=r.url;ct=r.headers.get('content-type','')
 ext='.html' if 'html' in ct else '.md';name=slug+ext;(P/name).write_bytes(data)
 return dict(slug=slug,url=url,final_url=final,file=name,http=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(fetch,items))
(P/'fetch-log.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
for r in rows:print(r['file'],r['http'],r['bytes'])
