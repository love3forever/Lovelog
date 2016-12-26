#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-26 15:52:56
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask_socketio import Namespace, emit
import sys
sys.path.append('..')
from extentions import socketio


class MessageRoom(Namespace):
    """docstring for MessageRoom"""

    def on_connect(self,data):
        print(data)

    def on_leave(self):
        print('client leave')

    def on_send(self, data):
        emit('response', data)

    def on_liaoxian(self,data):
    	print(data)



if __name__ == '__main__':
	socketio.on_namespace(MyCustomNamespace('/test'))