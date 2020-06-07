# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四十二题：判断两个随机矩阵 A 和 B 是否相等

import numpy as np

A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)

equal = np.allclose(A, B)
print(equal)

equal = np.array_equal(A, B)
print(equal)

# 输出内容：
# False
# False
