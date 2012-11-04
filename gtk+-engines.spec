Summary:	Default GTK+ theme engines
Name:		gtk+-engines
Version:	2.20.2
Release:	1
Epoch:		1
License:	GPL
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/2.20/gtk-engines-%{version}.tar.bz2
# Source0-md5:	5deb287bc6075dc21812130604c7dc4f
Patch0:		1e2d503ea6c1dbbf04fc0d7773338bd3f847257b.patch
Patch1:		8d49a386f467cbf8e0842d2218126f643e50f834.patch
Patch2:		a0cc71e7f62f355502045747cda973e674d3103b.patch
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the graphical engines for the various GTK+ toolkit themes.

%package devel
Summary:        gtk-engines development files
Group:          Development

%description devel
This is the package containing gtk-engines development files.

%prep
%setup -qn gtk-engines-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-crux		\
	--disable-glide		\
	--disable-hc		\
	--disable-industrial	\
	--disable-mist		\
	--disable-redmond	\
	--disable-silent-rules	\
	--disable-thinice
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# .la are not needed (according to spec included to package)
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/Redmond/gtk
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang gtk-engines

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
gdk-pixbuf-query-loaders --update-cache || :

%postun
if [ "$1" != "0" ]; then
    umask 022
    gdk-pixbuf-query-loaders --update-cache || :
fi

%files -f gtk-engines.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/Clearlooks
%{_datadir}/gtk-engines/*.xml

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*

