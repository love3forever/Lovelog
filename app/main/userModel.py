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


@lg.user_loader
def load_user(uid):
    return User.query(bson.objectid.ObjectId(str(uid)))


class User(UserMixin, db.Document):
    username = db.StringField(required=True, max_length=15)
    email = db.EmailField(required=True, max_length=40)
    password = db.StringField(required=True, max_length=15)
    sex = db.StringField(required=True, max_length=10)
    age = db.IntField(required=True, max_length=3)
    school = db.StringField(max_length=30)
    location = db.StringField(max_length=30)
    createdTime = db.DateTimeField(required=True)
    isactive = db.BooleanField(required=True)
    isauthenticated = db.BooleanField(required=True)

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

    @staticmethod
    def query(uid):
        result = User.objects(id=uid)
        if len(result) != 0:
            value = result[0]
            return value
        else:
            return None

    def verify_password(self, pswd):
        return check_password_hash(self.password, pswd)

if __name__ == '__main__':
    testUser = User()
    testUser.username = 'wangmeng'
    testUser.email = 'eclipse_sv@163.com'
    testUser.password = 'abc@123'
    testUser.sex = 'male'
    testUser.school = 'whu'

    testUser.save()
