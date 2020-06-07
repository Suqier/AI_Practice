# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十一题：考虑数组Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]，
# 如何生成数组R = [[1,2,3,4]，[2,3,4,5]，[3,4,5,6]，...，[11,12,13,14]] ?
# Author: Stefan van der Walt

from numpy.lib import stride_tricks
import numpy as np

Z = np.arange(1, 15, dtype=np.uint32)
R = stride_tricks.as_strided(Z, (11, 4), (4, 4))
print(R)

# 输出内容：
# [[ 1  2  3  4]
#  [ 2  3  4  5]
#  [ 3  4  5  6]
#  [ 4  5  6  7]
#  [ 5  6  7  8]
#  [ 6  7  8  9]
#  [ 7  8  9 10]
#  [ 8  9 10 11]
#  [ 9 10 11 12]
#  [10 11 12 13]
#  [11 12 13 14]]
