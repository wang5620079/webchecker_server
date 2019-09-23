#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 21:11
# @Author  : GXl
# @File    : errors.py.py
# @Software: win10 Tensorflow1.13.1 python3.7

from. . import apiv1
from .apiv1uitls import jsonerror

@apiv1.app_errorhandler(403)
def forbidden(e):
    return jsonerror('禁止访问',status=403), 403


@apiv1.app_errorhandler(404)
def page_not_found(e):
    return jsonerror('请求的页面未找到',status=404), 404


@apiv1.app_errorhandler(500)
def internal_server_error(e):
    return jsonerror('内部错误',status=500), 500
