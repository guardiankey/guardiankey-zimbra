#!/bin/bash

for ip in $(cat /etc/guardiankey/gk.deny)
do

btime=`echo $ip | cut -d "#" -f2`
unlockh=`date -d "4 hours ago" +%s`
	if [[ $btime > $unlockh ]]
	then
		echo $ip >> /etc/guardiankey/gk.denytmp
	fi

rm -rf /etc/guardiankey/gk.deny
mv /etc/guardiankey/gk.denytmp /etc/guardiankey/gk.deny
