%define BINNAME qdtools-test-data
%define RPMNAME smartmet-%{BINNAME}
Summary: Test data for smartmet-qdtools
Name: %{RPMNAME}
Version: 25.4.11
Release: 1%{?dist}.fmi
License: MIT
Group: Development/Tools
URL: https://github.com/fmidev/smartmet-qdtools-test-data
Source0: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: make
BuildRequires: /usr/bin/install
BuildRequires: rpm-build
Provides: RPMNAME

%description
Test data for smartmet-qdtools. Data is not needed for production.

GIT repo - https://github.com/fmidev/smartmet-qdtools-test-data

%prep
%setup -q -n %{RPMNAME}

%build
make %{_smp_mflags}

%install
%makeinstall

%clean

%files
%defattr(0775,root,root,0775)
%{_datadir}/smartmet/test/data/qdtools/*

%changelog
* Fri Apr 11 2025 Andris Pavēnis <andris.pavenis@fmi.fi> 25.4.11-1.fmi
- Add new nctoqd test file with expected result (sla.nc)

* Thu Feb 20 2025 Andris Pavēnis <andris.pavenis@fmi.fi> 25.2.20-2.fmi
- Add 2 more expected result files for eccodes-2.39

* Thu Feb 20 2025 Andris Pavēnis <andris.pavenis@fmi.fi> 25.2.20-1.fmi
- Update gribtoqd test results for eccodes 2.39

* Thu Nov 28 2024 Andris Pavēnis <andris.pavenis@fmi.fi> 24.11.28-1.fmi
- Update for eccodes-2.38.X

* Tue Oct  1 2024 Andris Pavēnis <andris.pavenis@fmi.fi> 24.10.1-1.fmi
- Support eccodes-3.37.0 and optimize differences between versions

* Tue Sep 10 2024 Andris Pavēnis <andris.pavenis@fmi.fi> 24.9.10-1.fmi
- Update for eccodes-2.35.0

* Wed Apr  3 2024 Andris Pavēnis <andris.pavenis@fmi.fi> 24.4.3-1.fmi
- Update for eccodes-2.33.0

* Fri Oct 20 2023 Andris Pavēnis <andris.pavenis@fmi.fi> 23.10.20-1.fmi
- Compress part of largest test input and output files
- Update test results: support of eccodes-2.33.0, new results for csv2qd and bufrtoqd

* Tue Sep 19 2023 Andris Pavenis <andris.pavenis@fmi.fi> 23.9.19-1.fmi
- Update test results for eccodes-2.31 and add support of earlier versions

* Thu Sep  8 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.9.8-1.fmi
- Updated kriging2qd test result, origin time now has nonzero minutes (QDTOOLS-156)

* Thu Sep  1 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.9.1-1.fmi
- Fixed qdtogrib output after fix to stereographic projection conversion

* Wed Aug 31 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.31-1.fmi
- Added qdtogrib test input and output

* Wed Aug 24 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.24-1.fmi
- Updated expected qdinfo -x result after a fix to resolution calculations

* Thu Aug 18 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.18-1.fmi
- Removed HDF5 test data with a strange projection definition

* Tue Aug  9 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.9-4.fmi
- Removed unwanted temporary files

* Tue Aug  9 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.9-2.fmi
- Added expected results

* Tue Aug  9 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.9-1.fmi
- Separated test data from smartmet-qdtools
