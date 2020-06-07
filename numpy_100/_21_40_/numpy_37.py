# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十七题：建立一个 5 * 5 的矩阵，每一行的值是 0 ~ 4

import numpy as np

Z = np.zeros((5, 5))
Z += np.arange(5)
print(Z)

# 输出内容：
# [[0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]]
