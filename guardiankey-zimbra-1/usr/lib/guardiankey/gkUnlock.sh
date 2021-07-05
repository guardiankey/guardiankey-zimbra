#!/bin/bash

blocktime=`cat /etc/guardiankey/gk.conf | grep "block_time" | cut -d "=" -f2`

for ip in $(cat /etc/guardiankey/gk.deny)
do

btime=`echo $ip | cut -d "#" -f2`
unlockh=`date -d "$blocktime hours ago" +%s`
	if [[ $btime > $unlockh ]]
	then
		echo $ip >> /etc/guardiankey/gk.denytmp
		iptables -D INPUT -s $ip -j DROP
	fi

rm -rf /etc/guardiankey/gk.deny
mv /etc/guardiankey/gk.denytmp /etc/guardiankey/gk.deny
