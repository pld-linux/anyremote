#
# TODO:
# - find out what it Requires to run (bluez ? some irda-tools ?)
#
Summary:	anyremote - bluetooth remote for Linux
Summary(pl):	anyremote - pilot bluetooth dla Linuksa
Name:		anyremote
Version:	2.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
# Source0-md5:	6acb19958a54aa50fcd10545dc34ffc6
Patch0:		%{name}-in.patch
Patch1:		%{name}-link.patch
URL:		http://anyremote.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	libtool
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

%description -l pl
Ogólnym celem tego projektu jest dostarczenie zdalnego,
bezprzewodowego systemu kontroli nad Linuksem z u¿yciem Bluetootha lub
podczerwieni (IrDA). W odró¿nieniu od innych programów tego typu
AnyRemote nie jest ograniczony do obs³ugi telefonów SonyEricssona czy
JSR-82. Zosta³ zaprojektowany jako cienka warstwa "komunikacyjna"
miêdzy telefonem posiadaj±cym Bluetooth, a Linuksem i w zasadzie mo¿e
zostaæ skonfigurowany do obs³ugi ka¿dej aplikacji. Po³±czenia
Bluetooth nie s± jedynym sposobem by korzystaæ z programu. AnyRemote
mo¿e byæ u¿ywany wraz z:
- telefonami posiadaj±cymi podczerwieñ (IrDA)
- telefonami z po³±czeniem kablowym
- mo¿e odbieraæ po³±czenia przychodz±ce z sieci
- klientem Javy napisanym dla telefonów obs³uguj±cych JSR82 (jak
  Bemused)
- ju¿ istniej±cymi klientami Bemused (czê¶ciowa obs³uga).

Jego odpowiednikiem dla ¶rodowiska KDE jest kAnyRemote (mo¿na go
znale¼æ w pakiecie kanyremote).

%prep
%setup -q
%patch0 -p0
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
%doc AUTHORS NEWS README cfg-examples
%attr(755,root,root) %{_bindir}/anyremote
