from pathlib import Path
from urllib.request import urlopen,Request
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,datetime
P=Path(__file__).resolve().parents[1]/'outputs/aside_browser_20260905';base='https://stmlscd.github.io/codex_utilization/aside-browser-20260905/'
files=[f for f in (P/'04_html_report').rglob('*') if f.is_file()]
def fetch(f):
 rel=str(f.relative_to(P/'04_html_report'));url=base+rel
 with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:b=r.read();status=r.status;ctype=r.headers.get('Content-Type')
 return {'path':rel,'url':url,'status':status,'bytes':len(b),'content_type':ctype,'sha256':hashlib.sha256(b).hexdigest(),'local_equal':b==f.read_bytes()}
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(fetch,files))
with urlopen('https://stmlscd.github.io/codex_utilization/',timeout=45) as r:catalog={'status':r.status,'new_link_present':'./aside-browser-20260905/' in r.read().decode()}
result={'pass':all(x['status']==200 and x['local_equal'] for x in rows) and catalog['status']==200 and catalog['new_link_present'],'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':rows,'catalog':catalog}
(P/'06_publish/http.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));assert result['pass']
