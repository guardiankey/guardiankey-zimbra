Name:	guardiankey-dovecot
Version:	1
Release:	0
Summary:	GuardianKey plugin for Dovecot

License:	GNU/GPLv3
URL:		https://guardiankey.io
Source0:	guardiankey-dovecot-1.tar.gz

Requires:	epel-release,python-requests,python-libs,python-devel,python2-crypto,python-configparser,python-pip,gcc,guardiankey-ssh

BuildArch:    noarch
BuildRoot:    %{_tmppath}/%{name}-buildroot

%description
 GuardiaKey is a service that use AI (Artificial Intelligence) for increase security of logins.
 This is a implementation of GuardianKey Auth Securuty Lite, that is free until 10 users. More info:
 https://guardiankey.io/services/guardiankey-auth-security-lite/

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT
cp -R * $RPM_BUILD_ROOT

%post

echo "Updating /etc/guardiankey/gk.conf..."
echo "

[DOVECOT]

dovecot_log = #Dovecot log" >> /etc/guardiankey/gk.conf

echo "imap: /etc/guardiankey/dovecot.deny" >> /etc/hosts.deny
echo "imaps: /etc/guardiankey/dovecot.deny" >> /etc/hosts.deny
echo "pop3: /etc/guardiankey/dovecot.deny" >> /etc/hosts.deny
echo "pop3s: /etc/guardiankey/dovecot.deny" >> /etc/hosts.deny

pip install datefinder


%postun

sed -i '/^[DOVECOT]$/d'  /etc/guardiankey/gk.conf
sed -i '/^dovecot_log$/d'  /etc/guardiankey/gk.conf

sed -i "/dovecot.deny$/d" /etc/hosts.deny

%files
%defattr(-,root,root,-)
/etc/guardiankey/dovecot.deny
/etc/systemd/system/guardiankey-dovecot.service
/usr/lib/guardiankey/gkdovecot.py
/usr/lib/guardiankey/gkparser_dovecot.py
/var/log/guardiankey.log
%exclude /usr/lib/guardiankey/*.pyc
%exclude /usr/lib/guardiankey/*.pyo
