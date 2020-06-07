# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十九题：给定整数 n 和一个二维数组 X，从 X 中找出满足条件的行,指数为 n 的多项式分布

import numpy as np

X = np.asarray([[1.0, 0.0, 3.0, 8.0],
                [2.0, 0.0, 1.0, 1.0],
                [1.5, 2.5, 1.0, 0.0]])

n = 4
print(np.mod(X, 1) == 0)
M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)
M = (X.sum(axis=-1) == n)
print("---------")
print(X[M])

# 输出内容：
# [[ True  True  True  True]
#  [ True  True  True  True]
#  [False False  True  True]]
# ---------
# [[2. 0. 1. 1.]]
