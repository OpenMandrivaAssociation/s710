%define libmajor 9
%define libname %mklibname %{name}_ %{libmajor}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Summary: 	Software for interfacing with Polar Heart Rate Monitors
Name: 		s710
Version: 	0.21
Release: 	3
URL:		http://daveb.net/s710/
Source0: 	http://s710.googlecode.com/files/%{name}-%{version}.tar.gz
License: 	GPL
Group: 		Toys

BuildRequires:	libusb-devel
BuildRequires:	gd-devel
BuildRequires:	libpng-devel

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
autoreconf -fi
%configure --with-usb
%make LIBS="-lgd -lusb -lm"

%install
%makeinstall_std

# weird docs dir
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/
mv %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/* %{buildroot}/%{_defaultdocdir}/%{name}/

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}/*
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

%files -n %{staticname}
%{_libdir}/*%{name}.a



%changelog
* Wed Oct 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.21-2
+ Revision: 707388
- added missing BR
- fix build and file list
- new version s710
  drop major from devel and static pkgs

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - import s710

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Sep 06 2006 Buchan Milne <bgmilne@mandriva.org> 0.19-3mdv2007.0
- Rebuild

* Fri Jan 27 2006 Buchan Milne <bgmilne@mandriva.org> 0.19-2mdk
- buildrequires

* Thu Jan 26 2006 Buchan Milne <bgmilne@mandriva.org> 0.19-1mdk
- Initial package
