Summary:	Red Connect Console Program
Summary(pl):	Tekstowy interfejs do dctc
Name:		cccp
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://members01.chello.se/hampasfirma/%{name}/%{name}.%{version}.tar.gz
URL:		http://members.chello.se/hampasfirma/cccp/index.html
Requires:	dctc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CCCP is a console front end to Direct Connect Text Client.

%description -l pl
CCCP jest konsolowym frontendem do Direct Connect Text Client.

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

install -d $RPM_BUILD_ROOT%{_bindir}
install cccp $RPM_BUILD_ROOT%{_bindir}
install scripts/dc.* $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README scripts/SCRIPTS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz scripts/*.gz
