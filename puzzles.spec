#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: eaa4f711da30
#
Name     : puzzles
Version  : 20240802.1c1899e
Release  : 4
URL      : https://www.chiark.greenend.org.uk/~sgtatham/puzzles/puzzles-20240802.1c1899e.tar.gz
Source0  : https://www.chiark.greenend.org.uk/~sgtatham/puzzles/puzzles-20240802.1c1899e.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: puzzles-data = %{version}-%{release}
Requires: puzzles-libexec = %{version}-%{release}
Requires: puzzles-license = %{version}-%{release}
BuildRequires : ImageMagick
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(gtk+-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
puzzle collection. The collection's web site is at
<https://www.chiark.greenend.org.uk/~sgtatham/puzzles/>.

%package data
Summary: data components for the puzzles package.
Group: Data

%description data
data components for the puzzles package.


%package libexec
Summary: libexec components for the puzzles package.
Group: Default
Requires: puzzles-license = %{version}-%{release}

%description libexec
libexec components for the puzzles package.


%package license
Summary: license components for the puzzles package.
Group: Default

%description license
license components for the puzzles package.


%prep
%setup -q -n puzzles-20240802.1c1899e
cd %{_builddir}/puzzles-20240802.1c1899e

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722968445
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
%cmake .. -DBUILD_SHARED_LIBS:BOOL=OFF  -G 'Unix Makefiles'
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
export SOURCE_DATE_EPOCH=1722968445
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/puzzles
cp %{_builddir}/puzzles-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/puzzles/83dd1f1e328493436aca627060881441137795bc || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
# Move puzzle binaries to a non-conflicting location
mkdir -p %{buildroot}/usr/libexec/puzzles
mv %{buildroot}/usr/bin/* %{buildroot}/usr/libexec/puzzles/

# Adjust desktop application files to point to relocated binaries
for desktop in %{buildroot}/usr/share/applications/*.desktop; do
sed -i 's|^\(Exec=\)\(.*\)|\1/usr/libexec/puzzles/\2|' "${desktop}"
done
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/blackbox.desktop
/usr/share/applications/bridges.desktop
/usr/share/applications/cube.desktop
/usr/share/applications/dominosa.desktop
/usr/share/applications/fifteen.desktop
/usr/share/applications/filling.desktop
/usr/share/applications/flip.desktop
/usr/share/applications/flood.desktop
/usr/share/applications/galaxies.desktop
/usr/share/applications/guess.desktop
/usr/share/applications/inertia.desktop
/usr/share/applications/keen.desktop
/usr/share/applications/lightup.desktop
/usr/share/applications/loopy.desktop
/usr/share/applications/magnets.desktop
/usr/share/applications/map.desktop
/usr/share/applications/mines.desktop
/usr/share/applications/mosaic.desktop
/usr/share/applications/net.desktop
/usr/share/applications/netslide.desktop
/usr/share/applications/palisade.desktop
/usr/share/applications/pattern.desktop
/usr/share/applications/pearl.desktop
/usr/share/applications/pegs.desktop
/usr/share/applications/range.desktop
/usr/share/applications/rect.desktop
/usr/share/applications/samegame.desktop
/usr/share/applications/signpost.desktop
/usr/share/applications/singles.desktop
/usr/share/applications/sixteen.desktop
/usr/share/applications/slant.desktop
/usr/share/applications/solo.desktop
/usr/share/applications/tents.desktop
/usr/share/applications/towers.desktop
/usr/share/applications/tracks.desktop
/usr/share/applications/twiddle.desktop
/usr/share/applications/undead.desktop
/usr/share/applications/unequal.desktop
/usr/share/applications/unruly.desktop
/usr/share/applications/untangle.desktop
/usr/share/icons/hicolor/128x128/apps/blackbox.png
/usr/share/icons/hicolor/128x128/apps/bridges.png
/usr/share/icons/hicolor/128x128/apps/cube.png
/usr/share/icons/hicolor/128x128/apps/dominosa.png
/usr/share/icons/hicolor/128x128/apps/fifteen.png
/usr/share/icons/hicolor/128x128/apps/filling.png
/usr/share/icons/hicolor/128x128/apps/flip.png
/usr/share/icons/hicolor/128x128/apps/flood.png
/usr/share/icons/hicolor/128x128/apps/galaxies.png
/usr/share/icons/hicolor/128x128/apps/guess.png
/usr/share/icons/hicolor/128x128/apps/inertia.png
/usr/share/icons/hicolor/128x128/apps/keen.png
/usr/share/icons/hicolor/128x128/apps/lightup.png
/usr/share/icons/hicolor/128x128/apps/loopy.png
/usr/share/icons/hicolor/128x128/apps/magnets.png
/usr/share/icons/hicolor/128x128/apps/map.png
/usr/share/icons/hicolor/128x128/apps/mines.png
/usr/share/icons/hicolor/128x128/apps/mosaic.png
/usr/share/icons/hicolor/128x128/apps/net.png
/usr/share/icons/hicolor/128x128/apps/netslide.png
/usr/share/icons/hicolor/128x128/apps/palisade.png
/usr/share/icons/hicolor/128x128/apps/pattern.png
/usr/share/icons/hicolor/128x128/apps/pearl.png
/usr/share/icons/hicolor/128x128/apps/pegs.png
/usr/share/icons/hicolor/128x128/apps/range.png
/usr/share/icons/hicolor/128x128/apps/rect.png
/usr/share/icons/hicolor/128x128/apps/samegame.png
/usr/share/icons/hicolor/128x128/apps/signpost.png
/usr/share/icons/hicolor/128x128/apps/singles.png
/usr/share/icons/hicolor/128x128/apps/sixteen.png
/usr/share/icons/hicolor/128x128/apps/slant.png
/usr/share/icons/hicolor/128x128/apps/solo.png
/usr/share/icons/hicolor/128x128/apps/tents.png
/usr/share/icons/hicolor/128x128/apps/towers.png
/usr/share/icons/hicolor/128x128/apps/tracks.png
/usr/share/icons/hicolor/128x128/apps/twiddle.png
/usr/share/icons/hicolor/128x128/apps/undead.png
/usr/share/icons/hicolor/128x128/apps/unequal.png
/usr/share/icons/hicolor/128x128/apps/unruly.png
/usr/share/icons/hicolor/128x128/apps/untangle.png
/usr/share/icons/hicolor/16x16/apps/blackbox.png
/usr/share/icons/hicolor/16x16/apps/bridges.png
/usr/share/icons/hicolor/16x16/apps/cube.png
/usr/share/icons/hicolor/16x16/apps/dominosa.png
/usr/share/icons/hicolor/16x16/apps/fifteen.png
/usr/share/icons/hicolor/16x16/apps/filling.png
/usr/share/icons/hicolor/16x16/apps/flip.png
/usr/share/icons/hicolor/16x16/apps/flood.png
/usr/share/icons/hicolor/16x16/apps/galaxies.png
/usr/share/icons/hicolor/16x16/apps/guess.png
/usr/share/icons/hicolor/16x16/apps/inertia.png
/usr/share/icons/hicolor/16x16/apps/keen.png
/usr/share/icons/hicolor/16x16/apps/lightup.png
/usr/share/icons/hicolor/16x16/apps/loopy.png
/usr/share/icons/hicolor/16x16/apps/magnets.png
/usr/share/icons/hicolor/16x16/apps/map.png
/usr/share/icons/hicolor/16x16/apps/mines.png
/usr/share/icons/hicolor/16x16/apps/mosaic.png
/usr/share/icons/hicolor/16x16/apps/net.png
/usr/share/icons/hicolor/16x16/apps/netslide.png
/usr/share/icons/hicolor/16x16/apps/palisade.png
/usr/share/icons/hicolor/16x16/apps/pattern.png
/usr/share/icons/hicolor/16x16/apps/pearl.png
/usr/share/icons/hicolor/16x16/apps/pegs.png
/usr/share/icons/hicolor/16x16/apps/range.png
/usr/share/icons/hicolor/16x16/apps/rect.png
/usr/share/icons/hicolor/16x16/apps/samegame.png
/usr/share/icons/hicolor/16x16/apps/signpost.png
/usr/share/icons/hicolor/16x16/apps/singles.png
/usr/share/icons/hicolor/16x16/apps/sixteen.png
/usr/share/icons/hicolor/16x16/apps/slant.png
/usr/share/icons/hicolor/16x16/apps/solo.png
/usr/share/icons/hicolor/16x16/apps/tents.png
/usr/share/icons/hicolor/16x16/apps/towers.png
/usr/share/icons/hicolor/16x16/apps/tracks.png
/usr/share/icons/hicolor/16x16/apps/twiddle.png
/usr/share/icons/hicolor/16x16/apps/undead.png
/usr/share/icons/hicolor/16x16/apps/unequal.png
/usr/share/icons/hicolor/16x16/apps/unruly.png
/usr/share/icons/hicolor/16x16/apps/untangle.png
/usr/share/icons/hicolor/24x24/apps/blackbox.png
/usr/share/icons/hicolor/24x24/apps/bridges.png
/usr/share/icons/hicolor/24x24/apps/cube.png
/usr/share/icons/hicolor/24x24/apps/dominosa.png
/usr/share/icons/hicolor/24x24/apps/fifteen.png
/usr/share/icons/hicolor/24x24/apps/filling.png
/usr/share/icons/hicolor/24x24/apps/flip.png
/usr/share/icons/hicolor/24x24/apps/flood.png
/usr/share/icons/hicolor/24x24/apps/galaxies.png
/usr/share/icons/hicolor/24x24/apps/guess.png
/usr/share/icons/hicolor/24x24/apps/inertia.png
/usr/share/icons/hicolor/24x24/apps/keen.png
/usr/share/icons/hicolor/24x24/apps/lightup.png
/usr/share/icons/hicolor/24x24/apps/loopy.png
/usr/share/icons/hicolor/24x24/apps/magnets.png
/usr/share/icons/hicolor/24x24/apps/map.png
/usr/share/icons/hicolor/24x24/apps/mines.png
/usr/share/icons/hicolor/24x24/apps/mosaic.png
/usr/share/icons/hicolor/24x24/apps/net.png
/usr/share/icons/hicolor/24x24/apps/netslide.png
/usr/share/icons/hicolor/24x24/apps/palisade.png
/usr/share/icons/hicolor/24x24/apps/pattern.png
/usr/share/icons/hicolor/24x24/apps/pearl.png
/usr/share/icons/hicolor/24x24/apps/pegs.png
/usr/share/icons/hicolor/24x24/apps/range.png
/usr/share/icons/hicolor/24x24/apps/rect.png
/usr/share/icons/hicolor/24x24/apps/samegame.png
/usr/share/icons/hicolor/24x24/apps/signpost.png
/usr/share/icons/hicolor/24x24/apps/singles.png
/usr/share/icons/hicolor/24x24/apps/sixteen.png
/usr/share/icons/hicolor/24x24/apps/slant.png
/usr/share/icons/hicolor/24x24/apps/solo.png
/usr/share/icons/hicolor/24x24/apps/tents.png
/usr/share/icons/hicolor/24x24/apps/towers.png
/usr/share/icons/hicolor/24x24/apps/tracks.png
/usr/share/icons/hicolor/24x24/apps/twiddle.png
/usr/share/icons/hicolor/24x24/apps/undead.png
/usr/share/icons/hicolor/24x24/apps/unequal.png
/usr/share/icons/hicolor/24x24/apps/unruly.png
/usr/share/icons/hicolor/24x24/apps/untangle.png
/usr/share/icons/hicolor/32x32/apps/blackbox.png
/usr/share/icons/hicolor/32x32/apps/bridges.png
/usr/share/icons/hicolor/32x32/apps/cube.png
/usr/share/icons/hicolor/32x32/apps/dominosa.png
/usr/share/icons/hicolor/32x32/apps/fifteen.png
/usr/share/icons/hicolor/32x32/apps/filling.png
/usr/share/icons/hicolor/32x32/apps/flip.png
/usr/share/icons/hicolor/32x32/apps/flood.png
/usr/share/icons/hicolor/32x32/apps/galaxies.png
/usr/share/icons/hicolor/32x32/apps/guess.png
/usr/share/icons/hicolor/32x32/apps/inertia.png
/usr/share/icons/hicolor/32x32/apps/keen.png
/usr/share/icons/hicolor/32x32/apps/lightup.png
/usr/share/icons/hicolor/32x32/apps/loopy.png
/usr/share/icons/hicolor/32x32/apps/magnets.png
/usr/share/icons/hicolor/32x32/apps/map.png
/usr/share/icons/hicolor/32x32/apps/mines.png
/usr/share/icons/hicolor/32x32/apps/mosaic.png
/usr/share/icons/hicolor/32x32/apps/net.png
/usr/share/icons/hicolor/32x32/apps/netslide.png
/usr/share/icons/hicolor/32x32/apps/palisade.png
/usr/share/icons/hicolor/32x32/apps/pattern.png
/usr/share/icons/hicolor/32x32/apps/pearl.png
/usr/share/icons/hicolor/32x32/apps/pegs.png
/usr/share/icons/hicolor/32x32/apps/range.png
/usr/share/icons/hicolor/32x32/apps/rect.png
/usr/share/icons/hicolor/32x32/apps/samegame.png
/usr/share/icons/hicolor/32x32/apps/signpost.png
/usr/share/icons/hicolor/32x32/apps/singles.png
/usr/share/icons/hicolor/32x32/apps/sixteen.png
/usr/share/icons/hicolor/32x32/apps/slant.png
/usr/share/icons/hicolor/32x32/apps/solo.png
/usr/share/icons/hicolor/32x32/apps/tents.png
/usr/share/icons/hicolor/32x32/apps/towers.png
/usr/share/icons/hicolor/32x32/apps/tracks.png
/usr/share/icons/hicolor/32x32/apps/twiddle.png
/usr/share/icons/hicolor/32x32/apps/undead.png
/usr/share/icons/hicolor/32x32/apps/unequal.png
/usr/share/icons/hicolor/32x32/apps/unruly.png
/usr/share/icons/hicolor/32x32/apps/untangle.png
/usr/share/icons/hicolor/44x44/apps/blackbox.png
/usr/share/icons/hicolor/44x44/apps/bridges.png
/usr/share/icons/hicolor/44x44/apps/cube.png
/usr/share/icons/hicolor/44x44/apps/dominosa.png
/usr/share/icons/hicolor/44x44/apps/fifteen.png
/usr/share/icons/hicolor/44x44/apps/filling.png
/usr/share/icons/hicolor/44x44/apps/flip.png
/usr/share/icons/hicolor/44x44/apps/flood.png
/usr/share/icons/hicolor/44x44/apps/galaxies.png
/usr/share/icons/hicolor/44x44/apps/guess.png
/usr/share/icons/hicolor/44x44/apps/inertia.png
/usr/share/icons/hicolor/44x44/apps/keen.png
/usr/share/icons/hicolor/44x44/apps/lightup.png
/usr/share/icons/hicolor/44x44/apps/loopy.png
/usr/share/icons/hicolor/44x44/apps/magnets.png
/usr/share/icons/hicolor/44x44/apps/map.png
/usr/share/icons/hicolor/44x44/apps/mines.png
/usr/share/icons/hicolor/44x44/apps/mosaic.png
/usr/share/icons/hicolor/44x44/apps/net.png
/usr/share/icons/hicolor/44x44/apps/netslide.png
/usr/share/icons/hicolor/44x44/apps/palisade.png
/usr/share/icons/hicolor/44x44/apps/pattern.png
/usr/share/icons/hicolor/44x44/apps/pearl.png
/usr/share/icons/hicolor/44x44/apps/pegs.png
/usr/share/icons/hicolor/44x44/apps/range.png
/usr/share/icons/hicolor/44x44/apps/rect.png
/usr/share/icons/hicolor/44x44/apps/samegame.png
/usr/share/icons/hicolor/44x44/apps/signpost.png
/usr/share/icons/hicolor/44x44/apps/singles.png
/usr/share/icons/hicolor/44x44/apps/sixteen.png
/usr/share/icons/hicolor/44x44/apps/slant.png
/usr/share/icons/hicolor/44x44/apps/solo.png
/usr/share/icons/hicolor/44x44/apps/tents.png
/usr/share/icons/hicolor/44x44/apps/towers.png
/usr/share/icons/hicolor/44x44/apps/tracks.png
/usr/share/icons/hicolor/44x44/apps/twiddle.png
/usr/share/icons/hicolor/44x44/apps/undead.png
/usr/share/icons/hicolor/44x44/apps/unequal.png
/usr/share/icons/hicolor/44x44/apps/unruly.png
/usr/share/icons/hicolor/44x44/apps/untangle.png
/usr/share/icons/hicolor/48x48/apps/blackbox.png
/usr/share/icons/hicolor/48x48/apps/bridges.png
/usr/share/icons/hicolor/48x48/apps/cube.png
/usr/share/icons/hicolor/48x48/apps/dominosa.png
/usr/share/icons/hicolor/48x48/apps/fifteen.png
/usr/share/icons/hicolor/48x48/apps/filling.png
/usr/share/icons/hicolor/48x48/apps/flip.png
/usr/share/icons/hicolor/48x48/apps/flood.png
/usr/share/icons/hicolor/48x48/apps/galaxies.png
/usr/share/icons/hicolor/48x48/apps/guess.png
/usr/share/icons/hicolor/48x48/apps/inertia.png
/usr/share/icons/hicolor/48x48/apps/keen.png
/usr/share/icons/hicolor/48x48/apps/lightup.png
/usr/share/icons/hicolor/48x48/apps/loopy.png
/usr/share/icons/hicolor/48x48/apps/magnets.png
/usr/share/icons/hicolor/48x48/apps/map.png
/usr/share/icons/hicolor/48x48/apps/mines.png
/usr/share/icons/hicolor/48x48/apps/mosaic.png
/usr/share/icons/hicolor/48x48/apps/net.png
/usr/share/icons/hicolor/48x48/apps/netslide.png
/usr/share/icons/hicolor/48x48/apps/palisade.png
/usr/share/icons/hicolor/48x48/apps/pattern.png
/usr/share/icons/hicolor/48x48/apps/pearl.png
/usr/share/icons/hicolor/48x48/apps/pegs.png
/usr/share/icons/hicolor/48x48/apps/range.png
/usr/share/icons/hicolor/48x48/apps/rect.png
/usr/share/icons/hicolor/48x48/apps/samegame.png
/usr/share/icons/hicolor/48x48/apps/signpost.png
/usr/share/icons/hicolor/48x48/apps/singles.png
/usr/share/icons/hicolor/48x48/apps/sixteen.png
/usr/share/icons/hicolor/48x48/apps/slant.png
/usr/share/icons/hicolor/48x48/apps/solo.png
/usr/share/icons/hicolor/48x48/apps/tents.png
/usr/share/icons/hicolor/48x48/apps/towers.png
/usr/share/icons/hicolor/48x48/apps/tracks.png
/usr/share/icons/hicolor/48x48/apps/twiddle.png
/usr/share/icons/hicolor/48x48/apps/undead.png
/usr/share/icons/hicolor/48x48/apps/unequal.png
/usr/share/icons/hicolor/48x48/apps/unruly.png
/usr/share/icons/hicolor/48x48/apps/untangle.png
/usr/share/icons/hicolor/64x64/apps/blackbox.png
/usr/share/icons/hicolor/64x64/apps/bridges.png
/usr/share/icons/hicolor/64x64/apps/cube.png
/usr/share/icons/hicolor/64x64/apps/dominosa.png
/usr/share/icons/hicolor/64x64/apps/fifteen.png
/usr/share/icons/hicolor/64x64/apps/filling.png
/usr/share/icons/hicolor/64x64/apps/flip.png
/usr/share/icons/hicolor/64x64/apps/flood.png
/usr/share/icons/hicolor/64x64/apps/galaxies.png
/usr/share/icons/hicolor/64x64/apps/guess.png
/usr/share/icons/hicolor/64x64/apps/inertia.png
/usr/share/icons/hicolor/64x64/apps/keen.png
/usr/share/icons/hicolor/64x64/apps/lightup.png
/usr/share/icons/hicolor/64x64/apps/loopy.png
/usr/share/icons/hicolor/64x64/apps/magnets.png
/usr/share/icons/hicolor/64x64/apps/map.png
/usr/share/icons/hicolor/64x64/apps/mines.png
/usr/share/icons/hicolor/64x64/apps/mosaic.png
/usr/share/icons/hicolor/64x64/apps/net.png
/usr/share/icons/hicolor/64x64/apps/netslide.png
/usr/share/icons/hicolor/64x64/apps/palisade.png
/usr/share/icons/hicolor/64x64/apps/pattern.png
/usr/share/icons/hicolor/64x64/apps/pearl.png
/usr/share/icons/hicolor/64x64/apps/pegs.png
/usr/share/icons/hicolor/64x64/apps/range.png
/usr/share/icons/hicolor/64x64/apps/rect.png
/usr/share/icons/hicolor/64x64/apps/samegame.png
/usr/share/icons/hicolor/64x64/apps/signpost.png
/usr/share/icons/hicolor/64x64/apps/singles.png
/usr/share/icons/hicolor/64x64/apps/sixteen.png
/usr/share/icons/hicolor/64x64/apps/slant.png
/usr/share/icons/hicolor/64x64/apps/solo.png
/usr/share/icons/hicolor/64x64/apps/tents.png
/usr/share/icons/hicolor/64x64/apps/towers.png
/usr/share/icons/hicolor/64x64/apps/tracks.png
/usr/share/icons/hicolor/64x64/apps/twiddle.png
/usr/share/icons/hicolor/64x64/apps/undead.png
/usr/share/icons/hicolor/64x64/apps/unequal.png
/usr/share/icons/hicolor/64x64/apps/unruly.png
/usr/share/icons/hicolor/64x64/apps/untangle.png
/usr/share/icons/hicolor/88x88/apps/blackbox.png
/usr/share/icons/hicolor/88x88/apps/bridges.png
/usr/share/icons/hicolor/88x88/apps/cube.png
/usr/share/icons/hicolor/88x88/apps/dominosa.png
/usr/share/icons/hicolor/88x88/apps/fifteen.png
/usr/share/icons/hicolor/88x88/apps/filling.png
/usr/share/icons/hicolor/88x88/apps/flip.png
/usr/share/icons/hicolor/88x88/apps/flood.png
/usr/share/icons/hicolor/88x88/apps/galaxies.png
/usr/share/icons/hicolor/88x88/apps/guess.png
/usr/share/icons/hicolor/88x88/apps/inertia.png
/usr/share/icons/hicolor/88x88/apps/keen.png
/usr/share/icons/hicolor/88x88/apps/lightup.png
/usr/share/icons/hicolor/88x88/apps/loopy.png
/usr/share/icons/hicolor/88x88/apps/magnets.png
/usr/share/icons/hicolor/88x88/apps/map.png
/usr/share/icons/hicolor/88x88/apps/mines.png
/usr/share/icons/hicolor/88x88/apps/mosaic.png
/usr/share/icons/hicolor/88x88/apps/net.png
/usr/share/icons/hicolor/88x88/apps/netslide.png
/usr/share/icons/hicolor/88x88/apps/palisade.png
/usr/share/icons/hicolor/88x88/apps/pattern.png
/usr/share/icons/hicolor/88x88/apps/pearl.png
/usr/share/icons/hicolor/88x88/apps/pegs.png
/usr/share/icons/hicolor/88x88/apps/range.png
/usr/share/icons/hicolor/88x88/apps/rect.png
/usr/share/icons/hicolor/88x88/apps/samegame.png
/usr/share/icons/hicolor/88x88/apps/signpost.png
/usr/share/icons/hicolor/88x88/apps/singles.png
/usr/share/icons/hicolor/88x88/apps/sixteen.png
/usr/share/icons/hicolor/88x88/apps/slant.png
/usr/share/icons/hicolor/88x88/apps/solo.png
/usr/share/icons/hicolor/88x88/apps/tents.png
/usr/share/icons/hicolor/88x88/apps/towers.png
/usr/share/icons/hicolor/88x88/apps/tracks.png
/usr/share/icons/hicolor/88x88/apps/twiddle.png
/usr/share/icons/hicolor/88x88/apps/undead.png
/usr/share/icons/hicolor/88x88/apps/unequal.png
/usr/share/icons/hicolor/88x88/apps/unruly.png
/usr/share/icons/hicolor/88x88/apps/untangle.png
/usr/share/icons/hicolor/96x96/apps/blackbox.png
/usr/share/icons/hicolor/96x96/apps/bridges.png
/usr/share/icons/hicolor/96x96/apps/cube.png
/usr/share/icons/hicolor/96x96/apps/dominosa.png
/usr/share/icons/hicolor/96x96/apps/fifteen.png
/usr/share/icons/hicolor/96x96/apps/filling.png
/usr/share/icons/hicolor/96x96/apps/flip.png
/usr/share/icons/hicolor/96x96/apps/flood.png
/usr/share/icons/hicolor/96x96/apps/galaxies.png
/usr/share/icons/hicolor/96x96/apps/guess.png
/usr/share/icons/hicolor/96x96/apps/inertia.png
/usr/share/icons/hicolor/96x96/apps/keen.png
/usr/share/icons/hicolor/96x96/apps/lightup.png
/usr/share/icons/hicolor/96x96/apps/loopy.png
/usr/share/icons/hicolor/96x96/apps/magnets.png
/usr/share/icons/hicolor/96x96/apps/map.png
/usr/share/icons/hicolor/96x96/apps/mines.png
/usr/share/icons/hicolor/96x96/apps/mosaic.png
/usr/share/icons/hicolor/96x96/apps/net.png
/usr/share/icons/hicolor/96x96/apps/netslide.png
/usr/share/icons/hicolor/96x96/apps/palisade.png
/usr/share/icons/hicolor/96x96/apps/pattern.png
/usr/share/icons/hicolor/96x96/apps/pearl.png
/usr/share/icons/hicolor/96x96/apps/pegs.png
/usr/share/icons/hicolor/96x96/apps/range.png
/usr/share/icons/hicolor/96x96/apps/rect.png
/usr/share/icons/hicolor/96x96/apps/samegame.png
/usr/share/icons/hicolor/96x96/apps/signpost.png
/usr/share/icons/hicolor/96x96/apps/singles.png
/usr/share/icons/hicolor/96x96/apps/sixteen.png
/usr/share/icons/hicolor/96x96/apps/slant.png
/usr/share/icons/hicolor/96x96/apps/solo.png
/usr/share/icons/hicolor/96x96/apps/tents.png
/usr/share/icons/hicolor/96x96/apps/towers.png
/usr/share/icons/hicolor/96x96/apps/tracks.png
/usr/share/icons/hicolor/96x96/apps/twiddle.png
/usr/share/icons/hicolor/96x96/apps/undead.png
/usr/share/icons/hicolor/96x96/apps/unequal.png
/usr/share/icons/hicolor/96x96/apps/unruly.png
/usr/share/icons/hicolor/96x96/apps/untangle.png

%files libexec
%defattr(-,root,root,-)
/usr/libexec/puzzles/blackbox
/usr/libexec/puzzles/bridges
/usr/libexec/puzzles/cube
/usr/libexec/puzzles/dominosa
/usr/libexec/puzzles/fifteen
/usr/libexec/puzzles/filling
/usr/libexec/puzzles/flip
/usr/libexec/puzzles/flood
/usr/libexec/puzzles/galaxies
/usr/libexec/puzzles/guess
/usr/libexec/puzzles/inertia
/usr/libexec/puzzles/keen
/usr/libexec/puzzles/lightup
/usr/libexec/puzzles/loopy
/usr/libexec/puzzles/magnets
/usr/libexec/puzzles/map
/usr/libexec/puzzles/mines
/usr/libexec/puzzles/mosaic
/usr/libexec/puzzles/net
/usr/libexec/puzzles/netslide
/usr/libexec/puzzles/palisade
/usr/libexec/puzzles/pattern
/usr/libexec/puzzles/pearl
/usr/libexec/puzzles/pegs
/usr/libexec/puzzles/range
/usr/libexec/puzzles/rect
/usr/libexec/puzzles/samegame
/usr/libexec/puzzles/signpost
/usr/libexec/puzzles/singles
/usr/libexec/puzzles/sixteen
/usr/libexec/puzzles/slant
/usr/libexec/puzzles/solo
/usr/libexec/puzzles/tents
/usr/libexec/puzzles/towers
/usr/libexec/puzzles/tracks
/usr/libexec/puzzles/twiddle
/usr/libexec/puzzles/undead
/usr/libexec/puzzles/unequal
/usr/libexec/puzzles/unruly
/usr/libexec/puzzles/untangle

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/puzzles/83dd1f1e328493436aca627060881441137795bc
