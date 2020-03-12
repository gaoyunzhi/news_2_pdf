#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'news_2_pdf'

import os
from .find_links import findLinks
from .article import getArticleHtml
from .index import getIndexHtml
from datetime import date
from telegram_util import cleanFileName

if os.name == 'posix':
	ebook_convert_app = '/Applications/calibre.app/Contents/MacOS/ebook-convert'
else:
	ebook_convert_app = 'ebook-convert'

def gen(news_source='bbc', ebook_convert_app=ebook_convert_app, additional_setting='', filename_suffix = ''):
	filename = '%s_%s新闻' % (date.today().strftime("%m%d"), news_source.upper()) + filename_suffix

	os.system('rm -rf html_result')	
	os.system('mkdir html_result > /dev/null 2>&1')

	links = []
	for link, name in findLinks(news_source):
		html = getArticleHtml(name, link, filename + '.html')
		if html:
			name = cleanFileName(name)
			with open('html_result/%s.html' % name, 'w') as f:
				f.write(html)
			links.append(name)
			if len(links) > 10:
				break

	index_html_name = 'html_result/%s.html' % filename
	with open(index_html_name, 'w') as f:
		f.write(getIndexHtml(news_source, links))

	os.system('mkdir pdf_result > /dev/null 2>&1')
	pdf_name = 'pdf_result/%s.pdf' % filename
	command = '%s %s %s %s > /dev/null 2>&1'
	os.system(command % (ebook_convert_app, index_html_name, pdf_name, additional_setting))
	return pdf_name
		

