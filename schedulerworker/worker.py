#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 11:32
# @Author  : GXl
# @File    : common.py
# @Software: win10 Tensorflow1.13.1 python3.7

from utils import logutils
from common import apscheduler,queuemaker
from app.models import Url

logger=logutils.getlogger(__file__)
#######################正式开始############################
#守护任务，该任务用于检测各个任务队列的长度，如果长度为0，则压入任务需要检测的url
def put_urls():
    rs_q = queuemaker.rs_q
    pjs_q = queuemaker.pjs_q
    if rs_q.empty():
        logger.debug('rs队列空，压入数据')
        rsurls = Url.query.filter(Url.mode=='QUICK').all()
        if rsurls and len(rsurls)>0:
            for item in rsurls:
                rs_q.put(item)
    if pjs_q.empty():
        logger.debug('pjs队列空，压入数据')
        prsurls = Url.query.filter(Url.mode=='NORMAL').all()
        if prsurls and len(prsurls)>0:
            for item in prsurls:
                pjs_q.put(item)



#######################以下是测试##########################
def work():
    logger.debug("work 开始")
    with apscheduler.app.app_context():
        urls=Url.query.filter(Url.mode=='NORMAL').all()
        print(urls)

def work1(*args):
    logger.debug("work 开始")
    print((args))

def testgworker(**kwargs):
    rs_q=queuemaker.rs_q
    pjs_q=queuemaker.pjs_q
    result_q = queuemaker.result_q

    try:
        item = rs_q.get(block=False)
        logger.debug('rs_q item={}'.format(item))
    except Exception  as e:
        pass
        # logger.error(e)

    try:
        item = pjs_q.get(block=False)
        logger.debug('pjs_q item={}'.format(item))
    except Exception  as e:
        pass
        # logger.error(e)

    try:
        item = result_q.get(block=False)
        logger.debug('result_q item={}'.format(item))
    except Exception  as e:
        pass
        # logger.error(e)


