# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十三题：考虑形状为 (8,3) 和 (2, 2) 的两个数组 A 和 B。
# 如何查找包含 B 每行元素的 A 行，而不考虑 B 中元素的顺序
# Author: Gabe Schwartz

import numpy as np

A = np.random.randint(0, 5, (8, 3))
B = np.random.randint(0, 5, (2, 2))

C = (A[..., np.newaxis, np.newaxis] == B)
rows = np.where(C.any((3, 1)).all(1))[0]
print(rows)

# 输出内容：
# [0 3 4 5 6 7]
