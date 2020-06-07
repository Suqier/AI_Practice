# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十六题：给定二维数组，如何提取唯一行
# Author: Jaime Fernández del Río

import numpy as np

Z = np.random.randint(0, 2, (6, 3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
_, idx = np.unique(T, return_index=True)
uZ = Z[idx]
print(uZ)

# Author: Andreas Kouzelis
# NumPy >= 1.13
print("---------")
uZ = np.unique(Z, axis=0)
print(uZ)

# 输出内容：
# [[0 0 1]
#  [0 1 1]
#  [1 0 0]
#  [1 0 1]
#  [1 1 0]]
# ---------
# [[0 0 1]
#  [0 1 1]
#  [1 0 0]
#  [1 0 1]
#  [1 1 0]]



