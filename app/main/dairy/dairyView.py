#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-29 08:51:16
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import bson
from datetime import datetime

from flask import Flask, flash, url_for, redirect, render_template, request
from flask_login import current_user, login_required
from . import dairy

import sys
sys.path.append('..')
from userModel import User, ImagePost

from dairyForm import ImagePostForm


@login_required
@dairy.route('/imagedairy', methods=['GET', 'POST'])
def imagePost():
    form = ImagePostForm()
    if form.validate_on_submit():
        img = form.image.data
        uid = current_user.userid
        user = User.query(bson.objectid.ObjectId(str(uid)))
        post = ImagePost()
        post.poster = user
        post.createdTime = datetime.today()
        post.img = img
        post.des = form.desc.data

        post.save()
    return render_template('dairy/imagedairy.html', form=form)
