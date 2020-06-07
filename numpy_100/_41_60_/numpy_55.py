# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五十五题：numpy 数组的枚举等效于什么

import numpy as np

Z = np.arange(9).reshape(3, 3)
for index, value in np.ndenumerate(Z):
    print(index, value)
for index in np.ndindex(Z.shape):
    print(index, Z[index])

# 输出内容：
# (0, 0) 0
# (0, 1) 1
# (0, 2) 2
# (1, 0) 3
# (1, 1) 4
# (1, 2) 5
# (2, 0) 6
# (2, 1) 7
# (2, 2) 8
# (0, 0) 0
# (0, 1) 1
# (0, 2) 2
# (1, 0) 3
# (1, 1) 4
# (1, 2) 5
# (2, 0) 6
# (2, 1) 7
# (2, 2) 8
