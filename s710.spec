%define name s710
%define version 0.19
%define release %mkrel 3
%define libmajor 5
%define libname %mklibname %{name}_ %{libmajor}

Summary: 	Software for interfacing with Polar Heart Rate Monitors
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
URL:		http://daveb.net/s710/
Source0: 	http://daveb.net/s710/src/%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		Toys
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	libusb-devel gd-devel

%description 
This software lets you communicate from a Linux computer to a Polar S710 heart
rate monitor via the serial IR or USB interface. It is not complete, but a
utility is provided that gives you the ability to view the settings on the
watch and download exercise files. Other utilities (also provided) allow you to
print the contents of exercise files and render the data in PNG graphs. A Perl
interface to the library is also provided.

%package -n %libname
Summary: 	Library for interfacing with Polar Heart Rate Monitors
License:	GPL
Group:		Development/Other

%description -n %libname
This package contains the library required by applications which communicate
with Polar Heart Rate Monitors

%package -n %libname-devel
Summary: 	Library for interfacing with Polar Heart Rate Monitors
License:	GPL
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %libname-devel
This package contains the development library required to compile applications
which communicate with Polar Heart Rate Monitors.

%package -n %libname-static-devel
Summary: 	Library for interfacing with Polar Heart Rate Monitors
License:	GPL
Group:		Development/Other
Requires:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %libname-static-devel
This package contains the development library required to compile applications
which communicate with Polar Heart Rate Monitors, but to not depend on the
library.

%prep
%setup -q

%build
%configure --with-usb
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING INSTALL NEWS
%{_bindir}/s710d
%{_bindir}/s710sh
%{_bindir}/srdcat
%{_bindir}/srdhead
%{_bindir}/srdplot
%{_bindir}/srd2hrm
%{_bindir}/srdmerge

%files -n %libname
%{_libdir}/*%{name}.so.*

%files -n %{libname}-devel
%{_includedir}/%{name}.h
%{_libdir}/*%{name}.so
%{_libdir}/*%{name}.la

%files -n %{libname}-static-devel
%{_libdir}/*%{name}.a

