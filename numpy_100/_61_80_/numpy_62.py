# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六十二题：如何使用 iterator 去计算两个 (1,3) 和 (3,1) 数组的和

import numpy as np

A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
print(A)
print("---------")
print(B)
print("---------")
it = np.nditer([A, B, None])
for x, y, z in it:
    z[...] = x + y
print(it.operands[2])

# 输出内容：
# [[0]
#  [1]
#  [2]]
# ---------
# [[0 1 2]]
# ---------
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]
