Summary:	Wnn6 Client Library
Summary(pl):	Biblioteka kliencka Wnn6
Name:		Wnn6-SDK
Version:	1.0
Release:	11
License:	Copyright (C) OMRON Corporation, OMRON Software Co., Ltd. (see README)
Group:		Libraries
Source0:	ftp://ftp.omronsoft.co.jp/pub/Wnn6/sdk_source/%{name}.tar.gz
# Source0-md5:	8e0148560524643680fd016e5c4e406b
Patch0:		%{name}-config.patch
Patch1:		%{name}-incl.patch
Patch2:		%{name}-shared.patch
Patch3:		%{name}-malloc.patch
Patch4:		%{name}-nonroot.patch
Patch5:		%{name}-cpp_workaround.patch
Patch6:		%{name}-header.patch
URL:		http://www.omronsoft.co.jp/SP/pcunix/wnn/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runtime Wnn6 client library necessary to run Wnn6 clients.

%description -l pl
Biblioteka kliencka Wnn6 potrzebna do uruchamiania klientów Wnn6.

%package devel
Summary:	Header files for Wnn6
Summary(pl):	Pliki nag³ówkowe Wnn6
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains header files for Wnn6 client developments.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do tworzenia klientów Wnn6.

%package static
Summary:	Static Wnn6 client library
Summary(pl):	Statyczna biblioteka kliencka Wnn6
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Wnn6 client library.

%description static -l pl
Statyczna biblioteka kliencka Wnn6.

%prep
%setup -q -n src/contrib/im/Xsi
%patch0 -p4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p0

%build
%{__make} World -f Makefile.ini \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_libdir}/libwnn6.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libwnn6.so
%{_includedir}/wnn6

%files static
%defattr(644,root,root,755)
%{_libdir}/libwnn6.a
