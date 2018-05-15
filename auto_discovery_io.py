#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import json
r=r'[s|v]d[a-z][0-9]$'
ctr=re.compile(r)
disk_info=[]
disk_dict={}
with open("/proc/partitions") as f:
	for i in f:
		if ctr.search(i):
			disk_info.append({"{#DISKNAME}":i.split()[-1]})
disk_dict["data"]=disk_info
print json.dumps(disk_dict)
