# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十题：找到两个数组之中的共同值

import numpy as np

Z1 = np.random.randint(0, 10, 10)   # 随机生成 0 到 9 中的数字，组成数组，长度为 10
Z2 = np.random.randint(0, 10, 10)
print(Z1)
print(Z2)
print(np.intersect1d(Z1, Z2))       # intersect： 相交

# 输出内容：
# [9 0 0 3 3 8 0 4 5 9]
# [3 7 2 8 0 7 8 0 6 1]
# [0 3 8]
