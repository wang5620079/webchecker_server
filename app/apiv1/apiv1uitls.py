#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 23:40
# @Author  : GXl
# @File    : apiv1uitls.py
# @Software: win10 Tensorflow1.13.1 python3.7

import json
from utils import logutils
logger=logutils.getlogger(__file__)
def jsonerror(responseText ='error' ,status=None,statusText='error'):
    tmpdict=dict()
    tmpdict['success']=False
    tmpdict['responseText ']=responseText
    tmpdict['statusText '] = statusText
    tmpdict['readyState']=4
    if status:
        tmpdict['status'] = status
    else:
        tmpdict['status'] = 500
    logger.error("errorinfo ={}".format(tmpdict ))

    return json.dumps(tmpdict, ensure_ascii=False)
def jsonmsg(responseText):
    tmpdict=dict()
    tmpdict['success']=True
    tmpdict['statusText ']='ok'
    tmpdict['responseText']='ok'
    tmpdict['readyState'] = 4
    tmpdict['status'] = 200
    logger.debug("successinfo ={}".format(tmpdict ))
    return json.dumps(tmpdict, ensure_ascii=False)