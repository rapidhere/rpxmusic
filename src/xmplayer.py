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
import pygst
pygst.require("0.10")
import gst
import math

import xmerr

class XMPlayer:
    def __init__(self,about_to_finish_cb):
        try:
            self.player = gst.element_factory_make("playbin2",None)
        except gst.ElementNotFoundError:
            raise xmerr.XMNoPlaybin2Installed()

        try:
            fakesink = gst.element_factory_make("fakesink",None)
            self.player.set_property("video-sink",fakesink)
            bus = self.player.get_bus()
            bus.add_watch(self.bus_signal_watcher)
        except Exception:
            raise
            #raise xmerr.XMPlayerInitFailed()

        self.pause_flag = False

        self.player.set_state(gst.STATE_READY)
        self.about_to_finish_cb = about_to_finish_cb

    def play(self,uri):
        self.player.set_property("uri",uri)
        self.player.set_state(gst.STATE_PLAYING)

        self.pause_flag = False

    def stop(self):
        self.player.set_state(gst.STATE_READY)
        self.pause_flag = False

    def next(self,uri):
        self.player.set_state(gst.STATE_READY)
        self.play(uri)

    def pause(self):
        if self.pause_flag:
            return
        self.pause_flag = True
        self.player.set_state(gst.STATE_PAUSED)

    def unpause(self):
        if not self.pause_flag:
            return
        self.pause_flag = False
        self.player.set_state(gst.STATE_PLAYING)

    def get_vol(self):
        vol = self.player.get_property("volume")
        vol = int(round(100.0 * vol / 5.0))
        return vol

    def set_vol(self,vol):
        vol = float(vol) * 5.0 / 100.0
        self.player.set_property("volume",vol)

    def get_pos(self):
        return self.player.query_position(gst.FORMAT_TIME,None)[0]

    def get_dur(self):
        return self.player.query_duration(gst.FORMAT_TIME,None)[0]

    def bus_signal_watcher(self,bus,msg):
        msg_t = msg.type
        if msg_t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_READY)
            self.about_to_finish_cb()
        elif msg_t == gst.MESSAGE_ERROR:
            self.player.set_state(gst.STATE_NULL)
            err,debug = msg.parse_error()
            raise xmerr.XMGSTRuntimeError("%s %s" % (err,debug))
            return False
        return True

if __name__ == "__main__":
    import gtk,time,sys
    uri = "file:///home/rapid/Desktop/repository/rpxmusic/src/a.mp3"
    def cb(data = None):
        xp.play(uri)
    xp = XMPlayer(cb)
    xp.play(uri)
    gtk.main()
