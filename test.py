#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import news_2_pdf
import os
import sys

def test():
	pdf_name = news_2_pdf.gen(news_source='bbc')
	os.system('open %s -g' % pdf_name)
	pdf_name = news_2_pdf.gen(news_source='nyt英文')
	pdf_name = news_2_pdf.gen(news_source='nyt')
	pdf_name = news_2_pdf.gen(news_source='bbc英文')
	
	
if __name__=='__main__':
	test()