#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : views.py
# @Software: win10 Tensorflow1.13.1 python3.7


from flask import render_template,current_app,send_file
from . import main

from utils import logutils

logger = logutils.getlogger(__file__)

@main.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("****** 进入主目录 *****")
    return "OK"
    # return send_file('index.html')

@main.route('/setinfo/<info>', methods=['GET', 'POST'])
def setinfo(info):
    # from webchecker import app
    app=current_app._get_current_object()
    setattr(app,'urllist',['www.baidu.com','www.sina.com'])
    return 'ok'

@main.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    app = current_app._get_current_object()
    urllist=getattr(app, 'urllist')
    logger.debug(urllist)
    return 'ok'
