%define tagname release_0_4_5

Summary:   SDL MPEG Library
Name:      smpeg
Version:   0.4.5
Release:   1%{dist}
License:   LGPL
Group:     System Environment/Libraries
Source:    https://github.com/Distrotech/smpeg/archive/%tagname.tar.gz
URL:       https://icculus.org/smpeg
BuildRequires: gcc-c++ SDL-devel subversion autoconf automake
Patch0:    smpeg-0.4.5-no_unsigned.patch
Patch1:    smpeg-0.4.5-format_security.patch

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 

%package devel
Summary: Libraries, includes and more to develop SMPEG applications.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 

This is the libraries, include files and other resources you can use
to develop SMPEG applications.

%package tools
Summary: Command line tools for working with %name
Group: Applications/Multimedia
Requires: %name = %version-%release

%description tools
Command line tools for working with %name

%package static
Summary: Libraries for linking statically to %name
Group: Development/Libraries
Requires: %name-devel = %version-%release

%description static
Libraries for linking statically to %name

%prep
%autosetup -n %name-%tagname

%build
./autogen.sh
%configure --with-sdl-prefix=%_prefix --disable-debug    \
           --disable-opengl-player --disable-gtk-player
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install

%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc CHANGES COPYING README
%{_libdir}/lib*.so.*
%{_libdir}/lib*.so

%files tools
%{_bindir}/plaympeg
%exclude %{_mandir}/man1/gtv*
%{_mandir}/man1/plaympeg*

%files devel
%{_bindir}/smpeg-config
%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%{_libdir}/lib*.a
%{_libdir}/lib*.la

%changelog
* Fri Mar  3 2000 Sam Lantinga <hercules@lokigames.com>
- Split package into development and runtime packages
