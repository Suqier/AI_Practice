# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十八题：如何使用 numpy 数组实现 "the Game of Life"
# Author: Nicolas Rougier

import numpy as np


def iterate(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2] + Z[1:-1,2:] + Z[2:  ,0:-2] +
         Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N == 2) | (N == 3)) & (Z[1:-1, 1:-1] == 1)
    Z[...] = 0
    Z[1:-1, 1:-1][birth | survive] = 1
    return Z


Z = np.random.randint(0, 2, (50, 50))
for i in range(100):
    Z = iterate(Z)
print(Z)

# 输出内容：
# [[0 0 0 ... 0 0 0]
#  [0 0 0 ... 0 0 0]
#  [0 0 1 ... 0 0 0]
#  ...
#  [0 0 0 ... 0 0 0]
#  [0 0 0 ... 0 0 0]
#  [0 0 0 ... 0 0 0]]
