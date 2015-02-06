# This package is de-facto noarch, but we need to install files to arch-specific places
%define debug_package %{nil}

Name:		nagios-check_logfiles
Version:	2.5.6.1
Release:	4
Summary:	Check log files for specific patterns
Group:		Networking/Other
License:	BSD
URL:		http://www.consol.com/opensource/nagios/check-logfiles
Source:     http://www.consol.com/fileadmin/opensource/Nagios/check_logfiles-%{version}.tar.gz

%description
check_logfiles is a Plugin for Nagios which scans log files for specific
patterns.

%prep
%setup -q -n check_logfiles-%{version}

%build
%configure2_5x --build=i586-mandriva-linux-gnu --libexec=%{_libdir}/nagios/plugins
%make


%install
%makeinstall_std

%files
%{_libdir}/nagios/plugins/check_logfiles

