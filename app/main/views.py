#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : views.py
# @Software: win10 Tensorflow1.13.1 python3.7


from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    user="webchecker"
    return render_template('index.html',user=user)

