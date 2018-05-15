#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from influxdb import InfluxDBClient
Argv=sys.argv[1]
#变量传值
Conn=InfluxDBClient('192.168.80.202',8086,'grafana','grafana','grafana')#连接并初始化数据库
Res="select mean(usage_percent) from docker_container_mem where container_name=" + "'" + Argv + "'" + " and time>now()- 8h  group by time(60s) fill(none)  order by desc  limit 1"
#查询语句
Data=Conn.query(Res)
#执行查询语句
#print(Res)
for itme in Data:
	print('%.2f'%(itme[0]['mean']))
#迭代打印出所需数据
