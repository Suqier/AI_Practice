# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十三题：如何找到数组中最频繁的值

import numpy as np

Z = np.random.randint(0, 10, 50)
print(Z)
print(np.bincount(Z).argmax())

# 输出内容：
# [7 4 9 9 1 9 8 3 2 5 3 8 9 6 4 6 0 7 8 9 2 8 4 5 7 9 8 6 5 0 8 2 3 5 2 3 1
#  8 9 0 2 1 8 4 3 3 3 7 9 8]
# 8
