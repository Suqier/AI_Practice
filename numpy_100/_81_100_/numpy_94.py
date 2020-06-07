# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十四题：考虑到 10 x 3 矩阵，请提取值不相等的行
# Author: Robert Kern

import numpy as np

Z = np.random.randint(0,5,(10,3))
print(Z)
print("---------")
E = np.all(Z[:,1:] == Z[:,:-1], axis=1)
U = Z[~E]
print(U)
print("---------")
U = Z[Z.max(axis=1) != Z.min(axis=1),:]
print(U)

# 输出内容：
# [[3 3 2]
#  [3 2 1]
#  [4 1 3]
#  [1 3 4]
#  [3 4 1]
#  [1 0 2]
#  [0 1 1]
#  [2 0 1]
#  [1 1 4]
#  [1 2 4]]
# ---------
# [[3 3 2]
#  [3 2 1]
#  [4 1 3]
#  [1 3 4]
#  [3 4 1]
#  [1 0 2]
#  [0 1 1]
#  [2 0 1]
#  [1 1 4]
#  [1 2 4]]
# ---------
# [[3 3 2]
#  [3 2 1]
#  [4 1 3]
#  [1 3 4]
#  [3 4 1]
#  [1 0 2]
#  [0 1 1]
#  [2 0 1]
#  [1 1 4]
#  [1 2 4]]
