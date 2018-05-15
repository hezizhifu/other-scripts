#!/usr/bin/env python
import urllib
import urllib2
import sys,json,time,re
url='http://pages.book.qq.com/fightlist/page.html'
pageno=sys.argv[1]
data={}	
author=u'\"author\":\"(.+?)\"'
author_re=re.compile(author)
data["pageNo"]=pageno
data["pageSize"]=50
urls=url+'?'+urllib.urlencode(data)
headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
#print urls
req=urllib2.Request(urls)
reps=urllib2.urlopen(req)
for line in reps.readlines():
	res=line.decode('unicode_escape')
	author_ress=author_re.findall(res)
	print author_ress
        for L in author_ress:
		print L	
	
