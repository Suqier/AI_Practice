# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十八题：给定用两组向量 (X,Y) 描述的一条线，如何进行等距采样
# Author: Bas Swinckels

import numpy as np

phi = np.arange(0, 10*np.pi, 0.1)

a = 1
x = a*phi*np.cos(phi)
y = a*phi*np.sin(phi)

dr = (np.diff(x)**2 + np.diff(y)**2)**.5    # segment lengths
r = np.zeros_like(x)
r[1:] = np.cumsum(dr)                       # integrate path
r_int = np.linspace(0, r.max(), 200)        # regular spaced path
x_int = np.interp(r_int, r, x)              # integrate path
y_int = np.interp(r_int, r, y)
