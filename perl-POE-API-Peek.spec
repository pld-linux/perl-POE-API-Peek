#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	API-Peek
Summary:	POE::API::Peek - peek into the internals of a running POE environment
Summary(pl):	POE::API::Peek - wgl�d do wn�trza dzia�aj�cego �rodowiska POE
Name:		perl-POE-API-Peek
Version:	1.06
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2655a284b329ad8036ab4de3bbdd7f14
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

%description -l pl
POE:API::Peek rozszerza interfejs POE::Kernel dostarczaj�c czysty
dost�p do wn�trza Kernela POE w spos�b kompatybilny mi�dzy wersjami.
Inne wyliczone dane tak�e s� dost�pne.

Intencj� Autora jest dostarczenie du�ych ilo�ci danych wewn�trznych
przydatnych w procesie debugowania POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/000*{,._notused}

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
%{_mandir}/man3/*
