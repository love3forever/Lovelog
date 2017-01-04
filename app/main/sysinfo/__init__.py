#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-04 09:20:33
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Blueprint

sysinfo = Blueprint('sysinfo',__name__)


from . import sysinfoView
