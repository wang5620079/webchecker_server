#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 9:37
# @Author  : GXl
# @File    : testworker.py
# @Software: win10 Tensorflow1.13.1 python3.7

from flask import current_app
import datetime


def work():
    from webchecker import app
    with app.app_context():
        if hasattr(current_app,'urllist'):
            urllist = current_app.__getattr__('urllist')
            print(urllist)
        else:
            print('no urllist')
