#!/usr/bin/env python3
#-*- coding:utf-8 -*-
file=open('/workspace/python/code/file.txt','r')
while True:
	char=file.readline()
	if not char: break
	print(char,end='..\n')
	
	

