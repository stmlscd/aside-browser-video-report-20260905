from html.parser import HTMLParser
from pathlib import Path
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.parts=[]
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style','noscript'):self.skip+=1
 def handle_endtag(self,tag):
  if tag in ('script','style','noscript') and self.skip:self.skip-=1
 def handle_data(self,data):
  if not self.skip and data.strip():self.parts.append(data.strip())
p=Path(__file__).resolve().parents[1]/'outputs/aside_browser_20260905/01_source_inventory/raw/official'
for name in ['home','terms','privacy-policy']:
 x=Parser();x.feed((p/(name+'.html')).read_text());(p/(name+'-readable.txt')).write_text('\n'.join(x.parts)+'\n')
print((p/'privacy-policy-readable.txt').read_text())
