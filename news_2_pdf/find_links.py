import link_extractor

SOURCE = {
	'bbc': 'https://www.bbc.com/zhongwen/simp',
	'nyt': 'https://cn.nytimes.com',
	'bbc英文': 'https://www.bbc.co.uk',
	'nyt英文': 'https://www.nytimes.com',
}

DOMAIN = {
	'bbc': 'https://www.bbc.co.uk',
}

def findLinks(news_source='bbc'):
	return link_extractor.getLinks(SOURCE[news_source], DOMAIN.get(news_source))