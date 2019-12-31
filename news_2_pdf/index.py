from datetime import date
from bs4 import BeautifulSoup

def getIndexHtml(news_source, links):
	today = date.today().strftime("%y%m%d")

	index_html = '''
<html>
   <body>
     <h1>今日新闻 %s %s</h1>
     <p style="text-indent:0pt">
     </p>
   </body>
</html>
	''' % (news_source, today)

	soup = BeautifulSoup(index_html, 'html.parser')
	content_list = soup.find('p')
	for name in links:
		item = '<a href="%s.html">%s</a>' % (name, name)
		content_list.append(BeautifulSoup(item, 'html.parser'))
		content_list.append(BeautifulSoup('<br/><br/>', 'html.parser'))
	return str(soup)