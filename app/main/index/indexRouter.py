#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 19:31:00
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from . import index
from flask import render_template
from flask_login import current_user
import bson
from indexForms import InviteForm
import sys
sys.path.extend('..')
from userModel import Pair
from smtpMail import sendInvite


@index.route('/', methods=['GET', 'POST'])
def indexPage():
    # if current_user.is_authenticated:
    #     return render_template('base.html')
    # else:
    if current_user.is_authenticated:
        pair = Pair.query(bson.objectid.ObjectId(str(current_user.userid)))
        if not pair:
            form = InviteForm()
            if form.validate_on_submit():
                mailAddr = form.email.data
                uid = current_user.userid
                print(uid)
                sendInvite(uid, mailAddr)
                return 'Invite mail sent already'
            return render_template('index.html', form=form)
    return render_template('index.html')
