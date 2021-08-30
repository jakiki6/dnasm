#!/bin/bash

rm -fr build 2>  /dev/null

mkdir build
cd build

mkdir DEBIAN
cat << EOF > DEBIAN/control
Package: dnasm
Version: 1.0
Section: custom
Priority: optional
Architecture: all
Essential: no
Maintainer: Jakiki6
Depends: python3, python3-requests
Description: Dnasm and tools build from commit $(git rev-parse HEAD | tr -d '\n')
EOF

mkdir opt
mkdir opt/dnasm
cp ../dnasm opt/dnasm/ -r
cp ../toolbox opt/dnasm/ -r
cp ../lib opt/dnasm/ -r
mkdir opt/dnasm/database
mkdir usr
mkdir usr/share
mkdir usr/share/dnasm
cp ../database usr/share/dnasm/ -r
rm -fr usr/share/dnasm/database/.git
rm usr/share/dnasm/database/LICENSE
mkdir usr/bin
ln -s /opt/dnasm/dnasm/dnasm.py usr/bin/dnasm
ln -s /opt/dnasm/dnasm/dnash.py usr/bin/dnash
ln -s /opt/dnasm/toolbox/toolbox.py usr/bin/toolbox

cd ..
dpkg-deb --build build
mv build.deb dnasm.deb

rm -fr build
