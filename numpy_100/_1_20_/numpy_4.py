# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四题：如何输出任意一个数组所占空间大小

import numpy as np

Z = np.zeros((10, 10))
print(Z)                                    # Z 是一个 10 * 10 的全零矩阵
print("Z.size = %d" % Z.size)               # Z.size 是指 Z 这个矩阵的元素个数
print("Z.itemsize = %d" % Z.itemsize)       # Z.itemsize 是指 Z 中每个元素所占空间大小
print("%d bytes" % (Z.size * Z.itemsize))   # 输出 Z 的所占空间大小

# 输出内容：
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
# Z.size = 100
# Z.itemsize = 8
# 800 bytes
