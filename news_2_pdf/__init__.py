import yaml
from bs4 import BeautifulSoup
from telegram_util import matchKey
import cached_url
import os
import datetime

with open('source.yaml') as f:
	source = yaml.load(f, Loader=yaml.FullLoader)

soup = BeautifulSoup(cached_url.get(source['bbc']), 'html.parser')
links = {}
for item in soup.find_all('a', class_='title-link'):
	if not item.text or not item.text.strip():
		continue
	name = item.text.strip()
	if matchKey(name, ['\n', '视频']):
		continue
	if len(name) < 5: # 导航栏目
		continue
	if len(links) > 10 and '代理服务器' not in name:
		continue
	links[name] = item['href'].strip()
	if not '://' in links[name]:
		links[name] = 'https://www.bbc.co.uk' +  links[name]

os.system('rm html_result')	
os.system('mkdir html_result > /dev/null 2>&1')

index_html = '''
<html>
   <body>
     <h1>Table of Contents</h1>
     <p style="text-indent:0pt">
     </p>
   </body>
</html>
'''
soup = BeautifulSoup(index_html, 'html.parser')
content_list = soup.find('p')
