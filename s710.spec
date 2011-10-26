%define libmajor 9
%define libname %mklibname %{name}_ %{libmajor}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Summary: 	Software for interfacing with Polar Heart Rate Monitors
Name: 		s710
Version: 	0.21
Release: 	2
URL:		http://daveb.net/s710/
Source0: 	http://s710.googlecode.com/files/%{name}-%{version}.tar.gz
License: 	GPL
Group: 		Toys

BuildRequires:	libusb-devel
BuildRequires:	gd-devel

%description 
This software lets you communicate from a Linux computer to a Polar S710 heart
rate monitor via the serial IR or USB interface. It is not complete, but a
utility is provided that gives you the ability to view the settings on the
watch and download exercise files. Other utilities (also provided) allow you to
print the contents of exercise files and render the data in PNG graphs. A Perl
interface to the library is also provided.

%package -n %{libname}
Summary: 	Library for interfacing with Polar Heart Rate Monitors
License:	GPL
Group:		Development/Other

%description -n %{libname}
This package contains the library required by applications which communicate
with Polar Heart Rate Monitors

%package -n %{develname}
Summary: 	Library for interfacing with Polar Heart Rate Monitors
License:	GPL
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{name}_ %{libmajor} -d}

%description -n %{develname}
This package contains the development library required to compile applications
which communicate with Polar Heart Rate Monitors.

%package -n %{staticname}
Summary: 	Library for interfacing with Polar Heart Rate Monitors
License:	GPL
Group:		Development/Other
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Provides:	%{libname}-static-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{name}_ %{libmajor} -s -d}

%description -n %{staticname}
This package contains the development library required to compile applications
which communicate with Polar Heart Rate Monitors, but to not depend on the
library.

%prep
%setup -q

%build
%configure --with-usb
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

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

%files -n %{libname}
%{_libdir}/*%{name}.so.%{libmajor}*

%files -n %{develname}
%{_includedir}/%{name}.h
%{_libdir}/*%{name}.so
%{_libdir}/*%{name}.la

%files -n %{staticname}
%{_libdir}/*%{name}.a

