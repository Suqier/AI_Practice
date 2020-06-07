# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第七十一题：考虑一个维度为 (5, 5, 3) 的数组，如何将其乘以维度为 (5, 5) 的数组？

import numpy as np

A = np.ones((5, 5, 3))
B = 2*np.ones((5, 5))

print(B)

print("---------")
print(B[:, :, None])

print("---------")
print(A * B[:, :, None])

# 输出内容：
# [[2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]
#  [2. 2. 2. 2. 2.]]
# ---------
# [[[2.]
#   [2.]
#   [2.]
#   [2.]
#   [2.]]
#
#  [[2.]
#   [2.]
#   [2.]
#   [2.]
#   [2.]]
#
#  [[2.]
#   [2.]
#   [2.]
#   [2.]
#   [2.]]
#
#  [[2.]
#   [2.]
#   [2.]
#   [2.]
#   [2.]]
#
#  [[2.]
#   [2.]
#   [2.]
#   [2.]
#   [2.]]]
# ---------
# [[[2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]]
#
#  [[2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]]
#
#  [[2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]]
#
#  [[2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]]
#
#  [[2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]
#   [2. 2. 2.]]]