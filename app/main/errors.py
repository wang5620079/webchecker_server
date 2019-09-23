#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : errors.py
# @Software: win10 Tensorflow1.13.1 python3.7

from flask import request
from flask import render_template
from . import main
from app.apiv1.apiv1uitls import jsonerror

@main.app_errorhandler(403)
def forbidden(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        jsonerror('禁止访问',status=403)
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        jsonerror('请求的页面未找到',status=404)
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        jsonerror('内部错误',status=500)
    return render_template('500.html'), 500
