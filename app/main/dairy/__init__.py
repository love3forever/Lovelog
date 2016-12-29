#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-29 08:49:21
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : 0.01
from flask import Blueprint

dairy = Blueprint('dairy',__name__)

from . import dairyView
