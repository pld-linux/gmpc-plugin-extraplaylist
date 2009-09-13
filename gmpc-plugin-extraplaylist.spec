%define		source_name gmpc-extraplaylist
Summary:	Extraplaylist plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka extraplaylist dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-extraplaylist
Version:	0.18.100
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	95e5e07c04d969e3e28928b400ad70d0
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_EXTRA_PLAYLIST
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.18.100
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.18.100
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The extraplaylist plugin adds a second pane showing the playlist.

%description -l pl.UTF-8
Wtyczka extraplaylist dodaje drugie okienko pokazujące listę
odtwarzania.

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/libextraplaylist.so
