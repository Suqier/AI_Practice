# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第七十二题：如何交换数组的两行？
# Author: Eelco Hoogendoorn

import numpy as np

A = np.arange(25).reshape(5,5)
print(A)

print("---------")
A[[0,1]] = A[[1,0]]
print(A)

# 输出内容：
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
# ---------
# [[ 5  6  7  8  9]
#  [ 0  1  2  3  4]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
