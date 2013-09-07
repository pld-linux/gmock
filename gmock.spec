Summary:	Google C++ Mocking Framework
Name:		gmock
Version:	1.6.0
Release:	2
License:	BSD
Group:		Development/Libraries
Source0:	https://googlemock.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	f547f47321ca88d3965ca2efdcc2a3c1
Patch0:		install.patch
URL:		http://code.google.com/p/googlemock/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtest-devel >= 1.5.0
BuildRequires:	libtool
BuildRequires:	python
Requires:	gtest-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s
specifics in mind, Google C++ Mocking Framework (or Google Mock for
short) is a library for writing and using C++ mock classes.

Google Mock:
- lets you create mock classes trivially using simple macros,
- supports a rich set of matchers and actions,
- handles unordered, partially ordered, or completely ordered
  expectations,
- is extensible by users, and
- works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and
  Symbian.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--host=%{_host} \
	--build=%{_host}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/gmock/generator/{README.cppclean,COPYING,README}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS COPYING README
%attr(755,root,root) %{_bindir}/gmock-config
%{_includedir}/%{name}
%{_npkgconfigdir}/gmock.pc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/generator
%attr(755,root,root) %{_datadir}/%{name}/generator/gmock_gen.py
%dir %{_datadir}/%{name}/generator/cpp
%attr(755,root,root) %{_datadir}/%{name}/generator/cpp/*.py
%{_prefix}/src/%{name}
