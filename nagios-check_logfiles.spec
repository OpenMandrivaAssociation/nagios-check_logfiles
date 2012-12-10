%define name	nagios-check_logfiles
%define version	2.5.6.1
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check log files for specific patterns
Group:		Networking/Other
License:	BSD
URL:		http://www.consol.com/opensource/nagios/check-logfiles
Source:     http://www.consol.com/fileadmin/opensource/Nagios/check_logfiles-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
check_logfiles is a Plugin for Nagios which scans log files for specific
patterns.

%prep
%setup -q -n check_logfiles-%{version}

%build
%configure2_5x --build=i586-mandriva-linux-gnu --libexec=%{_libdir}/nagios/plugins
%make


%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_logfiles



%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.6.1-2mdv2011.0
+ Revision: 620460
- the mass rebuild of 2010.0 packages

* Mon Jun 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.6.1-1mdv2010.0
+ Revision: 386202
- new version

* Mon Feb 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.5.1-1mdv2009.1
+ Revision: 336675
- update to new version 2.5.5.1

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1.8-1mdv2009.1
+ Revision: 297976
- new version

* Thu Jun 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1.3-2mdv2009.0
+ Revision: 229283
- this is not a noarch package

* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1.3-1mdv2009.0
+ Revision: 229039
- import nagios-check_logfiles


* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1.3-1mdv2009.0
- first mdv package
