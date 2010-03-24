#-*- coding: utf-8 -*-
#!/usr/bin/env python

# Common utilities.
#
# Copyright (C) 2007 Red Hat, Inc.  All rights reserved.
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.  You should have
# received a copy of the GNU General Public License along with this program; if
# not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
# Floor, Boston, MA 02110-1301, USA.  Any Red Hat trademarks that are
# incorporated in the source code or documentation are not subject to the GNU
# General Public License and may only be used or replicated with the express
# permission of Red Hat, Inc.
#
# Red Hat Author: Miloslav Trmac <mitr@redhat.com>
import gettext

_ = lambda char: format_ch(gettext.gettext(char))


def format_ch(char, encode = 'utf-8'):
    if isinstance( char, str ):
        uni_char = unicode(char, encode)
    else:
        uni_char = char
    return uni_char
