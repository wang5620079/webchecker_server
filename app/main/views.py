#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : views.py
# @Software: win10 Tensorflow1.13.1 python3.7


from flask import render_template,current_app
from . import main
from app import scheduler

from utils import logutils

logger = logutils.getlogger(__file__)

@main.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("****** 进入主目录 *****")
    user="webchecker"
    return render_template('index.html',user=user)

@main.route('/setinfo/<info>', methods=['GET', 'POST'])
def setinfo(info):
    from webchecker import app
    with app.app_context():
        current_app.__setattr__('urllist',['www.baidu.com','www.sina.com'])
    return 'ok'

@main.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    from webchecker import app
    with app.app_context():
        print(current_app.__getattr__('info'))
    return 'aaaaa'
