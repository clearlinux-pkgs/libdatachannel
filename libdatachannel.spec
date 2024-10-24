#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v13
# autospec commit: 2659038
#
Name     : libdatachannel
Version  : 0.21.2
Release  : 9
URL      : https://github.com/paullouisageneau/libdatachannel/archive/v0.21.2/libdatachannel-0.21.2.tar.gz
Source0  : https://github.com/paullouisageneau/libdatachannel/archive/v0.21.2/libdatachannel-0.21.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libdatachannel-lib = %{version}-%{release}
Requires: libdatachannel-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : gnutls-dev
BuildRequires : libjuice-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libsrtp2)
BuildRequires : pkgconfig(mbedcrypto)
BuildRequires : pkgconfig(mbedtls)
BuildRequires : pkgconfig(mbedx509)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(nice)
BuildRequires : pkgconfig(nlohmann_json)
BuildRequires : pkgconfig(usrsctp)
BuildRequires : plog-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# libdatachannel - C/C++ WebRTC network library
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-blue.svg)](https://www.mozilla.org/en-US/MPL/2.0/)
[![Build with GnuTLS](https://github.com/paullouisageneau/libdatachannel/actions/workflows/build-gnutls.yml/badge.svg)](https://github.com/paullouisageneau/libdatachannel/actions/workflows/build-gnutls.yml)
[![Build with Mbed TLS](https://github.com/paullouisageneau/libdatachannel/actions/workflows/build-mbedtls.yml/badge.svg)](https://github.com/paullouisageneau/libdatachannel/actions/workflows/build-mbedtls.yml)
[![Build with OpenSSL](https://github.com/paullouisageneau/libdatachannel/actions/workflows/build-openssl.yml/badge.svg)](https://github.com/paullouisageneau/libdatachannel/actions/workflows/build-openssl.yml)

%package dev
Summary: dev components for the libdatachannel package.
Group: Development
Requires: libdatachannel-lib = %{version}-%{release}
Provides: libdatachannel-devel = %{version}-%{release}
Requires: libdatachannel = %{version}-%{release}

%description dev
dev components for the libdatachannel package.


%package lib
Summary: lib components for the libdatachannel package.
Group: Libraries
Requires: libdatachannel-license = %{version}-%{release}

%description lib
lib components for the libdatachannel package.


%package license
Summary: license components for the libdatachannel package.
Group: Default

%description license
license components for the libdatachannel package.


%prep
%setup -q -n libdatachannel-0.21.2
cd %{_builddir}/libdatachannel-0.21.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720449955
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DPREFER_SYSTEM_LIB=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720449955
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libdatachannel
cp %{_builddir}/libdatachannel-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libdatachannel/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
cp %{_builddir}/libdatachannel-%{version}/examples/signaling-server-nodejs/LICENSE %{buildroot}/usr/share/package-licenses/libdatachannel/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
cp %{_builddir}/libdatachannel-%{version}/examples/signaling-server-python/LICENSE %{buildroot}/usr/share/package-licenses/libdatachannel/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
cp %{_builddir}/libdatachannel-%{version}/examples/signaling-server-qt/LICENSE %{buildroot}/usr/share/package-licenses/libdatachannel/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
cp %{_builddir}/libdatachannel-%{version}/examples/signaling-server-rust/LICENSE %{buildroot}/usr/share/package-licenses/libdatachannel/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
cp %{_builddir}/libdatachannel-%{version}/examples/web/LICENSE %{buildroot}/usr/share/package-licenses/libdatachannel/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/rtc/av1rtppacketizer.hpp
/usr/include/rtc/candidate.hpp
/usr/include/rtc/channel.hpp
/usr/include/rtc/common.hpp
/usr/include/rtc/configuration.hpp
/usr/include/rtc/datachannel.hpp
/usr/include/rtc/description.hpp
/usr/include/rtc/frameinfo.hpp
/usr/include/rtc/global.hpp
/usr/include/rtc/h264rtpdepacketizer.hpp
/usr/include/rtc/h264rtppacketizer.hpp
/usr/include/rtc/h265nalunit.hpp
/usr/include/rtc/h265rtppacketizer.hpp
/usr/include/rtc/mediahandler.hpp
/usr/include/rtc/message.hpp
/usr/include/rtc/nalunit.hpp
/usr/include/rtc/pacinghandler.hpp
/usr/include/rtc/peerconnection.hpp
/usr/include/rtc/plihandler.hpp
/usr/include/rtc/reliability.hpp
/usr/include/rtc/rtc.h
/usr/include/rtc/rtc.hpp
/usr/include/rtc/rtcpnackresponder.hpp
/usr/include/rtc/rtcpreceivingsession.hpp
/usr/include/rtc/rtcpsrreporter.hpp
/usr/include/rtc/rtp.hpp
/usr/include/rtc/rtpdepacketizer.hpp
/usr/include/rtc/rtppacketizationconfig.hpp
/usr/include/rtc/rtppacketizer.hpp
/usr/include/rtc/track.hpp
/usr/include/rtc/utils.hpp
/usr/include/rtc/version.h
/usr/include/rtc/websocket.hpp
/usr/include/rtc/websocketserver.hpp
/usr/lib64/cmake/LibDataChannel/LibDataChannelConfig.cmake
/usr/lib64/cmake/LibDataChannel/LibDataChannelConfigVersion.cmake
/usr/lib64/cmake/LibDataChannel/LibDataChannelTargets-relwithdebinfo.cmake
/usr/lib64/cmake/LibDataChannel/LibDataChannelTargets.cmake
/usr/lib64/libdatachannel.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdatachannel.so.0.21
/usr/lib64/libdatachannel.so.0.21.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libdatachannel/9744cedce099f727b327cd9913a1fdc58a7f5599
