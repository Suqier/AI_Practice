# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六题：创建一个长度为 10 的空向量，然后将向量中第 5 个数字改为 1

import numpy as np

Z = np.zeros(10)
print(Z)

Z[4] = 1
print(Z)

# 输出内容：
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
#              |
#  1  2  3  4  5  6  7  8  9  10
