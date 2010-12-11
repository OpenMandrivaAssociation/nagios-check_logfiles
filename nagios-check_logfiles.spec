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

