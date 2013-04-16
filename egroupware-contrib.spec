%define	name	egroupware-contrib
%define	Name	eGroupWare-contrib
%define egw	egroupware
%define wwwdir	%{_var}/www/%{egw}
%define	version	1.2.107
%define	Version	1.2.107-2
%define release:	8

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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.107-7mdv2011.0
+ Revision: 610346
- rebuild

* Mon Mar 01 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.107-6mdv2010.1
+ Revision: 513137
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise
- use herein documents instead of external source for apache configuration
- no need to prefix apache configuration file with an ordering number
- spec cleanup

* Fri Jan 22 2010 Adam Williamson <awilliamson@mandriva.org> 1.2.107-5mdv2010.1
+ Revision: 494871
- remove egwical and icalsrv directories before %%install
- drop modules that are in the main package now

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.107-4mdv2010.0
+ Revision: 428535
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.107-3mdv2009.0
+ Revision: 244631
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.107-1mdv2008.1
+ Revision: 140728
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 25 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.107-1mdv2008.0
+ Revision: 43801
- 1.2.107-2
- fix deps


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.106-2mdv2007.1
+ Revision: 144976
- 1.2.106-2 (bugfix and maintainance release)
- bunzipped the apache config file
- the changelog was present in the spec file for some reason

* Tue Jan 02 2007 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.106-1mdv2007.1
+ Revision: 103033
- New version, security and bug fixes

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org> 1.2.104-3mdv2007.0
+ Revision: 53312
- rebuild
- Import egroupware-contrib

* Fri Jul 28 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.104-2mdk
- fix duplicate fonts in projects

* Fri Jul 21 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.104-1mdk
- Bug fix

* Mon Jun 12 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2.102-1mdk
- New version, lots of bug fix

* Mon May 22 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2-2.2mdk
- delete .svn directories

* Mon May 22 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.2-2.1mdk
- new version, fix bugs

* Wed Apr 26 2006 Olivier Thauvin <nanardon@mandriva.org> 1.2-1.2mdk
- Fix typo: group and a require was on same line

* Wed Oct 26 2005 Anne Nicolas <anne.nicolas@mandriva.com> 1.2-1.1mdk
- new major version

