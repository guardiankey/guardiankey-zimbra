Name:	guardiankey-zimbra
Version:	1
Release:	1
Summary:	GuardianKey plugin for Zimbra

License:	GNU/GPLv3
URL:		https://guardiankey.io
Source0:	guardiankey-zimbra-1.tar.gz

Requires:	epel-release,python-requests,python-libs,python-devel,python2-crypto,python-configparser,python-pip,gcc,guardiankey-ssh

BuildArch:    noarch
BuildRoot:    %{_tmppath}/%{name}-buildroot

%description
 GuardiaKey is a service that use AI (Artificial Intelligence) for increase security of logins.

 https://guardiankey.io/services/guardiankey-auth-security-lite/

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT
cp -R * $RPM_BUILD_ROOT

%post
if [ $1 == 2];then

echo '' > /etc/hosts.deny
echo "#tempo de bloqueio em horas
block_time=8" >> /etc/guardiankey/gk.conf
else
echo "

[ZIMBRA]

zimbra_log = #Dovecot log
mailbox_log = #Mailbox log

#tempo de bloqueio em horas
block_time=8
" >> /etc/guardiankey/gk.conf

fi


pip install datefinder


%postun

sed -i '/^[ZIMBRA]$/d'  /etc/guardiankey/gk.conf
sed -i '/^zimbralog$/d'  /etc/guardiankey/gk.conf

sed -i "/dovecot.deny$/d" /etc/hosts.deny

%files
%attr(0644, root, root) "/etc/guardiankey/gk.deny"
%attr(0644, root, root) "/etc/systemd/system/guardiankey-zimbra.service"
%attr(0644, root, root) "/usr/lib/guardiankey/gkUnlock.sh"
%attr(0644, root, root) "/usr/lib/guardiankey/gk_pop_Imap.py"
%attr(0644, root, root) "/usr/lib/guardiankey/gkparser_popimaplog.py"
%attr(0644, root, root) "/usr/lib/guardiankey/gkparser_zimbralog.py"
%attr(0644, root, root) "/usr/lib/guardiankey/gkzimbra.py"
%attr(0644, root, root) "/var/log/guardiankey.log"

%exclude /usr/lib/guardiankey/*.pyc
%exclude /usr/lib/guardiankey/*.pyo
