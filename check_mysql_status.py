#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from influxdb import InfluxDBClient
Conn=InfluxDBClient('192.168.80.202',8086,'grafana','grafana','grafana')#连接并初始化数据库
Zbx_Items=['max_used_connections','commands_select','commands_delete','commands_update','commands_insert','threads_connected ','connections','aborted_clients','aborted_connects','bytes_received','bytes_sent','QPS','threads_running','slow_queries','innodb_data_read','innodb_data_write','open_files']
Argv=sys.argv[1]
def check_argv():

	if Argv not in Zbx_Items:
        	return Zbx_Items
		sys.exit()
	else:
		return 1

def check_mysql():
	
	qs='select mean('+ Argv + ')from mysql where time <= now() AND time >= now()- 60s'
	res=Conn.query(qs)
	return res
	#return qs

if (check_argv()==1):
	for items in check_mysql():
		 print('%.2f'%(items[0]['mean']))
else:
	print 'you should choice last one in:'
	print check_argv()



	
	
	

