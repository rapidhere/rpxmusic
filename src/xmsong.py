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

import xmnet,xmerr
import xml.etree.ElementTree as ElementTree
import math
import urllib
import sys

# Original Code from js

def _song_addr_decode(buf):
    fnum = int(buf[0])                  # loc2
    buf = buf[1:]                       # loc3
    k = int(math.floor(len(buf) / fnum))# loc4
    r = len(buf) % fnum                 # loc5
    arr = []                            # loc6

    for i in range(0,r):
        tmp = (k + 1) * i
        arr.append(buf[tmp : tmp + k + 1])

    for i in range(r,fnum):
        tmp = (k * (i - r)) + (k + 1) * r
        arr.append(buf[tmp : tmp + k])

    tmpStr = ""
    for i in range(0,len(arr[0])):
        for t in range(0,len(arr)):
            try:
                tmpStr += arr[t][i]
            except IndexError:
                tmpStr += ""

    tmpStr = urllib.unquote(tmpStr)
    ret = ""
    for ch in tmpStr:
        if ch == '^':
            ret += '0'
        else:
            ret += ch
    ret.replace("+"," ")
    return ret

class XMSong:
    def __init__(self,songid):
        self.set_songid(songid)

    def init_songinfo(self):
        req = xmnet.make_req(
            xmnet.URLS["song-xml"] % self.get_songid(),
            ""
        )
        lk = xmnet.XMNetLinker()
        lk.make_link(req)
        xml_buf = lk.get_respbuf()

        ns = "{http://xspf.org/ns/0/}"
        el = ElementTree.fromstring(xml_buf)
        t = el.find("%strackList/%strack" % (ns,ns))

        self.set_title(t.find("%stitle" % ns).text)
        self.set_albumid(t.find("%salbum_id" % ns).text)
        self.set_albumname(t.find("%salbum_name" % ns).text)
        self.set_artist(t.find("%sartist" % ns).text)
        self.set_lyrurl(t.find("%slyric" % ns).text)
        self.set_picurl(t.find("%spic" % ns).text)

        self.set_mp3url(
            _song_addr_decode(t.find("%slocation" % ns).text)
        )

    def set_picurl(self,url):       self.picurl = url
    def set_lyrurl(self,url):       self.lyrurl = url
    def set_mp3url(self,url):       self.mp3url = url
    def set_artist(self,artist):    self.artist = str(artist)
    def set_albumname(self,aln):    self.albumname = str(aln)
    def set_albumid(self,albumid):  self.albumid = int(albumid)
    def set_title(self,title):      self.title = str(title)
    def set_songid(self,songid):    self.songid = int(songid)

    def get_picurl(self):       return self.picurl
    def get_lyrurl(self):       return self.lyrurl
    def get_mp3url(self):       return self.mp3url
    def get_artist(self):       return self.artist
    def get_albumname(self):    return self.albumname
    def get_albumid(self):      return self.albumid
    def get_title(self):        return self.title
    def get_songid(self):       return self.songid

if __name__ == "__main__":
    xs = XMSong(1239160)
    xs.init_songinfo()
    print xs.get_mp3url()
