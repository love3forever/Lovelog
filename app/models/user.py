#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 16:37:27
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from . import db, lg
from flask.ext.login import UserMixin


@lm.user_loader
def load_user(uid):
    return User.query(bson.objectid.ObjectId(str(uid)))


class User(UserMixin, db.Document):
    username = db.StringField(required=True, max_length=15)
    email = db.StringField(required=True, max_length=40)
    password = db.StringField(required=True, max_length=15)
    sex = db.StringField(required=True, max_length=10)
    school = db.StringField(max_length=30)
    location = db.StringField(max_length=30)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

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
        if self.password == pswd:
            return True
        return False

if __name__ == '__main__':
    testUser = User()
    testUser.username = 'wangmeng'
    testUser.email = 'eclipse_sv@163.com'
    testUser.password = 'abc@123'
    testUser.sex = 'male'
    testUser.school = 'whu'

    testUser.save()
