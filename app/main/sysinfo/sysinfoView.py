#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-04 09:21:43
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import render_template, redirect, url_for, flash, abort, jsonify
from flask_login import current_user, login_required
from . import sysinfo

import sys
sys.path.append('..')

from userModel import SysInfo, User


@login_required
@sysinfo.route('/index')
def getSysinfoIndex():
    uid = current_user.userid
    user = User.getUserbyID(uid)

    if user:
        infos = SysInfo.objects(awaredof__in=[user])
        return render_template('sysinfo/index.html', infos=infos)
    else:
        return render_template('sysinfo/index.html')


@login_required
@sysinfo.route('/msgstatus')
def getInfoStatus():
    uid = current_user.userid
    user = User.getUserbyID(uid)

    infos = SysInfo.objects(awaredof__in=[user])
    return jsonify({'count': len(infos)})
