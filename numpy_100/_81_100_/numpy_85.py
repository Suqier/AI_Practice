# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十五题：创建二维数组类，使得 Z[i, j] == Z [j, i]（对称矩阵）
# Author: Eric O. Lebigot

import numpy as np


class Symetric(np.ndarray):
    def __setitem__(self, index, value):
        i, j = index
        super(Symetric, self).__setitem__((i,j), value)
        super(Symetric, self).__setitem__((j,i), value)


def symetric(Z):
    return np.asarray(Z + Z.T - np.diag(Z.diagonal())).view(Symetric)


S = symetric(np.random.randint(0, 10, (5, 5)))
S[2, 3] = 42
print(S)

# 输出内容：
# [[ 9 14  8  8  7]
#  [14  8  8 14  8]
#  [ 8  8  8 42 10]
#  [ 8 14 42  6 17]
#  [ 7  8 10 17  9]]
