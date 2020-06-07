# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六十九题：如何获得对角矩阵的点积
# Author: Mathieu Blondel

import numpy as np

A = np.random.uniform(0, 1, (5, 5))
B = np.random.uniform(0, 1, (5, 5))

# Slow version
print(np.diag(np.dot(A, B)))

# Fast version
print("---------")
print(np.sum(A * B.T, axis=1))

# Faster version
print("---------")
print(np.einsum("ij,ji->i", A, B))

# 输出内容：
# [0.75819288 2.14501998 0.91229192 1.37113823 1.28174324]
# ---------
# [0.75819288 2.14501998 0.91229192 1.37113823 1.28174324]
# ---------
# [0.75819288 2.14501998 0.91229192 1.37113823 1.28174324]
