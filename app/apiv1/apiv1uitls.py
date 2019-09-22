#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 23:40
# @Author  : GXl
# @File    : apiv1uitls.py
# @Software: win10 Tensorflow1.13.1 python3.7

import json
from utils import logutils
logger=logutils.getlogger(__file__)
def jsonerror(msg):
    tmpdict=dict()
    tmpdict['success']=False
    tmpdict['msg']=msg
    logger.error("msg={}".format(msg))
    return json.dumps(tmpdict, ensure_ascii=False)
def jsonmsg(msg):
    tmpdict=dict()
    tmpdict['success']=True
    tmpdict['msg']=msg
    logger.debug("msg={}".format(msg))
    return json.dumps(tmpdict, ensure_ascii=False)