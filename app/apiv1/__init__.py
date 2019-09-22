#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : __init__.py
# @Software: win10 Tensorflow1.13.1 python3.7

from flask import Blueprint
from app import db
apiv1 = Blueprint('apiv1', __name__)

from . import jobs, errors,config,views

