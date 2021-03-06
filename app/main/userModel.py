#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 22:34:48
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

import bson
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from extentions import db, lg


# things about user


class User(UserMixin, db.Document):
    username = db.StringField(required=True, max_length=15)
    email = db.StringField(required=True, max_length=40)
    password = db.StringField(required=True, max_length=100)
    sex = db.StringField(required=True, max_length=10)
    age = db.IntField(required=True, min_value=1, max_value=150)
    school = db.StringField(max_length=30)
    location = db.StringField(max_length=30)
    createdTime = db.DateTimeField(required=True)
    isactive = db.BooleanField(required=True)
    isauthenticated = db.BooleanField(required=True)

    def __repr__(self):
        return 'user:{} aged:{}'.format(self.username, self.age)

    @property
    def is_active(self):
        return self.isactive

    @property
    def is_authenticated(self):
        return self.isauthenticated

    @property
    def is_anonymous(self):
        # False as we do not support annonymity
        return False

    @property
    def userid(self):
        return str(self.id)

    @staticmethod
    def query(uid):
        result = User.objects(id=uid)
        if len(result) != 0:
            value = result[0]
            return value
        else:
            return None

    @staticmethod
    def getUserbyID(uid):
        user = User.query(bson.objectid.ObjectId(str(uid)))
        return user

    def verify_password(self, pswd):
        return check_password_hash(self.password, pswd)


class Pair(db.Document):
    """docstring for Pair"""
    boy = db.ReferenceField(User)
    girl = db.ReferenceField(User)

    @property
    def uid(self):
        return str(self.id)

    @staticmethod
    def query(uid):
        user = User.query(uid)
        if user.sex == 'male':
            return Pair.objects(boy=user)
        else:
            return Pair.objects(girl=user)

# things about posts


class Posts(db.Document):
    """docstring for Posts"""
    poster = db.ReferenceField(User)
    createdTime = db.DateTimeField(required=True)
    data = db.FileField(required=True)
    des = db.StringField()
    filename = db.StringField(required=True)
    meta = {'allow_inheritance': True}


class ImagePost(Posts):
    """docstring for ImagePost"""
    pass


class VideoPost(Posts):
    """docstring for VideoPost"""
    pass


# things about message
class SysInfo(db.Document):
    """docstring for SysInfo"""
    desc = db.StringField(required=True)
    awaredof = db.ListField(db.ReferenceField(User))
    date = db.DateTimeField(required=True)
    isread = db.BooleanField(required=True)


if __name__ == '__main__':
    testUser = User()
    testUser.username = 'wangmeng'
    testUser.email = 'eclipse_sv@163.com'
    testUser.password = 'abc@123'
    testUser.sex = 'male'
    testUser.school = 'whu'

    testUser.save()
