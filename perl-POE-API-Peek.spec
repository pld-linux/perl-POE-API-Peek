#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	API-Peek
Summary:	POE::API::Peek - peek into the internals of a running POE environment
Summary(pl):	POE::API::Peek - wgl±d do wnêtrza dzia³ajacego ¶rodowiska POE
Name:		perl-POE-API-Peek
Version:	1.0251
Release:	1
License:	Other
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ae6e858794e41fd4e8f61de04e875e5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(POE) >= 0.2802
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

%description -l pl
POE:API::Peek rozszerza interfejs POE::Kernel dostarczaj±c czysty
dostêp do wnêtrza Kernela POE w sposób kompatybilny miêdzy werjsami.
Inne wyliczone dane tak¿e s± dostêpne.

Intencj± Autora jest dostarczenie du¿ych ilo¶ci danych wewnêtrznych
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
%doc Changes README
%{perl_vendorlib}/POE/API/Peek.pm
%{_mandir}/man3/*
