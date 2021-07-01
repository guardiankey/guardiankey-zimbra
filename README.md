# GuardianKey Zimbra plugin

GuardianKey is a service that use AI (Artificial Intelligence) for increase security of logins. More info in https://guardiankey.io

This plugin will read the Zimbra log and send it to the GuardianKey engine. 

You need to install GuardianKey for SSH first. You can more info about Guardiankey for SSH below:

https://github.com/guardiankey/guardiankey-ssh


# Install


## RHEL/CentOS 7

You can install with this command:

\# yum install  https://github.com/guardiankey/guardiankey-zimbra/raw/master/guardiankey-zimbra-1-0.noarch.rpm



## From ".tar.gz" package

You need install python dependencies, example using pip:

\# pip install requests configparser crypto datefinder subprocess

Download and extract the ".tar.gz" package, config file "gk.conf", and execute:

\# python gkzimbra.py &


With your credencials, you should configure /etc/guardiankey/gk.conf. Finally, you starts the guardiankey-dovecot service:

\# systemctl enable --now guardiankey-dovecot



# Licence

This plugin is licencied by GNU/GPLv3.


