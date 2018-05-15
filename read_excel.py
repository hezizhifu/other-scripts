#!/usr/bin/env python
#-*-coding:utf-8 -*-
import xlrd
import sys
from datetime import datetime,date
reload(sys)
sys.setdefaultencoding( "utf-8" )
def open_xl_files(path):
	Excel_File=xlrd.open_workbook(path)
	sheet_1=Excel_File.sheet_by_name('特殊元宝收益结转')
	data_dict={}
	cols_1=sheet_1.col_values(8)[1:]
	cols_2=sheet_1.col_values(0)[1:]
	for i in cols_1:
		for j in cols_2:
			data_dict[j]=i 
	return data_dict
#if __name__=='__main__':
	#path='/workspace/python/code/20180507_clearing_data.xls'
	#print open_xl_files(path).keys()
	
	
	
