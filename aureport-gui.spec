Name:   aureport-gui
Summary: Utility for audit log visualization
Version: 1.0
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
BuildRequires: desktop-file-utils
Requires: audit pychart PyQt 
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description  
A graphical client utility for audit log visualization.

%prep
%setup -q

%build
bash ./autogen.sh
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/aureport-gui
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/{man5,man8}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
make DESTDIR=$RPM_BUILD_ROOT %{?_smp_mflags} install

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755, root, root)
%doc  README COPYING ChangeLog NEWS AUTHORS 
%{_bindir}/aureport-gui
%{_bindir}/mkbar
%{_datadir}/*

%changelog
*Mon Mar 22 2010 cheliequan <cheliequan@redflag-linux.com> 1.0.1
- add new aureport-gui package
