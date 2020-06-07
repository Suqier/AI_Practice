# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六十五题：如何基于索引列表（I）将向量（X）的元素累积到数组（F）？

# Author: Alan G Isaac

import numpy as np

X = [1, 2, 3, 4, 5, 6]
I = [1, 3, 9, 3, 4, 1]
F = np.bincount(I, X)
print(F)

# 输出内容：
# [0. 7. 0. 6. 5. 0. 0. 0. 0. 3.]
