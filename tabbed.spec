%define		commit	135
Summary:	Simple generic tabbed fronted to xembed aware applications
Summary(pl.UTF-8):	Prosty zarządca kart dla aplikacji obsługujących xembed
Name:		tabbed
Version:	0.2
Release:	0.%{commit}.1
License:	MIT
Group:		Applications
# hg clone http://hg.suckless.org/tabbed
Source0:	%{name}-%{version}-%{commit}.tar.bz2
# Source0-md5:	d0914cdcbcb9c9707afb7a5ea5e4c5d6
URL:		http://tools.suckless.org/tabbed
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tabbed is simple generic tabbed fronted to xembed aware applications,
originally designed for surf but also usable with many other
application, i.e. uzbl, urxvt and xterm

%prep
%setup -q -n %{name}-%{version}-%{commit}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tabbed
%{_mandir}/man1/tabbed.1*
