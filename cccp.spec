Summary:	Red Connect Console Program
Summary(pl):	Tekstowy interfejs do dctc
Name:		cccp
Version:	0.6
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://members01.chello.se/hampasfirma/%{name}/%{name}.%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://members01.chello.se/hampasfirma/cccp/
Requires:	dctc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CCCP is a console front end to the Direct Conect Text Client.
DCTC is a library that gives access to the direct connect world.
CCCP is a console based front end to that library. CCCP is 
designed to allow both scripting and command line interaction.

%description -l pl
CCCP jest konsolowym frontendem do Direct Connect Text Client.
DCTC jest bibliotek±, która daje dostêp do ¦wiata Bezpo¶rednich
Po³±czeñ, a CCCP jest konsolowym frontendem do tej biblioteki.
CCCP zosta³ stworzony, aby pozwoliæ jednocze¶nie na interaktywn±
oraz skryptow± pracê.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1

%build
%{__cc} %{rpmcflags} %{rpmldflags} cccp.c -o cccp

cd scripts
for i in [c-s]*
do
	mv $i dc.$i
done

%install
rm -rf $RPM_BUILD_ROOT

make	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1/ install

mv $RPM_BUILD_ROOT%{_mandir}/man1/cccp.1 $RPM_BUILD_ROOT%{_mandir}/man1/rccp.1
install scripts/dc.* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *.html scripts/SCRIPTS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
