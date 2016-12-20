#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 16:39:04
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from . import db


class Message(db.Document):
    """docstring for Message"""
    fromUser = db.StringField(required=True, max_length=15)
    toUser = db.StringField(required=True, max_length=15)

    content = db.StringField(required=True, max_length=140)
    date = db.DateTimeField()
