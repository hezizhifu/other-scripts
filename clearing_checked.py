#!/usr/bin/env python
#-*- coding:utf8-*-*
"""
@author:李坚
@time:2018/04/27
@func:将日常清算数据自动对账形成报表文件
"""
import sys
import math
import requests
import time
import random
import pytesseract
from PIL import Image
import encrypt_passwd 
from bs4 import BeautifulSoup
import read_excel
import write_excel
from datetime import date,datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )
"""
#生成随机数ran_num,
#这个随机数作为post数据的参数,和AES加密的密钥
"""
files_path='/workspace/python/code/'
agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
headers={
"User-Agent":agent
}
#ran_num=random.randrange(99,9999)
def get_check_code(session):
	#保存的验证码图片名称
	png_name='code_'+str(ran_num)+'.png'
	#保存验证码图片的路径
	code_url='http://114.242.145.101:9099/settlement_trade/captcha.html?id='+str(ran_num)
	get_code=session.get(code_url)
	if get_code.status_code==200:
		img_code=get_code.content
		with open(files_path+png_name,'w') as codefile:
			codefile.write(img_code)
		try:
			image =Image.open(files_path+png_name)
			code =pytesseract.image_to_string(image)
		except:
			print("图片验证码解析失败")
  	else:
		print ('网站无法访问!!!')
	return code
def login_sys(check_code,session,enc_pd):
	post_data={
	"id":ran_num,
	"loginId":"99003",
	"loginPassword":enc_pd,
	"captcha":check_code
	}
	post_url='http://114.242.145.101:9099/settlement_trade/login.html'
	login_page=session.post(post_url,data=post_data,headers=headers)
	login_code=login_page.status_code
	return login_code
	
def save_session():
	pass
def check_data(session,begin_date,endDate,relate_code):
	post_data={
	"pageNo":"0",
	"totalRowsAmount":"0",
	"download":"false",
	"begin_date":begin_date,
	"endDate":endDate,
	"action_in":"2",
	"relate_code":relate_code
	}
	post_url='http://114.242.145.101:9099/settlement_trade/alert/getTotalStatistic.html'
	res_data=session.post(post_url,data=post_data,headers=headers)
	res=res_data.text
	bs=BeautifulSoup(res,'lxml')
	re=bs.find('tbody').find_all('td')
	rest=[]
	for i in re:
		#tmp=i.repalce('<td>','')
		 tmp=str(i.get_text())
		 rest.append(tmp)
	return rest
	#for i in range(0,len(re)):
	#	return re[-i].get_text()
	#return re
def save_clr_file(session,endDate):
	get_url='http://114.242.145.101:9099/settlement_trade/alert/settleDataOut.html'
	res_data=session.get(get_url,headers=headers)
	res=res_data.content
	file_name=endDate+'_clearing_data.xls'
	with open(files_path+file_name,'wb') as xlsfile:
		xlsfile.write(res)
	try:
    		f =open(files_path+file_name)
   		f.close()
	except IOError:
    		print "File is not accessible."
	absloute_file=files_path+file_name
	return absloute_file
if __name__=='__main__':
	ran_num=math.floor(random.random()*10000+1)
        passwd='lj123'
        key=str(ran_num)
        aes=encrypt_passwd.AESCipher(key)
        en=aes.encrypt(passwd)
	session=requests.Session()
	times=datetime.now()
	endDate=times.strftime('%Y%m%d')
        login_sys(get_check_code(session),session,en)
	relate_code=''
	r_date=read_excel.open_xl_files(save_clr_file(session,endDate)).values()
	r_code=read_excel.open_xl_files(save_clr_file(session,endDate)).keys()
	begin_date=r_date[1].replace('-','')
	print begin_date
	print endDate
	for i in range(0,len(r_code)):
		relate_code+=''.join(r_code[i])+','
	data=check_data(session,begin_date,endDate,relate_code)
	write_excel.write_save(data)
	print data
