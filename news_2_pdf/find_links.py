import os
from bs4 import BeautifulSoup
import yaml
from telegram_util import matchKey
import cached_url

def getItems(soup, news_source):
	if news_source == 'bbc':
		return soup.find_all('a', class_='title-link')
	for x in soup.find_all():
		if not x.attrs:
			continue
		if 'Headline' not in str(x.attrs.get('class')):
			continue
		for y in x.find_all('a'):
			yield y

def getDomain(news_source):
	if news_source == 'bbc':
		return 'https://www.bbc.co.uk'
	return 'https://cn.nytimes.com'

def findLinks(news_source='bbc'):
	source_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'source.yaml')
	with open(source_filename) as f:
		source = yaml.load(f, Loader=yaml.FullLoader)
	soup = BeautifulSoup(cached_url.get(source[news_source]), 'html.parser')
	links = {}
	domain = getDomain(news_source)

	for item in getItems(soup, news_source):
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
			links[name] =  domain +  links[name]
	return links
