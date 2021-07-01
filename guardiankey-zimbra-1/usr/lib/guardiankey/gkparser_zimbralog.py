import time
import datetime
import json
import datefinder

mode = 'user'
arrayreturn = {}

def parselog(line):
	global mode
	global arrayreturn
	if mode == 'user':
		if 'auth failure' in line:
			date_stamp_found = datefinder.find_dates(line.split('[')[0])
			for match in date_stamp_found:
				try:
					dates =  int(time.mktime(match.timetuple()))
				except:
					dates = int(time.time())
			arrayreturn['time'] = dates
			arrayreturn['event'] = "Failed"
			arrayreturn['method'] = 'SMTP'	
					
			for c in line.split():
				if 'user=' in c:
					arrayreturn['user'] = c.split(']')[0].split('=')[1]
				if 'oip=' in c:
					arrayreturn['ip'] = c.split(';')[2].split('=')[1]
			mode = 'ip'
			return 'next'
			
	else:
		if 'SASL LOGIN authentication failed' in line:
			arrayreturn['ip'] = line.split(':')[4].split(']')[0].split('[')[1]
			mode = 'user'
			return arrayreturn
