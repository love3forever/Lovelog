#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-20 22:42:57
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import bson
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os
from flask import Flask
from config import config

app = Flask(__name__)
db = MongoEngine()
lg = LoginManager()
lg.session_protection = 'strong'
lg.login_view = 'login.userLogin'
bootstrap = Bootstrap()


def createApp(name='default'):

    app.config.from_object(config[name])
    try:
        lg.init_app(app)
        db.init_app(app)
        bootstrap.init_app(app)
    except Exception as e:
        print(str(e))
    

    from userModel import User
    @lg.user_loader
    def load_user(uid):
        return User.query(bson.objectid.ObjectId(str(uid)))

    from index import index as indexBlueprint
    app.register_blueprint(indexBlueprint)

    from login import login as loginBlueprint
    app.register_blueprint(loginBlueprint)

    from emails import userEmail as emailBlueprint
    app.register_blueprint(emailBlueprint, url_prefix='/email')

    from messages import msg as msgBlueprint
    app.register_blueprint(msgBlueprint, url_prefix='/msg')

    from dairy import dairy as dairyBlueprint
    app.register_blueprint(dairyBlueprint, url_prefix='/dairy')

    return app


if __name__ == '__main__':
    running = createApp()
    currentPath = os.path.abspath('.')
    sslContext = (currentPath + '/cert/ssl.crt',
                  currentPath + '/cert/ssl.key')
    running.run(debug=True, host='0.0.0.0',
                ssl_context=None, threaded=True)
