#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 21:53:24
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import bson
from datetime import date
from . import login
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from loginForm import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash
import sys
sys.path.extend('..')
from userModel import User, Pair


@login.route('/login', methods=['GET', 'POST'])
def userLogin():
    if current_user.is_authenticated:
        next = request.args.get('next')
        if next:
            return redirect(next)
    else:
        if current_user.is_active:
            return current_user.userid
        else:
            form = LoginForm()
            if form.validate_on_submit():
                user = User.objects(username=form.username.data).first()
                if user is not None and user.verify_password(form.password.data):
                    login_user(user, form.rememberme.data)
                    return redirect(url_for('index.indexPage'))
                flash('Invalid username or password.')
            return render_template('login/login.html', form=form)


@login.route('/logout', methods=['GET'])
def userLogout():
    if current_user:
        logout_user()
        return redirect(url_for('index.indexPage'))


@login.route('/registe', methods=['GET', 'POST'])
def userRegist():
    if current_user.is_authenticated:
        flash('Please logout before registe a new account')
        next = request.args.get('next')
        if next:
            return redirect(next)
        return redirect(url_for('index.indexPage'))
    else:
        form = RegisterForm()
        if form.validate_on_submit():
            user = User()
            user.username = form.username.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)
            user.sex = form.sex.data
            user.age = form.age.data
            user.school = form.school.data
            user.location = form.location.data
            user.createdTime = date.today()
            user.isactive = True
            user.isauthenticated = False

            print(user.username)
            user.save()

            login_user(user)
            return redirect(url_for('index.indexPage'))
        return render_template('login/registe.html', form=form)


@login.route('/registe/<string:code>', methods=['GET', 'POST'])
def userRegistWithCode(code):
    '''
    用户注册，有无邀请码来区分不同的组册情况
    '''
    if current_user.is_authenticated:
        flash('Please logout before registe a new account')
        next = request.args.get('next')
        if next:
            return redirect(next)
        return redirect(url_for('index.indexPage'))
    else:
        form = RegisterForm()
        if code:
            form.inviteCode.data = code
        if form.validate_on_submit():
            user = User()
            user.username = form.username.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)
            user.sex = form.sex.data
            user.age = form.age.data
            user.school = form.school.data
            user.location = form.location.data
            user.createdTime = date.today()
            user.isactive = True
            user.isauthenticated = False
            uniqueCode = form.inviteCode.data
            if uniqueCode:
                if Pair.query(bson.objectid.ObjectId(str(code))):
                    flash('This invite code has been used')
                    return redirect(url_for('login.userRegist'))
                user.save()
                login_user(user)
                if user.sex == 'male':
                    try:
                        pair = Pair()
                        pair.boy = user
                        pair.girl = User.query(
                            bson.objectid.ObjectId(str(code)))
                        pair.save()
                    except Exception as e:
                        print(str(e))
                else:
                    try:
                        pair = Pair()
                        pair.girl = user
                        pair.boy = User.query(
                            bson.objectid.ObjectId(str(code)))
                        pair.save()
                    except Exception as e:
                        print(str(e))
                return redirect(url_for('index.indexPage'))
            print(user.username)
            user.save()
            login_user(user)
            return redirect(url_for('index.indexPage'))
        return render_template('login/registe.html', form=form)


if __name__ == '__main__':
    print(User)
