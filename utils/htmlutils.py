#coding:utf-8
# -*- coding: utf-8 -*-

import urllib
#日志模块
from utils import logutils
logger=logutils.getlogger(__file__)

def newgetHtml(url,postDataList=None,pdata=None,headers=None):

    logger.info("******************************开始获取网页************************************")
    # logger.info("******************************开始获取网页************************************")
    if headers==None or len(headers)==0 :
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host':  '',
            'Pragma': 'no-cache',
            'Referer': '',
            'Upgrade-Insecure-Requests': '0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
    else:
        headers=headers

    if postDataList!=None and 'Content-Length' in headers.keys():
        pdata = urllib.parse.urlencode(postDataList, encoding='UTF-8', safe='+').encode('Utf-8')
        headers['Content-Length'] = str(len(pdata))


    if postDataList==None and pdata!=None and 'Content-Length' in headers.keys():
        headers['Content-Length'] = str(len(pdata))

    try:
        res=None
        if pdata==None:
            res = httpsession.get(url, headers=headers)
        else:
            res = httpsession.post(url, headers=headers,data=pdata)
    except Exception as e:
        logger.info('Error code:', str(e))
        logger.error('Error code:', str(e))
    # res.encoding = res.apparent_encoding
    page = res.text

    return page


def newpostHtml(url,postDataList=None,pdata=None,headers=None):

    logger.info("******************************开始获取网页************************************")
    # logger.info("******************************开始获取网页************************************")
    if headers==None or len(headers)==0 :
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Content-Length': '0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': systemconfig.hostparamdic[systemconfig.host]['host'],
            'Upgrade-Insecure-Requests': '0',
            'Referer': systemconfig.hostparamdic[systemconfig.host]['baseurl'] + '/secure/Dashboard.jspa',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        }
    else:
        headers=headers

    if postDataList!=None and 'Content-Length' in headers.keys():
        pdata = urllib.parse.urlencode(postDataList, encoding='UTF-8', safe='+').encode('Utf-8')
        headers['Content-Length'] = str(len(pdata))


    if postDataList==None and pdata!=None and 'Content-Length' in headers.keys():
        headers['Content-Length'] = str(len(pdata))

    try:
        res=None
        if pdata==None:
            res = httpsession.get(url, headers=headers)
        else:
            res = httpsession.post(url, headers=headers,data=pdata)
    except Exception as e:
        logger.info('Error code:', str(e))
        logger.error('Error code:', str(e))
    page = res.text

    return page