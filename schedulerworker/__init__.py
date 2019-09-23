#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 11:55
# @Author  : GXl
# @File    : __init__.py.py
# @Software: win10 Tensorflow1.13.1 python3.7

from flask_apscheduler import APScheduler
apscheduler = APScheduler()


# class APSSchedulerConfig(object):
#     JOBS = [
#         {
#             'id': 'teestjob',
#             'func':'webchecker_server.testworker:work',
#             'args':None,
#             'trigger': {
#                 'type': 'interval',
#                 'seconds': '2'
#             }
#         }
#     ]
#     SCHEDULER_API_ENABLED = True
#     SQLALCHEMY_ECHO = True