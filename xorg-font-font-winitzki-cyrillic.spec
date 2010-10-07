Summary:	Winitzki Cyrillic font
Summary(pl.UTF-8):	Font Winitzki w cyrylicy
Name:		xorg-font-font-winitzki-cyrillic
Version:	1.0.2
Release:	1
License:	Public Domain
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-winitzki-cyrillic-%{version}.tar.bz2
# Source0-md5:	2d92227f14910732dc46303d6f8a9543
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.3
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/cyrillic
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Winitzki Cyrillic font.

%description -l pl.UTF-8
Font Winitzki w cyrylicy.

%prep
%setup -q -n font-winitzki-cyrillic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--with-fontdir=%{_fontsdir}/cyrillic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# fonts.scale bogus, fonts.dir generated in post
rm -f $RPM_BUILD_ROOT%{_fontsdir}/cyrillic/fonts.{dir,scale}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst cyrillic

%postun
fontpostinst cyrillic

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/cyrillic/proof9x16.pcf.gz
