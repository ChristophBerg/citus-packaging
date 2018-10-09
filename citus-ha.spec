%global pgmajorversion 10
%global pgpackageversion 10
%global pginstdir /usr/pgsql-%{pgpackageversion}
%global sname citus-ha
%global extname citusha

Summary:	Auto-HA support for Citus
Name:		%{sname}%{?pkginfix}_%{pgmajorversion}
Provides:	%{sname}_%{pgmajorversion}
Conflicts:	%{sname}_%{pgmajorversion}
Version:	1.0.0
Release:	1%{dist}
License:	AGPLv3
Group:		Applications/Databases
Source0:	https://github.com/citusdata/citus-ha/archive/v1.0.0.tar.gz
URL:		https://github.com/citusdata/citus-ha
BuildRequires:	postgresql%{pgmajorversion}-devel libxml2-devel
BuildRequires:	libxslt-devel openssl-devel pam-devel readline-devel
BuildRequires:	citus_%{pgmajorversion} >= 7.0.0
Requires:	postgresql%{pgmajorversion}-server citus-enterprise%{?pkginfix}_%{pgmajorversion} >= 7.0.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This extension implements a set of functions for supporting
Auto-HA on Citus cluster.

%prep
%setup -q -n %{sname}-%{version}

%build
PATH=%{pginstdir}/bin:$PATH
make %{?_smp_mflags}

%install
PATH=%{pginstdir}/bin:$PATH
%make_install
# Install documentation with a better name:
%{__mkdir} -p %{buildroot}%{pginstdir}/doc/extension
%{__cp} README.md %{buildroot}%{pginstdir}/doc/extension/README-%{extname}.md

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{pginstdir}/doc/extension/README-%{extname}.md
%{pginstdir}/lib/%{extname}.so
%{pginstdir}/share/extension/%{extname}-*.sql
%{pginstdir}/share/extension/%{extname}.control
%{pginstdir}/bin/%{extname}

%changelog
* Fri Oct 5 2018 - Burak Velioglu <velioglub@citusdata.com> 1.0.0
- Official release for 1.0.0
