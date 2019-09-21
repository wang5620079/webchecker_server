#/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

import os
import logging
import time
from flask import current_app

levellst = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FALTAL']
logleve=[logging.DEBUG,logging.INFO,logging.WARN,logging.ERROR,logging.FATAL]

GLOABLELOGLEVEL=logging.DEBUG
FILELOGLEVEL = logging.INFO
CONSOLELOGLEVEL = logging.DEBUG
LOGDIR=os.path.abspath(os.path.join(os.getcwd(),'logs'))

def init_app(app):
    global GLOABLELOGLEVEL
    global FILELOGLEVEL
    global CONSOLELOGLEVEL
    global LOGDIR
    config=getattr(app, 'config', {})
    GLOABLELOGLEVEL = logleve[levellst.index(config['GLOABLELOGLEVEL'])]
    FILELOGLEVEL = logleve[levellst.index(config['FILELOGLEVEL'])]
    CONSOLELOGLEVEL = logleve[levellst.index(config['CONSOLELOGLEVEL'])]
    LOGDIR = config['LOGDIR']


def getlogger(file):
    # 日志模块设置--文件日志
    # 第一步，创建一个logger
    logger = logging.getLogger(file)
    logger.setLevel(GLOABLELOGLEVEL)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    log_path = LOGDIR
    # 如果不存在定义的日志目录就创建一个
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    # 获取脚本名称，并以脚本名称作为日志名
    log_name = log_path + os.sep+os.path.basename(os.path.realpath(file)).split('.')[0] +'_'+ rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
    # 文件日志级别
    fh.setLevel(FILELOGLEVEL)

    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)

    # 日志模块--控制台日志
    ch = logging.StreamHandler()
    ch.setLevel(CONSOLELOGLEVEL)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return  logger