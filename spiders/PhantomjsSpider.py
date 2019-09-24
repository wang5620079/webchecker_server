#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 21:50
# @Author  : GXl
# @File    : PhantomjsSpider.py
# @Software: win10 Tensorflow1.13.1 python3.7

import os
import time
from selenium import webdriver
from utils import logutils
import hashlib

logger = logutils.getlogger(__file__)

class PhantomjsSpider():
    PHANTOMJSPATH=os.path.join(os.getcwd(),'..','phantomjs','bin', 'phantomjs.exe')
    browser=None
    page_load_timeout=20
    script_timeout=20

    def init_app(self,app=None):
        config = getattr(app, 'config', {})
        self.PHANTOMJSPATH = config['PHANTOMJSPATH']
        logger.debug('PHANTOMJSPATH={}'.format(self.PHANTOMJSPATH))



    #全局变量，浏览器
    def __init__(self):
        logger.debug('path={}'.format(self.PHANTOMJSPATH))

    def __enter__(self):
        logger.debug('******************创建新浏览器实例********************')
        if not self.browser:
            self.browser = webdriver.PhantomJS(self.PHANTOMJSPATH)
            # 分辨率设置
            self.browser.set_window_size(1920, 1080)
            # 超时时间设置
            self.browser.set_page_load_timeout(self.page_load_timeout)
            self.browser.set_script_timeout(self.script_timeout)
            self.browser.implicitly_wait(self.script_timeout)
            # time.sleep(2)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info("****************************** exit ************************************")
        try:
            self.browser.quit()
        except Exception as e:
            raise e
        return  True
    def gethtml(self,url=None):
        logger.info("****************************** gethtml ************************************")
        logger.info("url={}".format(url))
        if not url:
            raise Exception('传入的url为空！')
        logger.info('打开页面 {}'.format(url))
        # 设置浏览器需要打开的url
        try:
            oldmiltime=int(round(time.time() * 1000000))
            self.browser.get(url)
            crtmiltime = int(round(time.time() * 1000000))
            timespent=crtmiltime-oldmiltime
            content = self.browser.page_source
        except Exception as e:
            logger.exception(e)
            self.browser.execute_script('window.stop()')
            content =None
            return content
        # finally:
        #     #关闭页面
        #     self.browser.close()
        pagelen=len(content)
        #MD5
        md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
        return content,pagelen,timespent,md5
    #退出浏览器
    def quit(self):
        if self.browser:
            self.browser.quit()

if __name__=='__main__':
    # spider = PhantomjsSpider()
    # content,pagelen,timespent,md5=spider.gethtml('http://www.baidu.com/')
    # # spider.quit()
    # print(pagelen,' ', timespent,' ',md5)
    # print('*************************************')
    # content, pagelen, timespent, md5 = spider.gethtml('http://www.baidu.com/')
    # spider.quit()
    # print(pagelen, ' ', timespent, ' ', md5)
    with PhantomjsSpider() as spider:
        content,pagelen,timespent,md5=spider.gethtml('http://www.baidu.com/')
        print(pagelen, ' ', timespent, ' ', md5)
        print('*************************************')
    with PhantomjsSpider() as spider:
        content,pagelen,timespent,md5=spider.gethtml('http://www.baidu.com/')
        print(pagelen, ' ', timespent, ' ', md5)
        print('*************************************')