#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
AC_COPYRIGHT(
[Copyright (C) 2010 RedFlag, Inc.  All rights reserved.

This copyrighted material is made available to anyone wishing to use, modify,
copy, or redistribute it subject to the terms and conditions of the GNU General
Public License v.2.  This program is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY expressed or implied, including the implied
warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.  You should have received a copy of
the GNU General Public License along with this program; if not, write to the
Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.  Any RedFlag trademarks that are incorporated in the source
code or documentation are not subject to the GNU General Public License and may
only be used or replicated with the express permission of RedFlag, Inc.

RedFlag Author: cheliequan <cheliequan@redflag-linux.com>])

AC_PREREQ(2.59)
AC_INIT([aureport-gui], [1.0], [cheliequan@redflag-linux.com])
AM_INIT_AUTOMAKE([dist-bzip2 no-define subdir-objects -Wall])

# Checks for programs.
AM_PATH_PYTHON([2.4])
GETTEXT_PACKAGE=$PACKAGE
AC_SUBST([GETTEXT_PACKAGE])
ALL_LINGUAS="zh_CN"
IT_PROG_INTLTOOL
AC_PROG_INSTALL

localedir='${prefix}/${DATADIRNAME}/locale'
AC_SUBST(localedir)

# Checks for libraries.
AM_GNU_GETTEXT([external])
AM_GNU_GETTEXT_VERSION([0.14.6])

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([Makefile qtstuff-po/Makefile src/Makefile po/Makefile.in],[AM_POSTPROCESS_PO_MAKEFILE])
AC_OUTPUT
