Summary:	Winitzki Cyrillic font
Summary(pl.UTF-8):	Font Winitzki w cyrylicy
Name:		xorg-font-font-winitzki-cyrillic
Version:	1.0.4
Release:	1
License:	Public Domain
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-winitzki-cyrillic-%{version}.tar.xz
# Source0-md5:	e20f934068fb51af035cd7897a862393
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
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
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/cyrillic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# fonts.dir generated in post
%{__rm} $RPM_BUILD_ROOT%{_fontsdir}/cyrillic/fonts.dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst cyrillic

%postun
fontpostinst cyrillic

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/cyrillic/proof9x16.pcf.gz
