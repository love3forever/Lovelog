#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 19:31:00
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from . import index
from flask import render_template
from flask_login import current_user


@index.route('/')
def indexPage():
    if current_user.is_authenticated:
        return render_template('base.html')
    else:
        return render_template('index.html')
