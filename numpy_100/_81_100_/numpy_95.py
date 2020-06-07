# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十五题：将整数向量转换为矩阵二进制表示形式
# Author: Warren Weckesser

import numpy as np

I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])
print(I)
print("---------")
B = ((I.reshape(-1, 1) & (2 ** np.arange(8))) != 0).astype(int)
print(B[:, ::-1])

# 另外一种写法
# Author: Daniel T. McDonald
print("---------")
I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
print(np.unpackbits(I[:, np.newaxis], axis=1))

# 输出内容：
# [  0   1   2   3  15  16  32  64 128]
# ---------
# [[0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 1]
#  [0 0 0 0 0 0 1 0]
#  [0 0 0 0 0 0 1 1]
#  [0 0 0 0 1 1 1 1]
#  [0 0 0 1 0 0 0 0]
#  [0 0 1 0 0 0 0 0]
#  [0 1 0 0 0 0 0 0]
#  [1 0 0 0 0 0 0 0]]
# ---------
# [[0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 1]
#  [0 0 0 0 0 0 1 0]
#  [0 0 0 0 0 0 1 1]
#  [0 0 0 0 1 1 1 1]
#  [0 0 0 1 0 0 0 0]
#  [0 0 1 0 0 0 0 0]
#  [0 1 0 0 0 0 0 0]
#  [1 0 0 0 0 0 0 0]]

