#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-29 08:51:01
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import re
from flask_wtf import Form
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import Email, Required
from wtforms import validators


class ImagePostForm(Form):
    """docstring for InviteForm"""
    data = FileField('Image file')
    desc = TextAreaField('Image description')

    submit = SubmitField('Upload')


class VideoForm(Form):
    """docstring for VideoForm"""
    data = FileField('Video file')
    desc = TextAreaField('Video description')

    submit = SubmitField('Upload')
