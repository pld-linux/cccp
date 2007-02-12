Summary:	Red Connect Console Program
Summary(pl.UTF-8):	Tekstowy interfejs do dctc
Name:		cccp
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://members01.chello.se/hampasfirma/%{name}/%{name}.%{version}.tar.gz
# Source0-md5:	44500b5077a9791d9c5eeaeace6ef34b
URL:		http://members01.chello.se/hampasfirma/cccp/
Requires:	dctc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CCCP is a console front end to the Direct Connect Text Client.
DCTC is a library that gives access to the direct connect world.
CCCP is a console based front end to that library. CCCP is
designed to allow both scripting and command line interaction.

%description -l pl.UTF-8
CCCP jest konsolowym frontendem do Direct Connect Text Client.
DCTC jest biblioteką, która daje dostęp do Świata Bezpośrednich
Połączeń, a CCCP jest konsolowym frontendem do tej biblioteki.
CCCP został stworzony, aby pozwolić jednocześnie na interaktywną
oraz skryptową pracę.

%prep
%setup -q -n %{name}.%{version}

%build
%{__cc} %{rpmcflags} %{rpmldflags} cccp.c -o cccp

cd scripts
for i in [c-s]*
do
	mv $i dc.$i
done

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

mv $RPM_BUILD_ROOT%{_mandir}/man1/cccp.1 $RPM_BUILD_ROOT%{_mandir}/man1/rccp.1
install scripts/dc.* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *.html scripts/SCRIPTS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
