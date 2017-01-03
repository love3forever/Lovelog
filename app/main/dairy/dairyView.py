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
from userModel import User, ImagePost, VideoPost

from dairyForm import ImagePostForm, VideoForm


def uploadFile(form=None, dbModel=None):
    form = form
    if form.validate_on_submit():
        file = request.files['data']
        uid = current_user.userid
        user = User.query(bson.objectid.ObjectId(str(uid)))
        post = dbModel()
        post.poster = user
        post.createdTime = datetime.today()
        post.data = form.data.data
        post.des = form.desc.data
        post.filename = file.filename
        print(form.data.name)
        post.save()


@login_required
@dairy.route('/imagedairy', methods=['GET', 'POST'])
def imagePost():
    form = ImagePostForm()
    uploadFile(form, ImagePost)
    return render_template('dairy/imagedairy.html', form=form)


@login_required
@dairy.route('/videodairy', methods=['GET', 'POST'])
def videoPost():
    '''
    this route is used to post video dairy to server
    '''
    form = VideoForm()
    uploadFile(form, VideoPost)
    return render_template('dairy/imagedairy.html', form=form)
