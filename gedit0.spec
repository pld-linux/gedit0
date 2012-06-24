Summary:	gEdit - small but powerful text editor for X Window
Summary(pl):	gEdit - ma�y ale pot�ny edytor tekstu dla X Window
Name:		gedit
Version:	0.5.4
Release:	1
Copyright:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Source:		http://gedit.pn.org/%{name}-%{version}.tar.gz
Patch0:		gedit-desktop.patch
Patch1:		gedit-DESTDIR.patch
Patch2:		gedit-dcl.patch
Patch3:		gedit-plugins.patch
URL:		http://gedit.pn.org
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRequires:	gnome-libs-devel
Requires: 	go-plugins
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_libexecdir	%{_libdir}

%description
gEdit is a small but powerful text editor for GTK+ and/or GNOME.
It includes such features as split-screen mode, a plugin API, which 
allows gEdit to be extended to support many features while remaining 
small at its core, multiple document editing and many more functions.

%description -l pl
gEdit jest ma�ym ale pot�nym edytorem tekstu dla GTK+ i/lub GNOME.
Zawiera takie funkcje jak tryb podzielonego ekranu, API dla "wtyczek",
kt�ry umo�liwia rozszerzenie funkcji gEdita o dodatkowe mo�liwo�ci,
nie zwi�kszaj�c rozmiar�w samego programu, mo�liwo�� edycji wielu 
dokument�w naraz i wiele innych.

%package devel
Summary:	Develop plugins for the gEdit editor
Summary(pl):	Biblioteki umo�liwiaj�ce pisanie wtyczek dla gEdit
Group: 		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
gEdit is a small but powerful text editor for GTK+ and/or GNOME.
This package allows you to develop plugins that work within
gEdit.  Plugins can create new documents and manipulate documents
in arbitrary ways.

%description devel -l pl
gEdit jest ma�ym ale pot�nym edytorem tekstu dla GTK+ i/lub GNOME.
Ten pakiet zawiera biblioteki umo�liwiaj�ce pisanie "wtyczek" dla gEdita.
"Wtyczki" mog� tworzy� nowe dokumenty i manipulowa� nimi na wiele r�znych
sposob�w.
 
%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p0

%build
gettextize --copy --force
LDFLAGS="-s" ; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/gedit.1 \
	FAQ README README.plugins ChangeLog TODO AUTHORS THANKS KNOWNBUGS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {FAQ,README,ChangeLog,TODO,AUTHORS,THANKS,README.plugins,KNOWNBUGS}.gz
%attr(755,root,root) %{_bindir}/gedit

%{_datadir}/applnk/Editors/gedit.desktop

%dir %{_datadir}/gnome/help/gedit
%{_datadir}/gnome/help/gedit/C
%lang(no) %{_datadir}/gnome/help/gedit/no

%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_datadir}/geditrc
%{_mandir}/man1/gedit.1.gz

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/gedit
%{_includedir}/gedit/client.h
%{_libdir}/libclient.a
