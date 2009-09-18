#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	API-Peek
Summary:	POE::API::Peek - peek into the internals of a running POE environment
Summary(pl.UTF-8):	POE::API::Peek - wgląd do wnętrza działającego środowiska POE
Name:		perl-POE-API-Peek
Version:	1.34
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c483bd98f7e0b45787dc8085f5c73ba
URL:		http://search.cpan.org/dist/POE-API-Peek/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-Size
BuildRequires:	perl-POE >= 0.2802
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::API::Peek extends the POE::Kernel interface to provide clean
access to Kernel internals in a cross-version compatible manner.
Other calculated data is also available.

Author's intention is to provide massive amounts of internal data for
use in POE debugging.

%description -l pl.UTF-8
POE:API::Peek rozszerza interfejs POE::Kernel dostarczając czysty
dostęp do wnętrza Kernela POE w sposób kompatybilny między wersjami.
Inne wyliczone dane także są dostępne.

Intencją Autora jest dostarczenie dużych ilości danych wewnętrznych
przydatnych w procesie debugowania POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%{perl_vendorlib}/POE/API/Peek.pm
%dir %{perl_vendorlib}/POE/API
%{_mandir}/man3/*
