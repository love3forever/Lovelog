#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-26 15:21:44
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from . import msg
from flask import render_template, url_for, redirect, flash
from flask_login import login_required, current_user
from msgRoom import MessageRoom

import sys
sys.path.append('..')
from extentions import socketio
from userModel import User, Pair


@login_required
@msg.route('/<string:username>')
def index(username):
    if username:
        user = User.objects(username=username).first()
        pair = Pair.query(user.userid).first()
        uid = pair.uid
        # print(type(socketio))
        try:
            socketio.on_namespace(MessageRoom('/{}'.format(uid)))
            print('chatroom:{} has been created'.format(uid))
            return render_template('message/msgIndex.html')
        except Exception as e:
            return str(e)
