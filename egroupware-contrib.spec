%define	name	egroupware-contrib
%define	Name	eGroupWare-contrib
%define egw	egroupware
%define wwwdir	%{_var}/www/%{egw}
%define	version	1.2.107
%define	Version	1.2.107-2
%define	release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Contrib modules for egroupware suite
License:	GPL+
Group:		System/Servers
URL:		http://www.egroupware.org/
Source0:	%{Name}-%{Version}.tar.bz2
%if %mdkversion < 201010
Requires(post):   rpm-helper
Requires(postun):   rpm-helper
%endif
Requires:	apache-mod_php
Requires:	php-xml
Requires:	php-gd
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
eGroupWare is a web-based groupware suite written in PHP. This -contrib 
package provides unsupported (and often obsolete and broken) plugins.

%package backup
Summary:	The eGroupWare backup application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-backup
Provides:	egroupware-backup

%description backup
An online configurable backup app to store data offline. 
Can store files in zip, tar.gz and tar.bz2 on the local machine 
or Remote via FTP, SMBMOUNT or NFS 

%package browser
Summary:	The eGroupWare browser application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}

%description browser
The eGroupWare browser application

%package chatty
Summary:	The eGroupWare chat application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}

%description chatty
Direct dialogue for egroupware.

%package comic
Summary:	The eGroupWare comic application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-comic
Provides:	egroupware-comic

%description comic
This application display comic strips.

%package email
Summary:	The eGroupWare email application
Group:		System/Servers
Requires:	%{name}-addressbook = %{version}-%{release}
Obsoletes:	egroupware-email
Provides:	egroupware-email

%description email
AngleMail for eGroupWare at www.anglemail.org is an Email reader with multiple
accounts and mailbox filtering. Also Anglemail support IMAP, IMAPS, POP3 and
POP3S accounts.

%package filescenter
Summary:	The eGroupWare filescenter application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}

%description filescenter
This is the filescenter app for eGroupWare.

%package forum
Summary:	The eGroupWare forum application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-forum
Provides:	egroupware-forum

%description forum
This is the forum app for eGroupWare.

%package ftp
Summary:	The eGroupWare ftp application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-ftp
Provides:	egroupware-ftp

%description ftp
This is the ftp app for eGroupWare.

%package fudforum
Summary:	The eGroupWare fudforum application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-fudforum
Provides:	egroupware-fudforum

%description fudforum
This is the fudforum app for eGroupWare.

%package headlines
Summary:	The eGroupWare headlines application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-headlines
Provides:	egroupware-headlines

%description headlines
This is the headlines app for eGroupWare.

%package jinn
Summary:	The eGroupWare jinn application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-jinn
Provides:	egroupware-jinn

%description jinn
The jinn app is a multi-site, multi-database, multi-user/-group, database
driven Content Management System written in and for the eGroupWare Framework.

%package messenger
Summary:	The eGroupWare messenger application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-messenger
Provides:	egroupware-messenger

%description messenger
This is the messenger app for eGroupWare.
bsoletes:	egroupware-phpbrain
Provides:	egroupware-phpbrain

%package phpldapadmin
Summary:	The eGroupWare phpldapadmin application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-phpldapadmin
Provides:	egroupware-phpldapadmin

%description phpldapadmin
This is the phpldapadmin app for eGroupWare.

%package projects
Summary:	The eGroupWare projects application
Group:		System/Servers
Requires:	%{name}-addressbook = %{version}-%{release}
Obsoletes:	egroupware-projects
Provides:	egroupware-projects

%description projects
This is the projects app for eGroupWare.

%package skel
Summary:        The eGroupWare skel application
Group:          System/Servers
Requires:       %{egw} >= %{version}-%{release}
Obsoletes:	egroupware-skel
Provides:	egroupware-skel

%description skel
This is the skel app for eGroupWare.

%package soap
Summary:        The eGroupWare soap application
Group:          System/Servers
Requires:       %{egw} >= %{version}-%{release}

%description soap
This is the soap app for eGroupWare.

%package stocks
Summary:	The eGroupWare stocks application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-stocks
Provides:	egroupware-stocks

%description stocks
This is the stocks app for eGroupWare.

%package switchuser
Summary:        The eGroupWare switchuser application
Group:          System/Servers
Requires:       %{egw} >= %{version}-%{release}

%description switchuser
This is the switchuser app for eGroupWare.

%package tts
Summary:	The eGroupWare tts application
Group:		System/Servers
Requires:	%{egw} >= %{version}-%{release}
Obsoletes:	egroupware-tts
Provides:	egroupware-tts

%description tts
This is the tts app for eGroupWare.

%package xmlrpc
Summary:        The eGroupWare xmlrpc application
Group:          System/Servers
Requires:       %{egw} >= %{version}-%{release}

%description xmlrpc
This is the xmlrpc app for eGroupWare.

%prep
%setup -q -n %{egw}
# cleanup
find . -type d -name CVS | xargs rm -rf
find . -type f -name *.old -o -name *.backup | xargs rm -f
find . -type f -empty | xargs rm -f
find . -type f | xargs chmod 644
find . -name .svn | xargs rm -rf


