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
The overall goal of this project is to provide wireless Bluetooth or
InfraRed remote control service for Linux. In contrast with other
Bluetooth remote control programs AnyRemote is not limited to
SonyEriccson or JSR-82 capable phones. It was developed as just thin
"communication" layer beetween bluetooth-capabled phone and Linux, and
in principle could be configured to manage any software. But Bluetooth
is not the only way to use it. AnyRemote could be used with:
- IR-capabled phone
- with cable connection
- it could accept incoming connection from network
- it could work with Java client written for JSR82 capabled phones
  (like Bemused)
- it have limited support for existing Bemused clients.

kAnyRemote is its KDE equivalent (you can find it in kanyremote.spec).

%description -l pl
Ogólnym celem tego projektu jest dostarczenie zdalnego,
bezprzewodowego systemu kontroli nad Linuksem z u¿yciem Bluetootha lub
podczerwieni (IrDA). W odró¿nieniu od innych programów tego typu
AnyRemote nie jest ograniczony do obs³ugi telefonów SonyEriccsona czy
JSR-82. Zosta³ zaprojektowany jako cienka warstwa "komunikacyjna"
miêdzy telefonem posiadaj±cym Bluetooth, a Linuksem i w zasadzie mo¿e
zostaæ skonfigurowany do obs³ugi ka¿dej aplikacji. Po³±czenia
Bluetooth nie s± jedynym sposobem by korzystaæ z programu. AnyRemote
mo¿e byæ u¿ywany wraz z:
- telefonami posiadaj±cymi podczerwieñ (IrDA)
- telefonami z po³±czeniem kablowym
- mo¿e odbieraæ po³±czenia przychodz±ce z sieci
- clientem Javy napisanym dla telefonów obs³uguj±cych JSR82 (jak
  Bemused)
- z ju¿ istniej±cymi klientami Bemused (czê¶ciowa obs³uga).

Jego odpowiednikiem dla ¶rodowiska KDE jest kAnyRemote (mo¿esz go
znale¼æ w kanyremote.spec).

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
