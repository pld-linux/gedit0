Summary:	gEdit - small but powerful text editor for X Window
Summary(pl):	gEdit - ma³y ale potê¿ny edytor tekstu dla X Window
Name:		gedit
Version:	0.6.0
Release:	1
Copyright:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Source:		http://gedit.pn.org/%{name}-%{version}.tar.gz
Patch0:		gedit-desktop.patch
Patch1:		gedit-makefile.patch
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

%description
gEdit is a small but powerful text editor for GTK+ and/or GNOME.
It includes such features as split-screen mode, a plugin API, which 
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
%patch0 -p0
%patch1 -p0

%build
automake
gettextize --copy --force
LDFLAGS="-s" ; export LDFLAGS
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/gedit.1 \
	FAQ README README.plugins ChangeLog TODO AUTHORS THANKS KNOWNBUGS \
	TODO-road_to_1.0.0

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {FAQ,README,ChangeLog,TODO,AUTHORS,THANKS,README.plugins,KNOWNBUGS}.gz
%doc TODO-road_to_1.0.0.gz
%attr(755,root,root) %{_bindir}/gedit

%{_datadir}/applnk/Editors/gedit.desktop

%dir %{_datadir}/gnome/help/gedit
%{_datadir}/gnome/help/gedit/C
%lang(no) %{_datadir}/gnome/help/gedit/no

%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_datadir}/misc/geditrc
%{_mandir}/man1/gedit.1.gz
