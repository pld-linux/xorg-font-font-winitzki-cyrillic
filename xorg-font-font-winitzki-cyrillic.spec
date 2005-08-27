# $Rev: 3219 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-winitzki-cyrillic
Summary(pl):	font-winitzki-cyrillic
Name:		xorg-font-font-winitzki-cyrillic
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-winitzki-cyrillic-%{version}.tar.bz2
# Source0-md5:	1f074ba59affffc7d10b5bb53fd697f5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-winitzki-cyrillic-%{version}-root-%(id -u -n)

%description
font-winitzki-cyrillic

%description -l pl
font-winitzki-cyrillic


%prep
%setup -q -n font-winitzki-cyrillic-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/cyrillic/*
