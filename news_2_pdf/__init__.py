import yaml
from bs4 import BeautifulSoup
from telegram_util import matchKey
import cached_url
import os
import datetime
import sys
from datetime import date
import readee
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-ebook_convert_app')
args = parser.parse_args()
if args.ebook_convert_app:
	ebook_convert_app = args.ebook_convert_app
elif os.name == 'posix':
	ebook_convert_app = '/Applications/calibre.app/Contents/MacOS/ebook-convert'
else:
	ebook_convert_app = 'ebook-convert'

def fact():
	return BeautifulSoup("<div></div>", features="lxml")

def getArticleHtml(name, link, soup):
	if soup.name == '[document]':
		soup = soup.find('div', {'property': 'articleBody'})
	return '''
<html>
	<body>
		<title>%s</title>
		%s
		<div><br/><a href="%s">原文</a></div>
	</body>
</html>
	''' % (name, str(soup), link)

def gen():
	source_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'source.yaml')
	with open(source_filename) as f:
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
	for name in links:
		item = '<a href="%s.html">%s</a>' % (name, name)
		content_list.append(BeautifulSoup(item, 'html.parser'))
		content_list.append(BeautifulSoup('<br/>', 'html.parser'))

	today = date.today().strftime("%y%m%d")
	os.system('rm -rf html_result')	
	os.system('mkdir html_result > /dev/null 2>&1')
	index_html_name = 'html_result/今日新闻%s.html' % today
	with open(index_html_name, 'w') as f:
		f.write(str(soup))

	for name, link in links.items():
		with open('html_result/%s.html' % name, 'w') as f:
			f.write(getArticleHtml(name, link, readee.export(link)))

	os.system('mkdir pdf_result > /dev/null 2>&1')
	pdf_name = 'pdf_result/今日新闻%s.pdf' % today
	# os.system('%s %s %s' % (ebook_convert_app, index_html_name, pdf_name))
		

