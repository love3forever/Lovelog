#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 19:29:34
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Blueprint

index = Blueprint('index', __name__)

from . import indexRouter
