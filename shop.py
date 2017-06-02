#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import csv
from bs4 import BeautifulSoup

csvfile = file('shop.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['no','name'])

soup =BeautifulSoup(urllib2.urlopen("http://www.japan-osaka.cn/osp/ch/facility/shop"),'html.parser')
data=['','']
for item in soup.body.select(".tempo_body_left"):
	text=item.a.get_text().strip()
	print text[2:3]
	if text[2:3]==' ':
		data[0]=text[:2]
		data[1]=text[2:].strip()
	else:
		data[0]=text[:3]
		data[1]=text[3:].strip()
	writer.writerows([data])
for item in soup.body.select(".tempo_body_right"):
	text=item.a.get_text().strip()
	if text[2:3]==' ':
		data[0]=text[:2]
		data[1]=text[2:].strip()
	else:
		data[0]=text[:3]
		data[1]=text[3:].strip()
	writer.writerows([data])

csvfile.close()