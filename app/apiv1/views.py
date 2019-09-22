#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 21:05
# @Author  : GXl
# @File    : views.py
# @Software: win10 Tensorflow1.13.1 python3.7
import os
import datetime
from . import apiv1
from app import db
import app.models as models
from utils import logutils
import json
import werkzeug
from .apiv1uitls import jsonerror
from utils import excelparser

from flask import request

logger = logutils.getlogger(__file__)

@apiv1.route('/', methods=['GET', 'POST'])
def index():
    return "OK"

#获取url数据
@apiv1.route('/geturls', methods=['GET', 'POST'])
def geturls():
    urls=models.Url.query.all()
    logger.debug(urls)
    tmplst=[item.to_dict() for item in urls]
    tmpdict=dict()
    tmpdict['total']=len(urls)
    tmpdict['data']=tmplst
    return json.dumps(tmpdict, ensure_ascii=False)

#url数据上传
def allowed_file(filename):
    from webchecker import app
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@apiv1.route('/upload', methods=['GET', 'POST'])
def upload_file():
    from webchecker import app
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonerror('没有上传文件的字段！')
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonerror('No selected file')
        if file and allowed_file(file.filename):
            filename = werkzeug.secure_filename(file.filename)
            filename=filename.rsplit('.', 1)[0].lower()+ datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.'+filename.rsplit('.', 1)[1].lower()
            filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            ##这里开始解析数据
            datalst=None
            try:
                datalst=excelparser.parse_excel(filepath)
            except Exception as e:
                jsonerror("错误：{}".format(e))
            if not datalst or len(datalst)==0:
                return jsonerror("文件解析错误！")
            #开始写库
            #先清空
            models.Url.query.delete()
            urllst=[]
            for item in datalst[1:]:
                url = models.Url(name=item[1],url=item[2],mode=item[3],timeout=item[4])
                urllst.append(url)
            #写库
            db.session.add_all(urllst)
            db.session.commit()
            return  '{"filename":"%s"}' % filename
        else:
            return jsonerror('文件类型不允许！')
    return ''
