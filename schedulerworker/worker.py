#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 11:32
# @Author  : GXl
# @File    : common.py
# @Software: win10 Tensorflow1.13.1 python3.7

from utils import logutils
from schedulerworker import apscheduler


logger=logutils.getlogger(__file__)
def work():
    logger.debug("work 开始")
    with apscheduler.app.app_context():
        # from app import db
        from app.models import Url
        # urls=scheduler.app.db.session.query(scheduler.app.models.Url).all()
        urls=Url.query.all()
        print(urls)