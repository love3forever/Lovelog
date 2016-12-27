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
        try:
            if not socketio.server:
                return render_template('message/msgIndex.html')
            if socketio.server.namespace_handlers.has_key('/{}'.format(uid)):
                print('room has created')
            else:
                socketio.on_namespace(MessageRoom('/{}'.format(uid)))
                print('new room created')
            return render_template('message/msgIndex.html')
        except Exception as e:
            print(str(e))
