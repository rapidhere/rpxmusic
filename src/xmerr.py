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
import xmenv

class XMException(Exception):
    def __init__(self,info):
        Exception.__init__(self,info)
        self.info = info
    def FormatInfo(self): return "Error : %s" % self.info

# XMNetError : {
class XMNetError(XMException):
    def __init__(self,info): XMException.__init__(self,info)

class XMNoResponseError(XMNetError):
    def __init__(self): XMNetError.__init__(self,"Must make a link at first!")
# }

# XMPlayerError : {
class XMPlayerError(XMException):
    def __init__(self,info): XMException.__init__(self,info)

class XMNoPlaybin2Installed(XMPlayerError):
    def __init__(self) :
        XMPlayerError.__init__(self,"No plugin playbin2 Installed in your gstreamer")
# }
# XM_GError : {
class XM_GError(XMException):
    def __init__(self,info) : XMException.__init__(self,info)

## XMWindowError: {
class XMWindowError(XM_GError):
    def __init__(self,info) : XM_GError.__init__(self,info)

class XMSkinNotFound(XMWindowError):
    def __init__(self,skin_name):
        XMWindowError.__init__(self,"Skin  %s not found in %s!" % (skin_name,xmenv.SKIN_PATH))

class XMSkinLoadFailed(XMWindowError):
    def __init__(self,skin_name):
        XMWindowError.__init__(self,"Failed to load skin %s!" % skin_name)
## } XMElementError {
class XMElementError(XM_GError):
    def __init__(self,info) : XM_GError.__init__(self,info)

class XMElementWrongState(XMElementError):
    def __init__(self,e_el_state):
        XMElementError.__init__(self,"Wrong Element state %s!" % str(el_state))

class XMElementNoSource(XMElementError):
    def __init__(self):
        XMElementError.__init__(self,"No source was setted in this element!")

class XMCoverElementMustPixbuf(XMElementError):
    def __init__(self):
        XMElementError.__init__(self,"The source of CoverElement must be a pixbuf!")
## } XMButtonError {
class XMButtonError(XM_GError):
    def __init__(self,info) : XM_GError.__init__(self,info)

class XMButtonWrongState(XMButtonError):
    def __init__(self,e_bt_state):
        XMButtonError.__init__(self,"Wrong Button state %s!" % str(e_bt_state))
## }
# }
