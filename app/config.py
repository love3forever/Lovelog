#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 14:19:31
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import os

class appConfig(object):
    """this is a default config for app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'can not guess'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MYGIT_MAIL_SUBJECT_PREFIX = '[mygit]'
    MYGIT_MAIL_SENDER = 'mygit Admin <eclipse_sv@163.com>'
    MYGIT_ADMIN = os.environ.get('MYGIT_ADMIN')
    MYGIT_POSTS_PER_PAGE = 20
    MYGIT_FOLLOWERS_PER_PAGE = 50
    MYGIT_COMMENTS_PER_PAGE = 30
    MYGIT_SLOW_DB_QUERY_TIME = 0.5


class developConfig(appConfig):
    """a config for develop env"""
    pass


class productConfig(appConfig):
    """a config for product env"""
    pass


config = {
    'default': developConfig,
    'product': productConfig
}
