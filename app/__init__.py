#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : __init__.py
# @Software: win10 Tensorflow1.13.1 python3.7


from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from schedulerworker import apscheduler

import testworker

from config import config

from utils import logutils

# bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
# scheduler = APScheduler()


# def work():
#    urls=db.session.query(Url).all()
#    print(urls)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # db.app=app
    logutils.init_app(app)
    #定时任务
    #####################################################上面代码忽略
    # 这里是重点
    apscheduler.api_enabled = True
    apscheduler.init_app(app)
    apscheduler.add_job(id='testjob', func=testworker.work, trigger='interval', seconds=2)
    apscheduler.start()
    ######################################################下面代码忽略



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .apiv1 import apiv1  as apiv_blueprint
    app.register_blueprint(apiv_blueprint,url_prefix='/api/v1')


    return app
