#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-26 15:52:56
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask_socketio import Namespace, emit
import sys


class MessageRoom(Namespace):
    """docstring for MessageRoom"""

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(MessageRoom, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def on_connect(self):
        print("connection from client")
        self.emit('liaoxian', "msg")

    def on_leave(self):
        print('client leave')

    def on_send(self, data):
        emit('response', data)

    def on_liaoxian(self, data):
        print(data)
        emit(data)
