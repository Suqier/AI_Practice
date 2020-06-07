# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第七十六题：考虑一维数组 Z，构建一个二维数组，
#           其第一行是 (Z[0]，Z[1]，Z[2])，随后的每一行都移位 1 (最后一行应为 (Z[-3]，Z[-2]，Z[-1])
# Author: Joe Kington / Erik Rigtorp

from numpy.lib import stride_tricks
import numpy as np


def rolling(a, window):
    shape = (a.size - window + 1, window)   # (8, 3)
    strides = (a.itemsize, a.itemsize)      # (4, 4)
    return stride_tricks.as_strided(a, shape=shape, strides=strides)


Z = rolling(np.arange(10), 3)
print(Z)

# 输出内容：
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]
#  [3 4 5]
#  [4 5 6]
#  [5 6 7]
#  [6 7 8]
#  [7 8 9]]
