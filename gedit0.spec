Summary:	gEdit - small but powerful text editor for X Window.
Summary(pl):	gEdit - ma³y ale potê¿ny edytor tekstu dla X Window.
Name:		gedit
Version:	0.5.1
Release:	3
Copyright:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Source:		%{name}-%{version}.tar.gz
Patch0:		gedit-DESTDIR.patch
Patch1:		gedit-desktop.patch
URL:		http://gedit.pn.org
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	imlib-devel
BuildPrereq:	zlib-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	gnome-libs-devel
BuildRoot:	/tmp/%{name}-%{version}-root

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
Requires:	%{name} = %{version}

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
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/gedit.1 \
	FAQ README README.plugins ChangeLog TODO AUTHORS THANKS KNOWNBUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {FAQ,README,ChangeLog,TODO,AUTHORS,THANKS,README.plugins,KNOWNBUGS}.gz
%attr(755,root,root) /usr/X11R6/bin/gedit

%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/gedit.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gedit.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/gedit.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gedit.mo
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/gedit.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gedit.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gedit.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/gedit.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/gedit.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gedit.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/gedit.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/gedit.mo

/usr/X11R6/share/gnome/apps/Applications/gedit.desktop
/usr/X11R6/share/pixmaps/*
/usr/X11R6/share/mime-info/*
/usr/X11R6/share/geditrc
/usr/X11R6/man/man1/gedit.1.gz
%attr(755,root,root) /usr/X11R6/libexec/go/plugins/*


%files devel
%defattr(644,root,root,755)
%dir /usr/X11R6/include/gedit
/usr/X11R6/include/gedit/client.h
/usr/X11R6/lib/libclient.a

%description
* Tue Apr 27 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.5.0-3]
- cleaned up spec file for PLD use,
- fixed Summary, Group and %description fields,
- added pl translation,
- added -q setup parameter,
- changed prefix to /usr/X11R6,
- added full %defattr description,
- added %attr and %lang macros,
- added pl translation for gnome desktop file,
- added using DESTDIR during install (gedit-DESTDIR.patch),
- added stripping binaries during install,
- added some BuildPrereqs,
- recompiled on rpm 3,
- major changes.

* Thu Oct 22 1998 Alex Roberts <bse@dial.pipex.com>
- First try at an RPM
