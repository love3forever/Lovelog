#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 19:31:00
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from . import index
from flask import render_template


@index.route('/')
def indexPage():
    return render_template('index.html')
