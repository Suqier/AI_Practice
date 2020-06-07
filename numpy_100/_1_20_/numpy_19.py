# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第十九题：创建一个 8 * 8 的 “棋盘图案” 矩阵

import numpy as np

Z = np.zeros((8, 8), dtype=int)
print(Z)

print("---------")
Z[1::2, ::2] = 1
print(Z)

print("---------")
Z[::2, 1::2] = 1
print(Z)

# 输出内容：
# [[0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0]]
# ---------
# [[0 0 0 0 0 0 0 0]
#  [1 0 1 0 1 0 1 0]
#  [0 0 0 0 0 0 0 0]
#  [1 0 1 0 1 0 1 0]
#  [0 0 0 0 0 0 0 0]
#  [1 0 1 0 1 0 1 0]
#  [0 0 0 0 0 0 0 0]
#  [1 0 1 0 1 0 1 0]]
# --------- 1，0 相互交错
# [[0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]]



