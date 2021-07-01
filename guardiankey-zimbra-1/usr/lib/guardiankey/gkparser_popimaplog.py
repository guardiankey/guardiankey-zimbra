import time
import datetime
import json
import datefinder

def parselog(line):
	if 'Pop3SSLServer' in line:
		if 'auth' in line:
			date_stamp_found = datefinder.find_dates(line.split('<')[0])
			arrayreturn = {}
			for match in date_stamp_found:
				try:
					dates =  int(time.mktime(match.timetuple()))
				except:
					dates = int(time.time())
			arrayreturn['time'] = dates
			
			if 'authenticated' in line:
				arrayreturn['event'] = "Accepted"
			else:
				arrayreturn['event'] = "Failed"
			arrayreturn['method'] = 'POP3'	
				
			for c in line.split():
				if 'name=' in c:
					arrayreturn['user'] = c.split(';')[0].split('=')[1]
				if 'oip=' in c:
					arrayreturn['ip'] = c.split(';')[2].split('=')[1]
			return arrayreturn
		
	else:
		if 'ImapSSLServer' in line:
			if 'auth' in line:
				date_stamp_found = datefinder.find_dates(line.split(',')[0])
				arrayreturn = {}
				for match in date_stamp_found:
					try:
						dates =  int(time.mktime(match.timetuple()))
					except:
						dates = int('999999')
				arrayreturn['time'] = dates
				arrayreturn['method'] = 'IMAP'	

				if 'authenticated' in line:
					arrayreturn['event'] = "Accepted"
					for c in line.split():
						if 'name=' in c:
							arrayreturn['user'] = c.split(';')[0].split('=')[1]
						if 'oip=' in c:
							arrayreturn['ip'] = c.split(';')[2].split('=')[1]
				else:
					arrayreturn['event'] = "Failed"
					for c in line.split():
						print c
						if '@' in c:
							arrayreturn['user'] = c.split('[')[1].split(']')[0]
						if 'oip=' in c:
							arrayreturn['ip'] = c.split(';')[1].split('=')[1]
					
				return arrayreturn

