Summary:	gEdit - small but powerful text editor for X Window
Summary(pl):	gEdit - ma³y ale potê¿ny edytor tekstu dla X Window
Name:		gedit
Version:	0.9.7
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.gnome.org/pub/gnome/stable/sources/gedit/%{name}-%{version}.tar.bz2
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
BuildRequires:	libglade-devel >= 0.11
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gedit-devel

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gEdit is a small but powerful text editor for GTK+ and/or GNOME. It
includes such features as split-screen mode, a plugin API, which
allows gEdit to be extended to support many features while remaining
small at its core, multiple document editing and many more functions.

%description -l pl
gEdit jest ma³ym ale potê¿nym edytorem tekstu dla GTK+ i/lub GNOME.
Zawiera takie funkcje jak tryb podzielonego ekranu, API dla "wtyczek",
który umo¿liwia rozszerzenie funkcji gEdita o dodatkowe mo¿liwo¶ci,
nie zwiêkszaj±c rozmiarów samego programu, mo¿liwo¶æ edycji wielu
dokumentów naraz i wiele innych.

%prep
%setup -q
%patch0 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing acinclude.m4
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c -f
%configure \
	--disable-static

%{__make} gtkrcdir=%{_datadir}/misc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Editors

gzip -9nf FAQ README README.plugins ChangeLog TODO AUTHORS THANKS

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gedit
%dir %{_libdir}/gedit
%dir %{_libdir}/gedit/plugins
%attr(755,root,root) %{_libdir}/gedit/plugins/*.so.*.*
%{_libdir}/gedit/plugins/*.so
%{_pixmapsdir}/*
%{_datadir}/gedit
%{_datadir}/mime-info/*
%{_applnkdir}/Office/Editors/gedit.desktop
%{_mandir}/man1/*
