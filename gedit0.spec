Summary:	gEdit - small but powerful text editor for X Window
Summary(pl.UTF-8):	gEdit - mały ale potężny edytor tekstu dla X Window
Name:		gedit
Version:	0.9.7
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gedit/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	ebef0c5e02fd3592350ff5b6fb9c6725
URL:		http://gedit.sourceforge.net/
Patch0:		%{name}-gnome-config.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-style-dsssl
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel > 1.0.55
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gnome-vfs >= 1.0
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	imlib-devel
BuildRequires:	libglade-gnome-devel >= 0.11
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRequires:	gnome-vfs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gedit-devel


%description
gEdit is a small but powerful text editor for GTK+ and/or GNOME. It
includes such features as split-screen mode, a plugin API, which
allows gEdit to be extended to support many features while remaining
small at its core, multiple document editing and many more functions.

%description -l pl.UTF-8
gEdit jest małym ale potężnym edytorem tekstu dla GTK+ i/lub GNOME.
Zawiera takie funkcje jak tryb podzielonego ekranu, API dla "wtyczek",
który umożliwia rozszerzenie funkcji gEdita o dodatkowe możliwości,
nie zwiększając rozmiarów samego programu, możliwość edycji wielu
dokumentów naraz i wiele innych.

%prep
%setup -q
%patch0 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing acinclude.m4
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make} gtkrcdir=%{_datadir}/misc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Editors

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ README README.plugins ChangeLog TODO AUTHORS THANKS
%attr(755,root,root) %{_bindir}/gedit
%dir %{_libdir}/gedit
%dir %{_libdir}/gedit/plugins
%attr(755,root,root) %{_libdir}/gedit/plugins/*.so.*.*
%{_libdir}/gedit/plugins/*.so
%{_pixmapsdir}/*
%{_datadir}/gedit
%{_datadir}/mime-info/*
%{_applnkdir}/Editors/gedit.desktop
%{_mandir}/man1/*
