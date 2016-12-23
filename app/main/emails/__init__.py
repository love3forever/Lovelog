#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-23 16:36:36
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Blueprint
userEmail = Blueprint('userEmail',__name__)

from . import userActive
