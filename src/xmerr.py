#!/usr/bin/python
#-*- coding: utf-8 -*-

# Copyright (C) 2013 rapidhere
#
# Author:     rapidhere <rapidhere@gmail.com>
# Maintainer: rapidhere <rapidhere@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class XMException(Exception):
    def __init__(self,info):
        Exception.__init__(self,info)
        self.info = info
    def FormatInfo(self): return "Error : %s" % self.info

class XMNetError(XMException):
    def __init__(self,info): XMException.__init__(self,info)

class XMNoResponseError(XMNetError):
    def __init__(self): XMNetError.__init__(self,"Must make a link at first!")

class XMPlayerError(XMException):
    def __init__(self,info): XMException.__init__(self.info)

class XMNoPlaybin2Installed(XMPlayerError):
    def __init__(self) : XMPlayerError.__init__(self,"No plugin playbin2 Installed in your gstreamer")
