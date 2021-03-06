#
# Spec file for package d2x.
#
Name:          d2x
Version:       0.2.5
Release:       1
Copyright:     Freely Redistributable
Packager:      bradleyb@u.washington.edu

Group:         Contrib/Games
Summary:       The port of Descent 2 Version 1.2 for Linux.
Provides:      d2x, descent2

URL:           http://shelob.classrooms.washington.edu/d2x/
Source:        d2x-%{version}.tar.gz
BuildRoot:     /var/tmp/%name-buildroot

%description
This is the port of Descent 2 Version 1.2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need the datafiles from the Retail version
of Descent 2 Version 1.2 installed in /usr/share/games/descent2.

%package -n d2x-sdl
Group:         Contrib/Games
Summary:       Descent 2 Version 1.2 for Linux, SDL version.
Provides:      d2x-sdl
Requires:      d2x

%description -n d2x-sdl
This is the port of Descent 2 Version 1.2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need the datafiles from the Retail version
of Descent 2 Version 1.2 installed in /usr/share/games/descent2.

This version uses SDL for Audio, Input/Output and graphics rendering.

%package -n d2x-gl
Group:         Contrib/Games
Summary:       Descent 2 Version 1.2 for Linux, OpenGL version.
Provides:      d2x-gl
Requires:      d2x

%description -n d2x-gl
This is the port of Descent 2 Version 1.2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need the datafiles from the Retail version
of Descent 2 Version 1.2 installed in /usr/share/games/descent2.

This version uses SDL for Audio and Input/Output and OpenGL for graphics
rendering.

%prep
%setup -q -n d2x*
#./autogen.sh

%build
# d2x-sdl
%configure --with-sharepath=/usr/share/games/descent2 --disable-debug
make
mv d2x-sdl d2x-sdl.real
# d2x-gl
make clean
rm -f config.cache
# Tell configure where to find libGLU (nonstandard location).
export LDFLAGS="${LDFLAGS} -L/usr/X11R6/lib"
%configure --with-sharepath=/usr/share/games/descent2 --with-opengl \
	--disable-debug
# Tell make where to link libGLU (nonstandard location).
make LDFLAGS="${LDFLAGS} -L /usr/X11R6/lib"
mv d2x-gl d2x-gl.real

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/games/
mkdir -p $RPM_BUILD_ROOT/usr/share/games/descent2/missions/
install -m 755 d2x-sdl.sh $RPM_BUILD_ROOT/usr/games/d2x-sdl
install -m 755 d2x-gl.sh $RPM_BUILD_ROOT/usr/games/d2x-gl
install d2x-sdl.real $RPM_BUILD_ROOT/usr/games/
install d2x-gl.real $RPM_BUILD_ROOT/usr/games/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS INSTALL COPYING AUTHORS
%doc readme.txt cvshowto.txt license.txt compilerdefs.txt
%doc installation.txt mingw32.txt
%dir /usr/share/games/descent2
%dir /usr/share/games/descent2/missions

%files -n d2x-sdl
%defattr(-,root,root)
/usr/games/d2x-sdl
/usr/games/d2x-sdl.real

%files -n d2x-gl
%defattr(-,root,root)
/usr/games/d2x-gl
/usr/games/d2x-gl.real

%changelog
* Tue Feb  7 2002 - Paolo Ulivi <pulivi@libero.it>
- New SPEC version for inclusion in d2x/rpm (CVS)
* Wed Nov 14 2001 - Paolo Ulivi <paoloulivi@tin.it>
- New upstream version 0.1.2 (CVS) dated 11 Nov 2001
* Sat Oct 13 2001 - Paolo Ulivi <paoloulivi@tin.it>
- Release 1mdk of D2X Version 0.1.0 for Mandrake 8.0
