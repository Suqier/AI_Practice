# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十五题：原地计算((A+B)*(-A/2))

import numpy as np

A = np.ones(3) * 1
print(A)

print("---------")
B = np.ones(3) * 2
print(B)

print("---------")
C = np.ones(3) * 3
print(C)

print("---------")
np.add(A, B, out=B)
print(B)

print("---------")
np.divide(A, 2, out=A)
print(A)

print("---------")
np.negative(A, out=A)
print(A)

print("---------")
np.multiply(A, B, out=A)
print(A)

# 输出内容：
# [1. 1. 1.]
# ---------
# [2. 2. 2.]
# ---------
# [3. 3. 3.]
# ---------
# [3. 3. 3.]
# ---------
# [0.5 0.5 0.5]
# ---------
# [-0.5 -0.5 -0.5]
# ---------
# [-1.5 -1.5 -1.5]
