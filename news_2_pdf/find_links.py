import os
from bs4 import BeautifulSoup
import yaml
from telegram_util import matchKey
import cached_url

def getItems(soup, news_source):
	for x in soup.find_all('a', class_='title-link'):
		yield x
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
	source = {
		'bbc': 'https://www.bbc.com/zhongwen/simp',
		'nyt': 'https://cn.nytimes.com/'
	}
	soup = BeautifulSoup(cached_url.get(source[news_source]), 'html.parser')
	links = {}
	domain = getDomain(news_source)
	link_set = set()
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
		if links[name] in link_set:
			del links[name]
		else:
			link_set.add(links[name])
	return links
