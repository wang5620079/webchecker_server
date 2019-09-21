#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 0021 19:11
# @Author  : GXl
# @File    : models.py
# @Software: win10 Tensorflow1.13.1 python3.7

from . import db

class Tab(db.Model):
    __tablename_ = 'tab'
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    score = db.Column(db.INTEGER)

    def __repr__(self):
        return  '\r\n'.join(['{}={}'.format(key,val) for key,val in self.__dict__.items()])


class Configuration(db.Model):
    __tablename_ = 'configuration'
    id = db.Column(db.INTEGER, primary_key=True)

