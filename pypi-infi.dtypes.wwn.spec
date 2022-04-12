#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-infi.dtypes.wwn
Version  : 0.1.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/41/5d/27caf6dbfa5c5be22ccc05882b7aefce752cec3173607ca2e3b13fbfa261/infi.dtypes.wwn-0.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/5d/27caf6dbfa5c5be22ccc05882b7aefce752cec3173607ca2e3b13fbfa261/infi.dtypes.wwn-0.1.1.tar.gz
Summary  : Datatype for WWN
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-infi.dtypes.wwn-python = %{version}-%{release}
Requires: pypi-infi.dtypes.wwn-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)

%description
Overview
========
*infi.dtypes.wwn* provides a datatype for representing WWNs from strings in various formats.

%package python
Summary: python components for the pypi-infi.dtypes.wwn package.
Group: Default
Requires: pypi-infi.dtypes.wwn-python3 = %{version}-%{release}

%description python
python components for the pypi-infi.dtypes.wwn package.


%package python3
Summary: python3 components for the pypi-infi.dtypes.wwn package.
Group: Default
Requires: python3-core
Provides: pypi(infi.dtypes.wwn)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-infi.dtypes.wwn package.


%prep
%setup -q -n infi.dtypes.wwn-0.1.1
cd %{_builddir}/infi.dtypes.wwn-0.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649763357
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
