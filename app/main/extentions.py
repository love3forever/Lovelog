#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 22:42:57
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os
from flask import Flask
from config import config


db = MongoEngine()
lg = LoginManager()
bootstrap = Bootstrap()


def createApp(name='default'):
    app = Flask(__name__)
    app.config.from_object(config[name])
    lg.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    from index import index as indexBlueprint
    app.register_blueprint(indexBlueprint)

    from login import login as loginBlueprint
    app.register_blueprint(loginBlueprint)

    return app


if __name__ == '__main__':
    running = createApp()
    currentPath = os.path.abspath('.')
    sslContext = (currentPath + '/cert/ssl.crt',
                  currentPath + '/cert/ssl.key')
    running.run(debug=True, host='0.0.0.0',
                ssl_context=sslContext, threaded=True)
