#!/usr/bin/python3
#encoding:UTF-8
# -*- coding: utf-8 -*-


import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(Debug=True)



