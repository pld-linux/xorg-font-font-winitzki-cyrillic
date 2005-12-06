Summary:	winitzki-cyrillic font
Summary(pl):	Font winitzki-cyrillic
Name:		xorg-font-font-winitzki-cyrillic
Version:	0.99.1
Release:	0.1
License:	Public Domain
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-winitzki-cyrillic-%{version}.tar.bz2
# Source0-md5:	512f22880a73d4bf9c70102d0a60e8f8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/cyrillic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
winitzki-cyrillic font.

%description -l pl
Font winitzki-cyrillic.

%prep
%setup -q -n font-winitzki-cyrillic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/cyrillic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst cyrillic

%postun
fontpostinst cyrillic

%files
%defattr(644,root,root,755)
%{_fontsdir}/cyrillic/*
