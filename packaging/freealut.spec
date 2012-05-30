Name:       freealut
Summary:    OpenAL User Toolkit library
Version:    1.1.0
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/freealut.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(openal)


%description
OpenAL User Toolkit library development package



%package devel
Summary:    OpenAL User Toolkit library (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
OpenAL User Toolkit library development package (devel)


%prep
%setup -q 

%build
cp %{SOURCE1001} .
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%manifest freealut.manifest
%defattr(-,root,root,-)
%{_bindir}/freealut-config
%{_libdir}/libalut.so.*


%files devel
%manifest freealut.manifest
%defattr(-,root,root,-)
%{_includedir}/AL/alut.h
%{_libdir}/libalut.so
%{_libdir}/pkgconfig/freealut.pc
