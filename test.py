#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import news_2_pdf
import os
import sys

def test():
	additional_setting = '--paper-size b6 --pdf-page-margin-left 15 ' + \
		'--pdf-page-margin-right 15 --pdf-page-margin-top 15 ' + \
		'--pdf-page-margin-bottom 15'
	pdf_name = news_2_pdf.gen(news_source='bbc', 
		filename_suffix='_大字版', additional_setting=additional_setting)
	os.system('open %s -g' % pdf_name)
	
	
if __name__=='__main__':
	test()