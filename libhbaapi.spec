%define buildversion 2.2.2

Name:           libhbaapi
Version:        2.2
Release:        10%{?dist}
Summary:        SNIA HBAAPI library

Group:          System Environment/Libraries
License:        SNIA
URL:            http://sourceforge.net/projects/hbaapi/
Source0:        http://downloads.sourceforge.net/hbaapi/hbaapi_src_%{version}.tgz
# This source was cloned from upstream git. To create tarball, run:
# git clone git://open-fcoe.org/openfc/hbaapi_build.git
# cd hbaapi_build
# git archive v%{buildversion} > ../hbaapi_build.tar
# cd .. && gzip hbaapi_build.tar
Source1:        hbaapi_build_%{buildversion}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0:         libhbaapi-2.2-9-dl-linking.patch

BuildRequires:  automake libtool
# Requires:       

%description
The SNIA HBA API library. C-level project to manage
Fibre Channel Host Bus Adapters.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n hbaapi_src_2.2
%setup -q -T -D -a 1 -n hbaapi_src_2.2
%patch0 -p1 -b .ld-linking


%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc readme.txt
%config(noreplace) %{_sysconfdir}/hba.conf
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Mar 08 2010 Jan Zeleny <jzeleny@redhat.com> - 2.2-10
- updated hbaapi_build to 2.2.2

* Wed Nov 04 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-9
- fixed linking with libdl

* Thu Jul 30 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-8
- added libtool to BuildRequires

* Thu Jul 30 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-7
- added automake to BuildRequires

* Thu Jul 30 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-6
- rebase of hbaapi_build code

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-4
- added some info to description line
- replaced unoficial build source tarball with official one

* Tue Mar 31 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-3
- minor changes in spec file - filenames change, removal of
  duplicate patch files (included in build source tarball)
  
* Thu Mar 12 2009 Jan Zeleny <jzeleny@redhat.com> - 2.2-2
- correction of patches' names to correct format

* Tue Feb 24 2009 Chris Leech <christopher.leech@intel.com> - 2.2-1
- initial packaging of hbaapi 2.2

