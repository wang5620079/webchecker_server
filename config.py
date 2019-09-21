#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : config.py
# @Software: win10 Tensorflow1.13.1 python3.7


import os
import sys
import yaml
import winreg

#当前目录
currentdir = os.path.abspath(os.path.join(os.getcwd()))

#基础目录
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in  ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 20

    # 配置文件目录
    CONFIGFILE = os.path.abspath(os.path.join(currentdir, 'config', 'config.yaml'))
    # 数据库数据文件所在路径
    DBFILEDIR = os.path.abspath(os.path.join(currentdir, 'data'))
    # 数据库数据文件路径
    DBFILE = os.path.abspath(os.path.join(DBFILEDIR, 'data','data.sqlite'))
    # 日志文件所在路径
    LOGDIR = os.path.abspath(os.path.join(currentdir, 'logs'))
    # phantomjs的目录
    PHANTOMJSPATH=os.path.abspath(os.path.join(currentdir,'phantomjs','bin', 'phantomjs.exe'))
    #桌面路径
    REGKEY = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders')
    DESCTOPPATH = winreg.QueryValueEx(REGKEY, "Desktop")[0]

    #其他各项初始化参数
    FILELOGLEVEL = 'INFO'
    GLOABLELOGLEVEL = 'DEBUG'
    CONSOLELOGLEVEL = 'DEBUG'
    PAGE_LOAD_TIMEOUT = 10
    SCRIPT_TIMEOUT = 5
    RERUNDTIME = 60
    DEFAULTCHECKERMODE = 'NORMAL'
    BROWSERPATH = dict()

    @staticmethod
    def init_app(app):
        print('**系统初始化**')

        #检查配置文件路径是否存在
        try:
            with  open(Config.CONFIGFILE, 'r', encoding="utf-8") as file:
                userconfig = yaml.load(file, Loader=yaml.FullLoader)
                # 浏览器配置
                if 'browserpath' in userconfig:
                    for key,val in userconfig['browserpath'].items():
                        if not os.path.exists(val):
                            raise Exception("{} 对应在路径 {} 未找到！".format(key,val))
                    Config.BROWSERPATH = userconfig['browserpath']

                if 'logging' in userconfig:
                    levellst = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FALTAL']
                    loggingconfig = userconfig['logging']
                    if 'gloableloglevel' in loggingconfig:
                        if  loggingconfig['gloableloglevel'] in levellst:
                            Config.GLOABLELOGLEVEL = loggingconfig['gloableloglevel']
                        else:
                            raise Exception('{} 配置必须为 {} 之一'.format('gloableloglevel', levellst))

                    if 'fileloglevel' in loggingconfig:
                        if loggingconfig['fileloglevel'] in levellst:
                            Config.FILELOGLEVEL = loggingconfig['fileloglevel']
                        else:
                            raise Exception('{} 配置必须为 {} 之一'.format('fileloglevel', levellst))

                    if 'consoleloglevel' in loggingconfig:
                        if loggingconfig['consoleloglevel'] in levellst:
                            Config.CONSOLELOGLEVEL = loggingconfig['consoleloglevel']
                        else:
                            raise Exception('{} 配置必须为 {} 之一'.format('consoleloglevel', levellst))

                if 'checkersetting' in userconfig:
                    browsersetting = userconfig['checkersetting']
                    if 'defaultcheckermode' in browsersetting :
                        if browsersetting['defaultcheckermode'] in ['NORMAL', 'QUICK']:
                            Config.DEFAULTCHECKERMODE = browsersetting['defaultcheckermode']
                        else:
                            raise Exception('{} 配置必须为 {} 之一'.format('defaultcheckermode', ['NORMAL', 'QUICK']))
                    if 'rerundtime' in browsersetting:
                        if isinstance(browsersetting['rerundtime'],int):
                            Config.RERUNDTIME = browsersetting['rerundtime']
                        else:
                            raise Exception('{} 配置必须为数值'.format('rerundtime'))
                    if 'page_load_timeout' in browsersetting:
                        if isinstance(browsersetting['page_load_timeout'],int):
                            Config.PAGE_LOAD_TIMEOUT = browsersetting['page_load_timeout']
                        else:
                            raise Exception('{} 配置必须为数值'.format('page_load_timeout'))
                    if 'script_timeout' in browsersetting:
                        if isinstance(browsersetting['script_timeout'],int):
                            Config.SCRIPT_TIMEOUT = browsersetting['script_timeout']
                        else:
                            raise Exception('{} 配置必须为数值'.format('script_timeout'))
        except FileNotFoundError as e:
            print("配置文件未找到，使用系统默认配置！")
        except Exception as e:
            print("错误:{},{}".format(e, " 初始化失败，退出!"))
            sys.exit(1)

        #如果数据库路径不存在，则创建
        if not os.path.exists(Config.DBFILEDIR):
            print("第一次运行，创建数据库目录{}".format(Config.DBFILEDIR))
            os.makedirs(Config.DBFILEDIR)
        print('**系统初始化完成**')
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + Config.DBFILE


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///'+Config.DBFILE


class ProductionConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + Config.DBFILE


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
