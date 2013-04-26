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
import xmnet

class XMUser:
    def __init__(self,usr = '',psw = ''):
        self.set_username(usr)
        self.set_password(psw)

    def login(self):
        req = xmnet.make_req(
            xmnet.URLS["login"],
            datas = {
                "done" : "/",
                "email" : self.get_username(),
                "password" : self.get_password(),
                "submit" : "登 录",
            }
        )
        lk = xmnet.XMNetLinker()
        lk.make_link(req)
        print lk.get_respbuf()

    def set_username(self,usr): self.usr = usr
    def set_password(self,psw): self.psw = psw

    def get_username(self): return self.usr
    def get_password(self): return self.psw

if __name__ == "__main__":
    import _accounts
    usr = XMUser(_accounts.usr,_accounts.psw)
    usr.login()
