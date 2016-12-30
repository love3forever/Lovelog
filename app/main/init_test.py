#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-19 14:47:46
# @Author  : eclipse (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

import unittest
import extentions


class initTest(unittest.TestCase):
    """docstring for initTest"""

    def setUp(self):
        self.app = extentions.createApp().test_client()

    def tearDown(self):
        self.app = None

    def test_index_route(self):
        rv = self.app.get('/')
        assert 'not login yet' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username, password=password, submit='Login'
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('wangmeng', 'abc@123')
        print(rv.data)
        print rv.status_code
        assert rv.status_code is 302
        print(rv.data)
        assert 'Login in as' in rv.data
        rv = self.logout()

        assert 'not login yet' in rv.data
        # rv = self.login('wangsan', 'abc@123')
        # assert 'Login in as' in rv.data
        rv = self.login('wanm', 'dasdasa')
        print(rv.data)
        assert 'Login in as' not in rv.data

if __name__ == '__main__':
    unittest.main()
