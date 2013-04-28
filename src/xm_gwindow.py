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
import xml.etree.ElementTree as ElementTree

import xmenv
import xmerr
import xm_gelement
import xm_gbutton

class XMWindow(gtk.Window):
    def __init__(self,skin = "default"):
        gtk.Window.__init__(self,gtk.WINDOW_POPUP)
        self.set_position(gtk.WIN_POS_CENTER)

        self.fixed = gtk.Fixed()
        self.add(self.fixed)
        self.set_app_paintable(True)

        self.button_list = {}
        self.element_list = {}
        self.load_skin(skin)

        self.connect("destroy",lambda w: gtk.main_quit())

        self.fixed.show()
        self.show()

    def load_skin(self,skin_name):
        import os
        skin_dir = xmenv.SKIN_PATH + "/" + skin_name
        if not os.path.isdir(skin_dir):
            raise xmerr.XMSkinNotFound(skin_name)

        try:
            el = ElementTree.parse(skin_dir + "/config.xml").getroot()
            self.load_background(skin_dir + "/" + el.findtext("background"))

            for bt in self.button_list:
                bt.destroy()

            self.button_list = {}
            self.element_list = {}
            for bt_conf in el.find("buttons"):
                pic = skin_dir + "/" + bt_conf.attrib["pic"]
                pos = [int(x) for x in bt_conf.attrib["pos"].split(",")]
                if bt_conf.tag == "pause":
                    self.load_button(pic,pos,bt_conf.tag,True)
                else:
                    self.load_button(pic,pos,bt_conf.tag)

            for el_conf in el.find("element"):
                pos = [int(x) for x in el_conf.attrib["pos"].split(",")]
                self.load_element(el_conf.tag,pos)

        except Exception:
            raise
            #raise xmerr.XMSkinLoadFailed(skin_name)

    def load_background(self,background_src):
        pixbuf = gtk.gdk.pixbuf_new_from_file(background_src)
        self.resize(pixbuf.get_width(),pixbuf.get_height())
        image = gtk.image_new_from_pixbuf(pixbuf)
        self.fixed.put(image,0,0)
        image.show()

    def load_button(self,png_src,pos,button_name,hide = False):
        BUTTON_CBS = {
            "close"      : self.button_close_cb,
            "play"       : self.button_play_cb,
            "next"       : self.button_next_cb,
            "previous"   : self.button_previous_cb,
            "pause"      : self.button_pause_cb,
            "download"   : self.button_download_cb,
        }
        if not button_name in BUTTON_CBS:
            raise ValueError(button_name)

        button = xm_gbutton.XMButton(png_src,BUTTON_CBS[button_name],pos)
        self.fixed.put(button,pos[0],pos[1])
        if hide:
            button.hide_all()
        else:
            button.show_all()
        self.button_list[button_name] = button

    def load_element(self,tag_name,pos):
        ELEMENT_NAME_LIST = (
            "cover",
        )
        if not tag_name in ELEMENT_NAME_LIST:
            raise ValueError(tag_name)
        cel = xm_gelement.XMCoverElement()
        self.fixed.put(cel,pos[0],pos[1])
        cel.show()
        self.element_list[tag_name] = cel

    def button_close_cb(self,button):
        gtk.main_quit()

    def button_play_cb(self,button): pass
    def button_next_cb(self,button): pass
    def button_previous_cb(self,button): pass
    def button_pause_cb(self,button): pass
    def button_download_cb(self,button): pass

if __name__ == "__main__":
    win = XMWindow("StarCraftII")
    gtk.main()
