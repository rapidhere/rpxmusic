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
import xmenv
import xm_gbutton

class XMWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self,gtk.WINDOW_POPUP)
        self.set_position(gtk.WIN_POS_CENTER)

        self.fixed = gtk.Fixed()
        self.add(self.fixed)

        self.load_background(xmenv.SKIN_PATH + "/default/back.png")
        self.load_button(xmenv.SKIN_PATH + "/default/close.png",(0,0),self.button_close_cb)

        self.set_app_paintable(True)
        self.connect("destroy",lambda w: gtk.main_quit())
        self.show_all()

    def load_background(self,background_src):
        pixbuf = gtk.gdk.pixbuf_new_from_file(background_src)
        self.resize(pixbuf.get_width(),pixbuf.get_height())
        image = gtk.image_new_from_pixbuf(pixbuf)
        self.fixed.put(image,0,0)

    def load_button(self,png_src,pos,on_click_cb):
        button = xm_gbutton.XMButton(png_src,on_click_cb,pos)
        self.fixed.put(button,pos[0],pos[1])

    def button_close_cb(self,button):
        gtk.main_quit()

if __name__ == "__main__":
    win = XMWindow()
    gtk.main()
