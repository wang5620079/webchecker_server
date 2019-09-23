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
from .apiv1uitls import jsonerror,jsonmsg
from utils import excelparser,dtutils

from flask import request,Response,current_app,send_from_directory

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


# 下载url设置模板
@apiv1.route('/getUrlTemplate', methods=['GET', 'POST'])
def get_url_template():
    logger.debug('**进入配置文件下载**')
    app = current_app._get_current_object()
    config = getattr(app, 'config')
    return send_from_directory(config['TEMPLATE_DIR'],filename='url配置模板.xlsx',as_attachment=True)
    # if request.method == 'GET':
    #     app = current_app._get_current_object()
    #     config = getattr(app, 'config')
    #     filepath = os.sep.join([config['TEMPLATE_DIR'], 'url配置模板.xlsx'])
    #     # 流式读取
    #     def send_file():
    #         store_path = filepath
    #         with open(store_path, 'rb') as targetfile:
    #             while 1:
    #                 data = targetfile.read(20 * 1024)  # 每次读取20M
    #                 if not data:
    #                     break
    #                 yield data
    #
    #     response = Response(send_file(), content_type='application/octet-stream')
    #     response.headers["Content-Disposition"] = 'attachment; filename={}'.format('url配置模板').encode('utf-8').decode('latin-1') # 如果不加上这行代码，导致下图的问题
    # else:
    #     return jsonerror('请求方式不允许！')
    # return response

#url数据上传过滤
def allowed_file(filename):
    from webchecker import app
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

#上传url任务清单
@apiv1.route('/upload', methods=['POST'])
def upload_file():
    #返回消息的list
    result_lst = []
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
            [fname, fename] = os.path.splitext(filename)
            fname = fname.strip()
            fename = fename.strip()
            filename=fname+dtutils.get_nowtime_str(fmt='%Y%m%d%H%M%S')+'.'+fename
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
                #如果模式不在规定的模式中，则自动忽略
                if str(item[3]).upper() not in ['QUICK','NORMAL']:
                    result_lst.append('{} 对应的模式 {} 不在标准模式 QUICK 或 NORMAL 中，忽略！'.format(item[0],item[3]))
                    continue
                if not item[4] or str(item[4]).upper() not in ['GET','POST']:
                    result_lst.append('{} 对应的请求方式 {} 不在标准模式 GET 或 GET 中，默认使用Get！'.format(item[0],item[4]))
                    item[4]='GET'
                url = models.Url(name=item[1],url=item[2],mode=str(item[3]).upper(),method=item[4],timeout=item[5])
                urllst.append(url)
            #写库
            db.session.add_all(urllst)
            db.session.commit()
            return  '{"filename":"%s"}' % filename
    else:
        return jsonerror('请求类型不允许！')
    return jsonmsg('\r\n'.join(result_lst))

