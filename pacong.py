#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib
import urllib2
url='http://www.jinfeibiao.com'
#url='http://114.242.145.101:9099/settlement_trade/login.html'
#urls=url.strip()
value={'loginId':'99001','loginPassword':'wzy123'}
headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
data=urllib.urlencode(value)
req=urllib2.Request(url,data,headers)
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
reps=urllib2.urlopen(req)
page=reps.read()
print page

