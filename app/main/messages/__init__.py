#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-26 15:21:26
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Blueprint
msg = Blueprint('msg', __name__)

from . import instanceMsg
