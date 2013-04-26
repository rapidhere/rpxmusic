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
import urllib2
import cookielib
import urllib

import xmerr

HTTPHeader = {
    "Accept"            : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset"    : "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Language"   : "en-US,en;q=0.8",
    "Content-Type"      : "application/x-www-form-urlencoded",
    "User-Agent"        : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Ubuntu Chromium/25.0.1364.160 Chrome/25.0.1364.160 Safari/537.22",
    "Connection"        : "keep-alive",
    "Cache-Control"     : "max-age=0",
}

URLS = {
    "login"         : "http://www.xiami.com/member/login",
    "song-xml"      : "http://www.xiami.com/song/playlist/id/%d/object_name/default/object_id/0",
}

ckjar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))

def make_req(url,datas,headers = HTTPHeader):
    return urllib2.Request(
        url = url,
        headers = headers,
        data = urllib.urlencode(datas)
    )

class XMNetLinker:
    def __init__(self): pass

    def make_link(self,req):
        self.resp = opener.open(req)

    def get_respinfo(self):
        if not hasattr(self,'resp'):
            raise xmerr.XMNoResponseError()
        return self.resp.info().dict

    def get_respmsg(self):
        if not hasattr(self,'resp'):
            raise xmerr.XMNoResponseError()
        return self.resp.msg

    def get_respcode(self):
        if not hasattr(self,'resp'):
            raise xmerr.XMNoResponseError()
        return self.resp.code

    def get_respbuf(self):
        if not hasattr(self,'resp'):
            raise xmerr.XMNoResponseError()
        return self.resp.read()
