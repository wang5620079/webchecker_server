#coding:utf-8
# -*- coding: utf-8 -*-

import datetime,time
from pytz import timezone

#日志模块
from utils import logutils
logger=logutils.getlogger(__file__)
cst_tz = timezone('Asia/Shanghai')

#时间戳转时间字符串
def timestamp2strftime(timeStamp):
    cst_tz = timezone('Asia/Shanghai')
    # dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    dateArray = datetime.datetime.fromtimestamp(timeStamp).replace(tzinfo=cst_tz)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    logger.debug(otherStyleTime)
    return otherStyleTime
#当前时间转换为1970秒数
def now2seconds():
    # timeDateStr = "2014-07-29 00:00:00"
    # time1 = datetime.datetime.strptime(timeDateStr, "%Y-%m-%d %H:%M:%S")
    now=datetime.datetime.now()
    secondsFrom1970 = time.mktime(now.timetuple())
    return secondsFrom1970

def ses2datetime(sec):
    timeArray = time.localtime(sec)  # 1970秒数
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    dt = datetime.datetime.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    return dt

def get_nowtime_str(fmt=None):
    nowtime = datetime.datetime.now()
    if fmt:
        return nowtime.strftime(fmt)
    return nowtime.strftime('%Y-%m-%d %H:%M:%S')

if __name__=='__main__':
    print(get_nowtime_str(fmt='%Y%m%d%H%M%S'))
    print(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
