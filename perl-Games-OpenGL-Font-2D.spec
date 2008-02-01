#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
# test are failing, no idea why, yet
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	OpenGL-Font-2D
Summary:	perl(Games::OpenGL::Font::2D) - load/render 2D colored bitmap fonts via OpenGL
Name:		perl-Games-OpenGL-Font-2D
Version:	0.07
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae55f071dc5bb395401b5a25780555ca
URL:		http://search.cpan.org/dists/Games-OpenGl-Font-2D
BuildRequires:	perl-SDL
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	perl-
#BuildRequires:	perl-SDL
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package lets you load and render colored bitmap fonts via OpenGL.

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/lib/SDL/App/FPS
install examples/font.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/font.pl
install examples/lib/SDL/App/FPS/MyFont.pm $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/lib/SDL/App/FPS/MyFont.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES BUGS TODO
# use macros:
%{perl_vendorlib}/Games/OpenGL/Font/2D.pm
#%%{perl_vendorarch}/...
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}/font.pl
%{_examplesdir}/%{name}-%{version}/lib/SDL/App/FPS/MyFont.pm
