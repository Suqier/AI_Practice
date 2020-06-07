# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第七十四题：给定一个 bincount 数组 C ，如何生成一个数组 A 使得 np.bincount（A）== C？
# Author: Jaime Fernández del Río

import numpy as np

C = np.bincount([1, 1, 2, 3, 4, 4, 6])
A = np.repeat(np.arange(len(C)), C)
print(A)

# 输出内容：
# [1 1 2 3 4 4 6]
