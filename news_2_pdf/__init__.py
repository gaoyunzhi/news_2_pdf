#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'news_2_pdf'

import os
import argparse
from .find_links import findLinks
from .article import getArticleHtml
from .index import getIndexHtml
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument('-ebook_convert_app')
args = parser.parse_args()
if args.ebook_convert_app:
	ebook_convert_app = args.ebook_convert_app
elif os.name == 'posix':
	ebook_convert_app = '/Applications/calibre.app/Contents/MacOS/ebook-convert'
else:
	ebook_convert_app = 'ebook-convert'

def gen(news_source='bbc', ebook_convert_app=ebook_convert_app):
	links = findLinks(news_source)
	filename = '今日新闻%s%s' % (news_source, date.today().strftime("%y%m%d"))

	os.system('rm -rf html_result')	
	os.system('mkdir html_result > /dev/null 2>&1')

	for name, link in links.copy().items():
		html = getArticleHtml(name, link, filename + '.html')
		if html:
			with open('html_result/%s.html' % name, 'w') as f:
				f.write(html)
		else:
			del links[name]

	index_html_name = 'html_result/%s.html' % filename
	with open(index_html_name, 'w') as f:
		f.write(getIndexHtml(news_source, links))

	os.system('mkdir pdf_result > /dev/null 2>&1')
	pdf_name = 'pdf_result/%s.pdf' % filename
	os.system('%s %s %s' % (ebook_convert_app, index_html_name, pdf_name))
	os.system('open %s -g' % pdf_name)
	return pdf_name
		

