#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 12:16
# @Author  : GXl
# @File    : __init__.py.py
# @Software: win10 Tensorflow1.13.1 python3.7

#公共模块

from .jobqueue import QueueMaker
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy

queuemaker = QueueMaker()
apscheduler = APScheduler()
db = SQLAlchemy()