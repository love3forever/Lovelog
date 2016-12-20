#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 21:53:24
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from . import login
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from loginForm import LoginForm, RegisterForm
import sys
sys.path.extend('..')
from userModel import User


@login.route('/login', methods=['GET', 'POST'])
def userLogin():
    if current_user.is_authenticated:
        next = request.args.get('next')
        if next:
            return redirect(next)
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.objects(username=form.username.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user, form.rememberme.data)
                return redirect(url_for('index.indexPage'))
                # return render_template('index.html', current_user=user)
            flash('Invalid username or password.')
        return render_template('login/login.html', form=form)


if __name__ == '__main__':
    print(User)
