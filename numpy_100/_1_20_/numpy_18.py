# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第十八题：用值 1，2，3，4 创建一个 5 * 5 的矩阵，使得这些数字在对角线的下方一行

import numpy as np

Z = np.diag(1+np.arange(4), k=-1)   # 这里的 k 可以理解为偏移量
print(Z)

# 输出内容：
# [[0 0 0 0 0]
#  [1 0 0 0 0]
#  [0 2 0 0 0]
#  [0 0 3 0 0]
#  [0 0 0 4 0]]

Z = np.diag(1+np.arange(4), k=0)
print(Z)

# 输出内容：
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

Z = np.diag(1+np.arange(4), k=1)
print(Z)

# 输出内容：
# [[0 1 0 0 0]
#  [0 0 2 0 0]
#  [0 0 0 3 0]
#  [0 0 0 0 4]
#  [0 0 0 0 0]]
