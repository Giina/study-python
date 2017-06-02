#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import csv
from bs4 import BeautifulSoup

csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['name', 'detail'])

soup =BeautifulSoup(urllib2.urlopen("http://www.japan-osaka.cn/osp/ch/facility/privilege"),'html.parser')
for item in soup.body.select(".free_body"):
	data=['','']
	for tag in item.select('.free_body_left a')[0].contents:
		if tag.name!='span':
			data[0]=tag
	for tag in item.select('.free_body_right > div'):
		for j in tag.children:
			try:
				if j.name=='span':
					data[1]+='\n'
					data[1]+=j.get_text()
				elif j.name=='p':
					for m in j.children:
						if m.name=='img' or m.name=='br':
							print '..'
						else:
							data[1]+='\n'
							data[1]+=m.strip()
				elif j.name=='img' or j.name=='br':
					print '.'
				else:
					data[1]+='\n'
					data[1]+=j.strip()
			except:
				print 'error:',type(j),j.name
	print data[0]
	data[1]=data[1][1:]
	writer.writerows([data])
csvfile.close()