#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-23 16:36:47
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from . import userEmail
from flask import url_for, render_template, redirect
from flask_login import current_user
from smtpMail import sendMail


@userEmail.route('/active/<string:uid>', methods=['GET'])
def active(uid):
    if uid:
        pass


@userEmail.route('/sendemail', methods=['GET'])
def sendEmail():
    if current_user:
        uid = current_user.userid
        email = current_user.email
        sendMail(uid, email)
        return redirect(url_for('index.indexPage'))
