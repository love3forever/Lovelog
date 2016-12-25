#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-25 19:16:37
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Email, Required


class InviteForm(Form):
    """docstring for InviteForm"""
    email = StringField('Email', validators=[Email(), Required()])
    submit = SubmitField('Send Invite')