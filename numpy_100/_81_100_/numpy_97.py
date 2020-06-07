# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十七题：给定数组 A, B，使用函数 einsum 实现求和，矩阵相乘，内积和外积
# Author: Alex Riley # Make sure to read: http://ajcr.net/Basic-guide-to-einsum/

import numpy as np

A = np.random.uniform(0, 1, 10)
B = np.random.uniform(0, 1, 10)

np.einsum('i->',A)          # np.sum(A)

np.einsum('i,i->i', A, B)   # A * B

np.einsum('i,i', A, B)      # np.inner(A, B)

np.einsum('i,j->ij', A, B)  # np.outer(A, B)
