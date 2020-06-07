# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五十九题：如何根据第 n 列对一个数组排序
# Author: Steve Tjoa

import numpy as np

Z = np.random.randint(0, 10, (3, 3))
print(Z)
print(Z[Z[:, 1].argsort()])

# 输出内容：
# [[5 5 0]
#  [1 5 0]
#  [2 3 1]]
# [[2 3 1]
#  [5 5 0]
#  [1 5 0]]
