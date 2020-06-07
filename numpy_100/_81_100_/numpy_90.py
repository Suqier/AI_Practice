# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十题：给定任意数量的向量，构建笛卡尔乘积（每一项的每种组合）
# Author: Stefan Van der Walt

import numpy as np


def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)

    ix = np.indices(shape, dtype=int)
    ix = ix.reshape(len(arrays), -1).T

    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]
        return ix


print(cartesian(([1, 2, 3], [4, 5], [6, 7])))

# 输出内容：
# [[1 0 0]
#  [1 0 1]
#  [1 1 0]
#  [1 1 1]
#  [2 0 0]
#  [2 0 1]
#  [2 1 0]
#  [2 1 1]
#  [3 0 0]
#  [3 0 1]
#  [3 1 0]
#  [3 1 1]]
