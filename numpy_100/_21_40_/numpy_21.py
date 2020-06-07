# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十一题：使用 numpy 中提供的函数生成一个 8 * 8 的 “棋盘图案” 矩阵

import numpy as np

X = np.array([[0, 1], [1, 0]])
print(X)

print("---------")
Z = np.tile(X, (4, 4))   # tile: 铺砖瓦，以 X 为砖瓦铺开成一个 4 * 4 的形状
print(Z)

# 输出内容：
# [[0 1]
#  [1 0]]
# ---------
# [[0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]]


