#!/usr/bin/env python
#-*-coding:utf-8 -*-
import sys,json,xlwt 
reload(sys)
sys.setdefaultencoding( "utf-8" )
def set_font_style(name,height,color_index,bold):
       # style=xlwt.XFStyle()
        font=xlwt.Font()
        font.name=name
        font.height=height
	font.bold=bold
        font.color_index=color_index
        return font

def set_head_style(name,height,color_index,bold):
	alignment = xlwt.Alignment() # 创建表格对齐方式
	alignment.horz = xlwt.Alignment.HORZ_CENTER 
	alignment.vert = xlwt.Alignment.VERT_CENTER
	pattern = xlwt.Pattern() # 创建表格填充颜色
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
	pattern.pattern_fore_colour =24 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
	style=xlwt.XFStyle()#初始化样式
	style.alignment=alignment#设置对齐样式为居中对齐
	style.pattern=pattern#添加填充颜色
	style.font=set_font_style(name,height,color_index,bold)#设置字体
	return style

def set_col_style(name,height,color_index,bold):
	style=xlwt.XFStyle()
	style.font=set_font_style(name,height,color_index,bold)
	return style
	
def set_col_width(sheet,contents,index,num):
	cwitdth=sheet.col(index).width
	if type(contents[index])!=int:

		if(len(contents[index])*1067)>cwitdth:
			sheet.col(index).width=len(contents[index])*num
			return sheet.col(index).width

def write_save(data):				
	excel=xlwt.Workbook()#创建工作薄
	sheet1=excel.add_sheet(u'股交数据核对',cell_overwrite_ok=True)#创建一张工作表
	row1=[u'母代码',u'基金名称',u'赎回本金',u'赎回收益',u'固定收益',u'总固定收益',u'浮动收益',u'总金额']#表头信息
	it_data=iter(data)
	row_con=(len(data)/8)+1
	change=['C','D','E','F','H']
	index=0
	for i in range(0,len(row1)):
		set_col_width(sheet1,row1,i,710)
                sheet1.write(0,i,row1[i],set_head_style('Times New RomanTimes',260,14,True))
	for row in range(1,row_con):
		for col in range(0,8):
			try:
				set_col_width(sheet1,data,index,510)
				index=index+1
				sheet1.write(row,col,next(it_data).decode('utf-8'),set_col_style(u'微软雅黑',220,13,False))
			except StopIteration:
				break
   		#print x+1,y
	excel.save('clearing.xlsx')#保存文件
	"""wb=openpyxl.load_workbook('clearing.xlsx')
	sheet=wb.get_sheet_by_name('股交数据核对')
	for lg in (2,row_con):
		for keys,values in enumerate(changes):
			cg=sheet[values+str(lg)].value()
			print cg
	"""
