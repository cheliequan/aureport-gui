#! /bin/sh
set -x -e
autoreconf -fv --install
intltoolize --force --copy

#./configure --enable-Werror
