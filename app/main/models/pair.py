#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 19:07:39
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from . import db


class Pair(db.EmbeddedDocument):
    """docstring for Pair"""
    boyfirend = db.StringField(max_length=15)
    girlFirend = db.StringField(max_length=15)

    initDate = db.DateTimeField()
