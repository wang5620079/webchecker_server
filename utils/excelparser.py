#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 0:30
# @Author  : GXl
# @File    : excelparser.py
# @Software: win10 Tensorflow1.13.1 python3.7

#根据传入的文件解析，并返回list数据
import os
import openpyxl
from utils import logutils
logger=logutils.getlogger(__file__)

def parse_excel(filepath):
    if not filepath or not os.path.exists(filepath):
        raise FileNotFoundError('文件未找到！')
    wb = openpyxl.load_workbook(filename=filepath)
    # 获取活动的sheet页
    act_sheet = wb.active
    ##########################
    logger.debug('###########开始读取数据##########')
    # 循环开始按行读取数据,把所有数据存到一个list中,list中的数据是一行数据的list
    datalst = []
    for row in act_sheet.rows:
        tmplst = []
        for cell in row:
            if None != cell.value and len(str(cell.value).strip()) > 0:
                tmplst.append(cell.value)
            else:
                tmplst.append('')
        datalst.append(tmplst)
    logger.debug('###########读取数据完成##########')
    logger.debug("datalst={}".format(datalst))
    return  datalst