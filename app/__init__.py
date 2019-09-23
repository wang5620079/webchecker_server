#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : __init__.py
# @Software: win10 Tensorflow1.13.1 python3.7


from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
#从公共组件中引入，包含引入队列组件
from  common import db,apscheduler,queuemaker

#自动任务
from schedulerworker import worker

from config import config

from utils import logutils

mail = Mail()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    logutils.init_app(app)
    ########任务队列创建################################
    queuemaker.init_app(app)
    #定时任务
    #####################################################
    # 这里是重点
    # apscheduler.api_enabled = True
    # apscheduler.init_app(app)
    # apscheduler.add_job(id='put_ruls', func=worker.put_urls, trigger='interval', seconds=1)
    # apscheduler.add_job(id='rs_work', func=worker.rs_work, trigger='interval', seconds=1)
    # apscheduler.add_job(id='pjs_work', func=worker.pjs_work, trigger='interval', seconds=1)
    # apscheduler.start()
    ######################################################



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .apiv1 import apiv1  as apiv_blueprint
    app.register_blueprint(apiv_blueprint,url_prefix='/api/v1')


    return app
