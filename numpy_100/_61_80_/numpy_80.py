# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十题：对于一个任意数组，编写一个函数来提取具有固定形状并以给定元素为中心的子部分（必要时填充一个填充值）
# Author: Nicolas Rougier

import numpy as np

Z = np.random.randint(0, 10, (10, 10))
shape = (5, 5)
fill = 0
position = (1, 1)

R = np.ones(shape, dtype=Z.dtype) * fill
P = np.array(list(position)).astype(int)
Rs = np.array(list(R.shape)).astype(int)
Zs = np.array(list(Z.shape)).astype(int)

R_start = np.zeros((len(shape),)).astype(int)
R_stop = np.array(list(shape)).astype(int)
Z_start = (P - Rs // 2)
Z_stop = (P + Rs // 2) + Rs % 2

R_start = (R_start - np.minimum(Z_start, 0)).tolist()
Z_start = (np.maximum(Z_start, 0)).tolist()
R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop - Zs, 0))).tolist()
Z_stop = (np.minimum(Z_stop, Zs)).tolist()

r = [slice(start, stop) for start, stop in zip(R_start, R_stop)]
z = [slice(start, stop) for start, stop in zip(Z_start, Z_stop)]
R[r] = Z[z]
print(Z)
print(R)

# 输出内容：
# [[4 7 2 3 1 9 6 4 5 9]
#  [9 0 1 5 0 5 1 1 7 6]
#  [6 2 1 4 9 5 6 1 8 7]
#  [7 7 5 1 2 8 8 6 3 0]
#  [2 0 6 1 6 3 9 6 9 9]
#  [1 8 0 3 5 1 4 3 2 2]
#  [9 7 2 6 7 0 1 0 1 0]
#  [0 8 8 4 3 5 2 9 3 6]
#  [4 4 5 3 1 4 9 4 5 7]
#  [6 5 0 8 2 6 4 5 8 7]]
# [[0 0 0 0 0]
#  [0 4 7 2 3]
#  [0 9 0 1 5]
#  [0 6 2 1 4]
#  [0 7 7 5 1]]









