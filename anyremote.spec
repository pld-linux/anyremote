#
# TODO:
# - find out what it Requires to run (bluez ? some irda-tools ?)
#
Summary:	anyremote - bluetooth remote for Linux
Summary(pl):	anyremote - pilot bluetooth dla Linuksa
Name:		anyremote
Version:	2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
# Source0-md5:	444c217871471672f3263554f46c0c58
URL:		http://anyremote.sourceforge.net
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The overall goal of this project is to provide wireless Bluetooth
remote control service for Linux. In contrast with other Bluetooth
remote control programs AnyRemote is not limited to SonyEriccson or
JSR-82 capable phones. Bluetooth connection is not the only way to use
it.

%description -l pl
Ogólnym celem tego projektu jest dostarczenie zdalnego,
bezprzewodowego systemu kontroli nad Linuksem z u¿yciem Bluetootha. W
odró¿nieniu od innych programów tego typu AnyRemote nie jest
ograniczony do obs³ugi telefonów SonyEriccsona czy JSR-82. Po³±czenia
Bluetooth nie s± jedynym sposobem by korzystaæ z programu.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/anyremote
