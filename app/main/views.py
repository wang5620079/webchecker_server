#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : views.py
# @Software: win10 Tensorflow1.13.1 python3.7

import os
from common import queuemaker
from flask import render_template,current_app,request,Response
from . import main

from utils import logutils,dtutils

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


@main.route('/testqueue/rs_q', methods=['GET', 'POST'])
def test_rs_q():
    queuemaker.rs_q.put("{} test re_q".format(dtutils.get_nowtime_str()))
    return 'ok'
@main.route('/testqueue/pjs_q', methods=['GET', 'POST'])
def test_pjs_q():
    queuemaker.pjs_q.put("{} test pjs_q".format(dtutils.get_nowtime_str()))
    return 'ok'

@main.route('/testqueue/result_q', methods=['GET', 'POST'])
def test_result_q():
    queuemaker.result_q.put("{} test result_q".format(dtutils.get_nowtime_str()))
    return 'ok'

@main.route('/testqueue/clear_result_q', methods=['GET', 'POST'])
def clear_result_q():
    logger.debug(queuemaker.result_q.qsize())
    while not queuemaker.result_q.empty():
        queuemaker.result_q.get(block=False)
    logger.debug(queuemaker.result_q.qsize())
    return 'ok'
