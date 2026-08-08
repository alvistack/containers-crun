# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: crun
Epoch: 100
Version: 1.28
Release: 1%{?dist}
Summary: OCI runtime written in C
License: GPLv2
URL: https://github.com/containers/crun/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?rhel} == 7
BuildRequires: devtoolset-11
BuildRequires: devtoolset-11-gcc
BuildRequires: devtoolset-11-gcc-c++
BuildRequires: devtoolset-11-libatomic-devel
%endif
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: glibc-static
BuildRequires: json-c-devel
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: python3
BuildRequires: systemd-devel
Provides: oci-runtime

%description
crun is a runtime for running OCI containers.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-11/enable
%endif
autoreconf -i
%if 0%{?suse_version} >= 1500
export CFLAGS='-I /usr/include/libseccomp'
%endif
%configure \
%if 0%{?rhel} == 7
    --disable-systemd \
%endif
    --disable-shared \
    --disable-static
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/*
rm -rf %{buildroot}/%{_mandir}/man1/*

%files
%license COPYING
%{_bindir}/crun

%changelog
