#
# TODO:
# - find out what it Requires to run (bluez ? some irda-tools ?)
#
Summary:	anyremote - bluetooth remote for Linux
Summary(pl.UTF-8):	anyremote - pilot bluetooth dla Linuksa
Name:		anyremote
Version:	5.4.2
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
# Source0-md5:	9cd6b4075ae3f66ff0177c7e7cb2bafc
Patch0:		%{name}-in.patch
Patch1:		%{name}-useless_files.patch
URL:		http://anyremote.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The overall goal of this project is to provide wireless Bluetooth or
InfraRed remote control service for Linux. In contrast with other
Bluetooth remote control programs AnyRemote is not limited to
SonyEricsson or JSR-82 capable phones. It was developed as just thin
"communication" layer beetween bluetooth-capabled phone and Linux, and
in principle could be configured to manage any software. But Bluetooth
is not the only way to use it. AnyRemote could be used with:
- IR-capabled phone
- with cable connection
- it could accept incoming connection from network
- it could work with Java client written for JSR82 capabled phones
  (like Bemused)
- it have limited support for existing Bemused clients.

kAnyRemote is its KDE equivalent (you can find it in kanyremote
package).

%description -l pl.UTF-8
Ogólnym celem tego projektu jest dostarczenie zdalnego,
bezprzewodowego systemu kontroli nad Linuksem z użyciem Bluetootha lub
podczerwieni (IrDA). W odróżnieniu od innych programów tego typu
AnyRemote nie jest ograniczony do obsługi telefonów SonyEricssona czy
JSR-82. Został zaprojektowany jako cienka warstwa "komunikacyjna"
między telefonem posiadającym Bluetooth, a Linuksem i w zasadzie może
zostać skonfigurowany do obsługi każdej aplikacji. Połączenia
Bluetooth nie są jedynym sposobem by korzystać z programu. AnyRemote
może być używany wraz z:
- telefonami posiadającymi podczerwień (IrDA)
- telefonami z połączeniem kablowym
- może odbierać połączenia przychodzące z sieci
- klientem Javy napisanym dla telefonów obsługujących JSR82 (jak
  Bemused)
- już istniejącymi klientami Bemused (częściowa obsługa).

Jego odpowiednikiem dla środowiska KDE jest kAnyRemote (można go
znaleźć w pakiecie kanyremote).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
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
%doc AUTHORS NEWS README doc-html
%attr(755,root,root) %{_bindir}/anyremote
%{_datadir}/anyremote
%{_mandir}/man1/anyremote.1.*