# delete duplicate fonts
find . -type d -name ttf-bitstream-vera-1.10|xargs rm -rf

# remove egwical and icalsrv (they're in the main package now)
rm -rf egwical/ icalsrv/

%build

%install
rm -rf  %{buildroot}

# install files
install -d -m 755 %{buildroot}%{wwwdir}
cp -aRf * %{buildroot}%{wwwdir}

# post-install cleanup
rm -rf %{buildroot}%{wwwdir}/doc 
rm -rf %{buildroot}%{wwwdir}/*/doc 
rm -f %{buildroot}%{wwwdir}/backup/README
rm -f %{buildroot}%{wwwdir}/felamimail/{COPYING,Changelog,README,TODO}
rm -f %{buildroot}%{wwwdir}/jinn/{CHANGELOG,COPYING,INSTALL,LICENSE,README,TODO}
rm -f %{buildroot}%{wwwdir}/phpldapadmin/{INSTALL,LICENSE,VERSION}
rm -rf %{buildroot}%{wwwdir}/infolog/debian
rm -rf %{buildroot}%{wwwdir}/jinn/quixplorer_2_3
# doc cleanup
rm -f doc/Makefile
rm -rf doc/rpm-build

# remove .htaccess files
find %{buildroot}%{wwwdir} -name .htaccess -exec rm -f {} \;

# modify shell bang for perl scripts
find %{buildroot}%{wwwdir} -name '*.pl' -exec perl -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|g' {} \;
find %{buildroot}%{wwwdir} -name '*.py' -exec perl -pi -e 's|/usr/local/bin/python|/usr/bin/python|g' {} \;

# fix right on scripts
find %{buildroot}%{wwwdir} -name '*.pl' -exec chmod 755 {} \;
find %{buildroot}%{wwwdir} -name '*.py' -exec chmod 755 {} \;

# apache configuration for fudforum
install -d -m 755 %{buildroot}%{_webappconfdir}
cat > %{buildroot}%{_webappconfdir}/%{egw}-fudforum.conf <<EOF
<Directory /var/www/egroupware/fudforum/setup/base>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/sql>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/src>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/thm>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/cache>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/scripts>
    Deny from all
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/www_root>

    php_admin_value output_buffering 16000
    php_admin_value variables_order GPCS
    php_admin_value implicit_flush 0
    php_admin_value register_globals 0
    php_admin_value register_argc_argv 0
    php_admin_value magic_quotes_gpc 0
    php_admin_value session.use_trans_sid 0
</Directory>

<Directory /var/www/egroupware/fudforum/setup/base/include>
    Deny from all
</Directory>
EOF

%post fudforum
%if %mdkversion < 201010
%_post_webapp
%endif

%postun fudforum
%if %mdkversion < 201010
%_postun_webapp
%endif

%clean
rm -rf %{buildroot}

%files backup
%defattr(-,root,root)
%doc backup/README
%{wwwdir}/backup

%files browser
%defattr(-,root,root)
%doc browser/doc/*
%{wwwdir}/browser

%files chatty
%defattr(-,root,root)
%{wwwdir}/chatty

%files comic
%defattr(-,root,root)
%doc comic/doc/*
%{wwwdir}/comic

%files email
%defattr(-,root,root)
%doc email/addressbook-js.changelog.txt email/doc/*
%{wwwdir}/email

%files filescenter
%defattr(-,root,root)
%doc filescenter/doc/*
%{wwwdir}/filescenter

%files forum
%defattr(-,root,root)
%doc forum/README 
%{wwwdir}/forum

%files ftp
%defattr(-,root,root)
%doc ftp/doc/*
%{wwwdir}/ftp

%files fudforum
%defattr(-,root,root)
%{wwwdir}/fudforum
%config(noreplace) %{_webappconfdir}/%{egw}-fudforum.conf

%files headlines
%defattr(-,root,root)
%{wwwdir}/headlines

%files jinn
%defattr(-,root,root)
%doc jinn/{CHANGELOG,COPYING,INSTALL,LICENSE,README,TODO} jinn/doc/*
%{wwwdir}/jinn

%files messenger
%defattr(-,root,root)
%doc messenger/doc/*
%{wwwdir}/messenger

%files phpldapadmin
%defattr(-,root,root)
%doc phpldapadmin/{LICENSE,VERSION}
%{wwwdir}/phpldapadmin

%files projects
%defattr(-,root,root)
%doc projects/doc/*
%{wwwdir}/projects

%files skel
%defattr(-,root,root)
%doc skel/doc/*
%{wwwdir}/skel

%files soap
%defattr(-,root,root)
%doc soap/README.txt
%{wwwdir}/soap

%files stocks
%defattr(-,root,root)
%doc stocks/doc/*
%{wwwdir}/stocks

%files switchuser
%defattr(-,root,root)
%doc switchuser/CHANGELOG switchuser/doc/*
%{wwwdir}/switchuser

%files tts
%defattr(-,root,root)
%doc tts/doc/*
%{wwwdir}/tts

%files xmlrpc
%defattr(-,root,root)
%doc xmlrpc/NOTE xmlrpc/doc/*
%{wwwdir}/xmlrpc
