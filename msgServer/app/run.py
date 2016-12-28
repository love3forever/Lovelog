#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-28 09:20:21
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask_socketio import SocketIO, Namespace, emit, send
from flask import Flask


class ChatRoom(Namespace):
    def on_connect(self):
        print('client connected to room')
        # emit('liaoxian', 'hhhh')

    def on_disconnect(self):
        print('client disconnected from room')

    def on_liaoxian(self, msg):
        print('running liaoxian')
        print(msg)
        self.send(msg)

    def on_recv(self, data):
        self.emit('liaoxian', data['msg'])


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wtf'
    return app


app = createApp()
socketio = SocketIO(app)


@socketio.on('message')
def getMsg(sss):
    print(sss)
    room = sss['msg']
    newRoom = ChatRoom('/{}'.format(room))
    socketio.on_namespace(newRoom)
    print(newRoom)
    print(socketio.server.namespace_handlers.keys())


@socketio.on('connect')
def getConn():
    print('client connected')

socketio.run(app, debug=True, host='0.0.0.0', port=4000)
