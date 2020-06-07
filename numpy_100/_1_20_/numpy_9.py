# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九题：创建一个 3 * 3 的矩阵，矩阵的数据从 0 ~ 8

import numpy as np

Z = np.arange(9)
print(Z)

print("---------")
Z = Z.reshape(3, 3)
print(Z)

print("---------")
Z = np.arange(9).reshape(3, 3)
print(Z)

# 输出内容：
# [0 1 2 3 4 5 6 7 8]
# ---------
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# ---------
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
