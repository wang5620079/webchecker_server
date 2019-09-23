#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 21:15
# @Author  : GXl
# @File    : Test.py
# @Software: win10 Tensorflow1.13.1 python3.7
import os
[dirname,filename]=os.path.split('sw724.vaps')
print(dirname,"\n",filename)

[fname,fename]=os.path.splitext('sw724.vaps')
print(fname.strip())
print(fename.strip())