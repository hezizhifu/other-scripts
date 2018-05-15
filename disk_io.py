#!/usr/bin/env python
#-*- coding:utf-8 -*-
import psutil
import sys
if sys.argv<3:
	sys.exit()

disk_name,disk_oper=sys.argv[1],sys.argv[2]
def get_disk_io_info():
	disk_dict={}
	disk_io=psutil.disk_io_counters(perdisk=True)
	disk_dict["read"]=disk_io[disk_name][0]
	disk_dict["write"]=disk_io[disk_name][1]
	disk_dict["read_bytes"]=disk_io[disk_name][2]
	disk_dict["write_bytes"]=disk_io[disk_name][3]
	return disk_dict
print get_disk_io_info()[disk_oper]
	
