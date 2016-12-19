#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 14:18:04
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import os
from flask import Flask
from config import config


def createApp(name='default'):
    app = Flask(__name__)
    app.config.from_object(config[name])

    return app


if __name__ == '__main__':
    running = createApp()
    currentPath = os.path.abspath('.')
    sslContext = (currentPath + '/cert/ssl.cert',
                  currentPath + '/cert/ssl.key')
    running.run(debug=True, host='0.0.0.0',
                ssl_context=sslContext, threaded=True)
