#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-23 16:36:47
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import bson
from . import userEmail
from flask import url_for, render_template, redirect
from flask_login import current_user
import sys
sys.path.extend('..')
from userModel import User
from smtpMail import sendMail


@userEmail.route('/active/<string:uid>', methods=['GET'])
def active(uid):
    if uid:
        user = User.query(bson.objectid.ObjectId(str(uid)))
        if not user or user.is_authenticated:
            return redirect(url_for('index.indexPage'))
        user.update(isauthenticated=True)
        return redirect(url_for('index.indexPage'))


@userEmail.route('/sendemail', methods=['GET'])
def sendEmail():
    if current_user:
        uid = current_user.userid
        email = current_user.email
        if sendMail(uid, email):
            return 'Mail has been sent already'
        return 'Someting wrong happened'
