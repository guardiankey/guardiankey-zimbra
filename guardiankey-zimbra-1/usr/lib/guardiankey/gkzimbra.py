import guardiankey
import gkparser_zimbralog
import sys
import json
import configparser
import datetime
import tail
import time

configp = configparser.ConfigParser()
configp.read('/etc/guardiankey/gk.conf')
GKconfig = configp['REGISTER']
GKzimbra = configp['ZIMBRA']

def callback_f(line):
	send(line)

def doAction(ip):
    now = datetime.datetime.now()
    blockdate = str(int(time.time()))
    ipline = str(ip)+'#'+blockdate+'\n'
    f = open('/etc/guardiankey/gk.deny','a')
    f.write(ipline)
    f.close()
    cmd = "iptables -I INPUT -s {} -j DROP".format(ip)
    subprocess.check_output(cmd, shell=True)
    
def send(line):
    global GKconfig
    jlog = gkparser_zimbralog.parselog(line)
    if jlog != None and jlog <> 'next':
		if jlog['user'] <> 'xNull':
			if jlog['event'] == "Accepted":
				loginfailed = 0
			else:
				loginfailed = 1
			result = guardiankey.checkaccess(jlog['user'],jlog['ip'],jlog['time'],loginfailed,'Authentication')
			if result['response'] == 'BLOCK' and GKconfig['block'] == '1':
				f = open('/var/log/guardiankey.log','a')
				f.write(str(json.dumps(result)))
				f.close()
				doAction(jlog['ip'])
    return None
    
while True:
    if GKconfig['key'] is None:
        print "You need configure /etc/guardiankey/gk.conf!"
        quit()
    t = tail.Tail(GKzimbra['zimbra_log'])
    t.register_callback(callback_f)
    t.follow(s=1)
