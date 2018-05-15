#!/usr/bin/env python
#-*-coding:utf-8 -*-
import urllib
import urllib2
import sys,json,time,re,xlwt 
url='http://pages.book.qq.com/fightlist/page.html'
pageno=sys.argv[1]
data={}
def set_style(name,height,color_index,bold=False):
	alignment = xlwt.Alignment() # 创建表格对齐方式
	alignment.horz = xlwt.Alignment.HORZ_CENTER 
	alignment.vert = xlwt.Alignment.VERT_CENTER
	pattern = xlwt.Pattern() # 创建表格填充颜色
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
	pattern.pattern_fore_colour =3 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
	font=xlwt.Font()#为样式创建字体
	font.name=name
	font.height=height
	font.color_index=color_index
	style=xlwt.XFStyle()#初始化样式
	style.alignment=alignment#设置对齐样式为居中对齐
	style.pattern=pattern#添加填充颜色
	style.font=font#设置字体
	return style

def write_excel(cloumn1,x):
	excel=xlwt.Workbook()#创建工作薄
	sheet1=excel.add_sheet(u'书籍信息',cell_overwrite_ok=True)#创建一张工作表
	row1=[u'作者',u'书名',u'热度值',u'最新更新章节',u'更新时间',u'阅读地址',u'故事梗概']#表头信息
	for i in range(0,len(row1)):
		sheet1.write(0,i,row1[i],set_style('Times New RomanTimes',220,42,True))		
	for j in range(0,len(cloumn1)):
		cwidth = sheet1.col(j).width
                if(len(row1[i])*1067)>cwidth:
                        sheet1.col(j).width=(len(row1[j])*1900)
		sheet1.write(x+1,j,cloumn1[j])
		
	excel.save('book.xls')#保存文件
	
data["pageNo"]=pageno
data["pageSize"]=50
urls=url+'?'+urllib.urlencode(data)
#print urls
req=urllib2.Request(urls)
reps=urllib2.urlopen(req)
for line in reps.readlines():
	res=line

res_json=json.loads(res)
books_all_info=res_json['info']['booklist']
excel=xlwt.Workbook()#创建工作薄
sheet1=excel.add_sheet(u'书籍信息',cell_overwrite_ok=True)#创建一张工作表
row1=[u'作者',u'书名',u'热度值',u'最新更新章节',u'更新时间',u'阅读地址',u'故事梗概']#表头信息
for i in range(0,len(row1)):
		cwidth = sheet1.col(i).width
		if(len(row1[i])*1067)>cwidth:
			sheet1.col(i).width=(len(row1[i])*1900)
                sheet1.write(0,i,row1[i],set_style('Times New RomanTimes',220,42,True))
book_key=['author','title','innerValue','newChapter','showTime','bookurl','intro']
for i,j in  enumerate(books_all_info):
	for x,y in enumerate(book_key):
		if x==3:
			j[y]=j[y].replace('<br/>','--')

		sheet1.write(i+1,x,j[y])   
excel.save('book.xls')#保存文件
