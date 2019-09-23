#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : models.py
# @Software: win10 Tensorflow1.13.1 python3.7

from common import db


class Url(db.Model):
    __tablename_ = 'urls'
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    url = db.Column(db.TEXT)
    mode = db.Column(db.String(10))
    method = db.Column(db.String(10))
    timeout = db.Column(db.INTEGER)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'url': self.url,
            'mode': self.mode,
            'method':self.method,
            'timeout': self.timeout,
        }

    def __repr__(self):
        return  '\r\n'.join(['{}={}'.format(key,val) for key,val in self.__dict__.items()])
