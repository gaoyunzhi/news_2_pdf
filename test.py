#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import news_2_pdf
import os
import sys

def test(source):
	pdf_name = news_2_pdf.gen(news_source=source)
	os.system('open %s -g' % pdf_name)
	
	
if __name__=='__main__':
	test('bbc英文')
	# test('nyt英文')
	# test('nyt')