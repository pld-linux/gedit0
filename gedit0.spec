Summary:	gEdit - small but powerful text editor for X Window
Summary(pl):	gEdit - ma�y ale pot�ny edytor tekstu dla X Window
Name:		gedit
Version:	0.7.0
Release:	2
License:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Source0:	http://download.sourceforge.net/gedit/%{name}-%{version}.tar.gz
URL:		http://gedit.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	imlib-devel
BuildRequires:	zlib-devel
BuildRequires:	gnome-libs-devel > 1.0.55
BuildRequires:	gnome-print-devel >= 0.18
BuildRequires:	libglade-devel >= 0.11
BuildRequires:	gettext-devel
Requires:	go-plugins
Obsoletes:	gedit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gEdit is a small but powerful text editor for GTK+ and/or GNOME. It
includes such features as split-screen mode, a plugin API, which
allows gEdit to be extended to support many features while remaining
small at its core, multiple document editing and many more functions.

%description -l pl
gEdit jest ma�ym ale pot�nym edytorem tekstu dla GTK+ i/lub GNOME.
Zawiera takie funkcje jak tryb podzielonego ekranu, API dla "wtyczek",
kt�ry umo�liwia rozszerzenie funkcji gEdita o dodatkowe mo�liwo�ci,
nie zwi�kszaj�c rozmiar�w samego programu, mo�liwo�� edycji wielu
dokument�w naraz i wiele innych.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s" ; export LDFLAGS
%configure \
	--disable-staic

make gtkrcdir=%{_datadir}/misc

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Office/Editors

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	FAQ README README.plugins ChangeLog TODO AUTHORS THANKS TODO-road_to_1.0.0

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gedit
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_applnkdir}/Office/Editors/gedit.desktop
%{_mandir}/man1/*
