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
BUTTON_STATE = {
    "NORMAL" : 0,
    "FOCUS"  : 1,
    "PRESS"  : 2,
    "DISABLE": 3,
}

FLAG = 0
class XMButton(gtk.Button):
    def __init__(self,png_src,on_click_cb,pos):
        gtk.Button.__init__(self)

        self.bt_state = "NORMAL"
        self.pos = pos

        self.connect("enter"    , self.on_ent)
        self.connect("leave"    , self.on_lea)
        self.connect("pressed"  , self.on_pre)
        self.connect("released" , self.on_rel)
        self.connect("clicked"  , on_click_cb)
        self.connect("expose_event",self.on_draw)

        self.set_app_paintable(True)

        self.read_png(png_src)

    def set_button_state(self,bs):
        lbs = self.get_button_state()
        if not bs in BUTTON_STATE:
            raise xmerr.XMButtonWrongState(bs)
        self.bt_state = bs

    def get_button_state(self):
        if not self.bt_state in BUTTON_STATE:
            raise xmerr.XMButtonWrongState(self.bt_state)

        return self.bt_state

    def read_png(self,png_src):
        pixbuf = gtk.gdk.pixbuf_new_from_file(png_src)
        ulen = pixbuf.get_width() / 4
        height = pixbuf.get_height()
        self.pixbufs = (
            pixbuf.subpixbuf(0,0,ulen,height),
            pixbuf.subpixbuf(ulen,0,ulen,height),
            pixbuf.subpixbuf(ulen*2,0,ulen,height),
            pixbuf.subpixbuf(ulen*3,0,ulen,height)
        )
        image = gtk.image_new_from_pixbuf(self.pixbufs[0])
        self.add(image)

    def on_draw(self,widget,event,data = None):
        cr = widget.window.cairo_create()
        pixbuf = self.pixbufs[BUTTON_STATE[self.get_button_state()]]
        cr.set_source_pixbuf(pixbuf,self.pos[0],self.pos[1])
        cr.paint()

        return True

    def on_ent(self,button):
        if self.bt_state == "DISABLE": return False
        self.set_button_state("FOCUS")

    def on_lea(self,button):
        if self.bt_state == "DISABLE": return False
        self.set_button_state("NORMAL")

    def on_pre(self,button):
        if self.bt_state == "DISABLE": return False
        self.set_button_state("PRESS")

    def on_rel(self,button):
        if self.bt_state == "DISABLE": return False
        self.set_button_state("NORMAL")
