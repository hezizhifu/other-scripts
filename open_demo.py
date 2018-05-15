#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:54:58 2017
截止08-13二网发票查询
@author: user
"""
import urllib2
import json
import pandas as pd
# 是否使用代理
enable_proxy = False  # False表示不配置代理，True表示使用代理
http_proxy = {"http": '10.126.3.112:3128'}

# appKey 与 appSecret 配置
appKey1 ="5ece5e1f70ac4e2a97665cc677708e42"
appSecret1 ="ec61e354-b42a-4eaf-96bd-72dbd6ac4492"
# 获取token的url
token_url = "https://open.leshui365.com/getToken?appKey=%s&appSecret=%s" % (appKey1,appSecret1)

#2100162160	#07285871	2017-07-15	72943.59
#invoiceCode = "2100162160"
#invoiceNumber = "07285871"
#billTime = "2017-07-15	"
#invoiceAmount = "72943.59"

### 发票api接口
fapiao_url = "https://open.leshui365.com/api/invoiceInfoForCom"
#invoiceCode = "3100161130"
#invoiceNumber = "14788847"
#billTime = "2016-11-15"
#invoiceAmount = "93096"

def get_token(token_url):
    proxy_support = urllib2.ProxyHandler(http_proxy)
    proxy_dis_support = urllib2.ProxyHandler({})
    # 是否配置代理
    if enable_proxy:
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    else:
        opener = urllib2.build_opener(proxy_dis_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    # 获取最新的token，有效时间两个小时，有效期内不需要重新获取
    req1 = urllib2.Request(token_url)
    f1 = urllib2.urlopen(req1)
    token = f1.read()
    #print token.decode('utf-8')
    f1.close()
    return token

def get_fapiao(invoiceCode, invoiceNumber, billTime, invoiceAmount, token):
    proxy_support = urllib2.ProxyHandler(http_proxy)
    proxy_dis_support = urllib2.ProxyHandler({})
    # 是否配置代理
    if enable_proxy:
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    else:
        opener = urllib2.build_opener(proxy_dis_support, urllib2.HTTPHandler)

    # 参数
    fp_data = {"invoiceCode": invoiceCode,  # 发票代码
               "invoiceNumber": invoiceNumber,  # 发票号码
               "billTime": billTime,  # 开票时间
               "invoiceAmount": invoiceAmount,  # totalAmount
               "token": token # 授权码，token取get_token返回值
               }
    # 提交post请求
    urllib2.install_opener(opener)
    req = urllib2.Request(fapiao_url, json.dumps(fp_data), {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    response = f.read()
#    response1 = json.loads(response)['invoiceResult']
#    response2 = json.loads(response1)['salesName']
#    response=json.loads(response)['invoiceResult']
#    value=json.loads(response)['invoiceResult']
    # 打印 返回值
#    print response.decode('utf-8')
    return response

if __name__ == "__main__":
    # 两小时内不需要执行获取token
    token = json.loads(get_token(token_url))['token']
    #print token
    # 两小时内不需要执行获取token
    invoiceCode="3300172130"
    invoiceNumber="05928720"
    billTime="20171024"
    invoiceAmount="494.34"
##
example=get_fapiao(invoiceCode, invoiceNumber, billTime, invoiceAmount, token)
print example
