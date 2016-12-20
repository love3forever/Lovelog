#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 21:53:46
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Blueprint
login = Blueprint('login', __name__)

from . import userLogin