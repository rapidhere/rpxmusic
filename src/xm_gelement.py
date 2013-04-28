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
import pygtk
pygtk.require("2.0")
import gtk
import cairo

import xmenv
import xmerr

ELEMENT_STATE = {
    "WAITING": 0,
    "LOADING": 1,
    "NORMAL" : 2
}

class XMElement:
    def __init__(self):
        self.el_state = ''

    def set_element_state(self,el_state):
        if not el_state in ELEMENT_STATE:
            raise xmerr.XMElementWrongState(el_state)
        self.el_state = el_state

    def get_element_state(self):
        if not self.el_state in ELEMENT_STATE:
            raise xmerr.XMElementWrongState(self.el_state)
        return self.el_state

    def set_source(self,src): self.src = src
    def get_source(self):
        if not hasattr(self,"src"):
            raise xmerr.XMElementNoSource()
        return self.src

class XMCoverElement(gtk.Image,XMElement):
    def __init__(self):
        gtk.Image.__init__(self)
        XMElement.__init__(self)
        self.set_element_state("WAITING")

        self.connect("expose-event",self.on_draw)
        self.set_app_paintable(True)

    def on_draw(self,widget,event,data = None):
        if self.get_element_state() == "WAITING":
            self.set_from_file(xmenv.DATA_PATH + '/cover_wait.png')
        elif self.get_element_state() == "LOADING":
            self.set_from_file(xmenv.DATA_PATH + '/cover_load.png')
        elif self.get_element_state() == "NORMAL":
            self.set_from_file(self.get_source())

        return False

    def set_src(self,src):
        if not isinstance(src,gtk.gdk.Pixbuf):
            raise xmerr.XMCoverElementMustPixbuf()
        XMElement.set_src(self,src)
