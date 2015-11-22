Summary:	Google C++ Mocking Framework
Summary(pl.UTF-8):	Szkielet Google Mock dla C++
Name:		gmock
Version:	1.7.0
Release:	4
License:	BSD
Group:		Development/Libraries
#Source0Download: http://code.google.com/p/googlemock/downloads/list
Source0:	https://googlemock.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	073b984d8798ea1594f5e44d85b20d66
Patch0:		install.patch
URL:		http://code.google.com/p/googlemock/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gtest-devel >= 1.7.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	python >= 2.3
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{_host_cpu} == "x32"
%define	build_arch %{_target_platform}
%else
%define	build_arch %{_host}
%endif

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

%description -l pl.UTF-8
Google C++ Mocking Framework (w skrócie Google Mock) to zainspirowana
przez jMock, EasyMock i Hamcrest, zaprojektowana z myślą o specyfice
C++ biblioteka do pisania i wykorzystywania klas "mock" w C++.

Google Mock:
- pozwala tworzyć klasy "mock" w sposób trywialny przy użyciu makr;
- obsługuje bogaty zbiór dopasowań i akcji;
- obsługuje oczekiwania nieuporządkowane, częściowo uporządkowane
  lub w pełni uporządkowane;
- jest rozszerzalna dla użytkownika;
- działa na Linuksie, Mac OS X, Windows, Windows Mobile, minGW oraz
  Symbianie.

%package devel
Summary:	Google C++ Mocking Framework
Summary(pl.UTF-8):	Szkielet Google Mock dla C++
Group:		Development/Libraries
Requires:	gtest-devel >= 1.7.0-2
Requires:	libstdc++-devel
Provides:	%{name} = %{version}-%{release}
Obsoletes:	gmock < 1.6.0-3

%description devel
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

%description devel -l pl.UTF-8
Google C++ Mocking Framework (w skrócie Google Mock) to zainspirowana
przez jMock, EasyMock i Hamcrest, zaprojektowana z myślą o specyfice
C++ biblioteka do pisania i wykorzystywania klas "mock" w C++.

Google Mock:
- pozwala tworzyć klasy "mock" w sposób trywialny przy użyciu makr;
- obsługuje bogaty zbiór dopasowań i akcji;
- obsługuje oczekiwania nieuporządkowane, częściowo uporządkowane
  lub w pełni uporządkowane;
- jest rozszerzalna dla użytkownika;
- działa na Linuksie, Mac OS X, Windows, Windows Mobile, minGW oraz
  Symbianie.

%prep
%setup -q
%patch0 -p1

grep -rl bin/env scripts | xargs %{__sed} -i -e '1s,^#!.*python,#!%{__python},'

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--host=%{build_arch} \
	--build=%{build_arch}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/gmock/generator/{README.cppclean,LICENSE,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS LICENSE README
%attr(755,root,root) %{_bindir}/gmock-config
%{_includedir}/%{name}
%{_npkgconfigdir}/gmock.pc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/generator
%attr(755,root,root) %{_datadir}/%{name}/generator/gmock_gen.py
%dir %{_datadir}/%{name}/generator/cpp
%attr(755,root,root) %{_datadir}/%{name}/generator/cpp/*.py
%{_prefix}/src/%{name}
