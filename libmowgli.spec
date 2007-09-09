Summary:	Development framework for C (like GLib)
Summary(pl.UTF-8):	Szkielet programistyczny dla C (podobny do GLiba)
Name:		libmowgli
Version:	0.4.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tgz
# Source0-md5:	46b03e8ac00bb49a6db9695d1c143aff
URL:		http://www.atheme-project.org/projects/mowgli.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib functions (like list
manipulation), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.

%description -l pl.UTF-8
mowgli to szkielet programistyczny dla C (podobny do GLiba)
udostępniający wysoko wydajne i elastyczne algorytmy. Może być używany
jako suplement do GLiba (dodający nowe funkcje, takie jak słowniki czy
hasze) albo do zastąpienia niektórych wolnych funkcji GLiba (jak
operacje na listach), albo samodzielnie. Udostępnia także potężny
system uchwytów i wygodnego logowania, a także wysoko wydajny alokator
bloków.

%package devel
Summary:        Header files for libmowgli
Summary(pl.UTF-8):	Pliki nagłówkowe libmowgli
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for libmowgli.

%description devel -l pl.UTF-8
Pliki nagłówkowe libmowgli.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libmowgli.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libmowgli.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmowgli.so
%{_includedir}/libmowgli
%{_pkgconfigdir}/libmowgli.pc
