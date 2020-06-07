# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五十题：如何在向量中找到最接近（给定标量）的值

import numpy as np

Z = np.arange(100)
print(Z)

v = np.random.uniform(0, 100)
print(v)

index = (np.abs(Z - v)).argmin()    # min()：是求矩阵中的最小值； argmin()：是求最小值的索引
print(index)

print(Z[index])

# 输出内容：
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#  24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
#  48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
#  72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
#  96 97 98 99]
# 51.20511118484378
# 51
# 51
