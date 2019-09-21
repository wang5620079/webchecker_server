#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : views.py
# @Software: win10 Tensorflow1.13.1 python3.7


from flask import render_template
from . import main

from utils import logutils

logger = logutils.getlogger(__file__)

@main.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("****** 进入主目录 *****")
    user="webchecker"
    return render_template('index.html',user=user)

