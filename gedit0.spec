Summary:	gEdit - small but powerful text editor.
Summary(pl):	gEdit - ma³y ale potê¿ny edytor tekstu.
Name:		gedit
Version:	0.5.1
Release:	3
Copyright:	GPL
Group:		X11/Editors
Source0:	%{name}-%{version}.tar.gz
URL:		http://gedit.pn.org
BuildPrereq:	gtk+-devel >= 1.0.7
BuildPrereq:	glib-devel >= 1.0.7
#Requires:	gnome-libs
BuildRoot:      /tmp/%{name}-%{version}-root

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

%package devel
Summary:	Develop plugins for the gEdit editor.
Summary(pl):	Biblioteki umo¿liwiaj±ce pisanie pluginów do gEdit.
Group: 		Development/Libraries
Group(pl):	Programowanie/Biblioteki

%description devel
gEdit is a small but powerful text editor for GTK+ and/or GNOME.
This package allows you to develop plugins that work within
gEdit.  Plugins can create new documents and manipulate documents
in arbitrary ways.

%description devel -l pl
gEdit jest ma³ym ale potê¿nym edytorem tekstu dla GTK+ i/lub GNOME.
Ten pakiet zawiera biblioteki umo¿liwiaj±ce pisanie "wtyczek" dla gEdita.
"Wtyczki" mog± tworzyæ nowe dokumenty i manipulowaæ nimi na wiele róznych
sposobów.
 
%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/* \
	README ChangeLog NEWS TODO AUTHORS THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,NEWS,TODO,AUTHORS,THANKS}.gz
%attr(755,root,root) /usr/X11R6/bin/gedit
/usr/X11R6/share/locale/*/*/*
/usr/X11R6/share/gnome/apps/*/*
/usr/X11R6/share/pixmaps/*
/usr/X11R6/share/mime-info/*
/usr/X11R6/share/geditrc
/usr/X11R6/man/man1/*
/usr/X11R6/libexec/*/*/*


%files devel
%defattr(644,root,root,755)
/usr/X11R6/include/*/*
/usr/X11R6/lib/*

* Thu Oct 22 1998 Alex Roberts <bse@dial.pipex.com>
- First try at an RPM
