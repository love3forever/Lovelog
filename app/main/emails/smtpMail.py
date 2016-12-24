#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-24 19:36:17
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

import smtplib
from threading import Thread

from email.mime.text import MIMEText
from email.header import Header

HOST = 'smtp.163.com'
PORT = 465

MAIL_USER = 'xx@163.com'
MAIL_PASSWD = 'xxx'


def asyncMail(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@asyncMail
def sendMail(uid, mailAddr):
    try:
        link = 'https://localhost:5000/email/active/' + uid
        title = 'Active Your Account by Click this link'
        context = '<p>{}</p><br><p><a href="{}">{}</a></p>'.format(
            title, link, link)
        msg = MIMEText(context, 'html', 'utf-8')
        msg['From'] = '<{}>'.format(MAIL_USER)
        msg['Subject'] = Header('Active your account', 'utf8').encode()
        msg['To'] = '<{}>'.format(mailAddr)
        smtpObj = smtplib.SMTP_SSL(HOST)
        smtpObj.connect(HOST, PORT)
        smtpObj.login(MAIL_USER, MAIL_PASSWD)
        smtpObj.sendmail(MAIL_USER, mailAddr, msg.as_string())
        print('Mail sent successfully')
    except smtplib.SMTPException as e:
        print(str(e))
        print('Something wrong with Mail Module')


if __name__ == '__main__':
    sendMail('123456', 'xxx@qq.com')
