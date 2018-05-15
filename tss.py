#!/usr/bin/env python
#-*-coding:utf-8 -*-
import tushare as ts
import pandas as pd
years=[2012,2013,2014,2015,2016]
codes=['000921','002032','002035','002242','002290','002403','000418','600481','600690','600839','600854ST','600983','000651','000527','000016']
frames=[]
data12=ts.get_report_data(years[0],4)
data13=ts.get_report_data(years[1],4)
data14=ts.get_report_data(years[2],4)
data15=ts.get_report_data(years[3],4)
data16=ts.get_report_data(years[4],4)
frames=[data12,data13,data14,data15,data16]
res=pd.concat(frames)
print res

	
