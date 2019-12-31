#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://mp.weixin.qq.com/s?__biz=MjM5NDEwMDI1MA==&mid=2654666539&idx=1&sn=783dcb8c9f97536636b5fc2be5b1c1c4&chksm=bd42ba5e8a353348d75c0bb183b61ffe140a5281ba7097cdf1654e45ca54ba3869a5817e5651&dt_dapp=1#rd',
]

def getFileName(url):
	os.system('mkdir result > /dev/null 2>&1')
	name = [x for x in url.split('/') if x][-1]
	name = [x for x in name.split('.') if x][0]
	return 'result/%s.html' % name

def test():
	if len(sys.argv) > 1:
		mode = sys.argv[1]
	else:
		mode = ''
	if mode == 'open':
		mode = ''
	for url in urls:
		if not mode in url:
			continue
		print('原文：', url)
		name = getFileName(url)
		with open(name, 'w') as f:
			f.write(str(readee.export(url, include_title=True, move_head_photo=True)))
		print('导出：', name)
		if 'open' in str(sys.argv):
			os.system('open ' + name + ' -g')

test()