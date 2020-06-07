# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十六题：考虑一组形状为 (n，n) 的 p 个矩阵和一组形状为 (n, 1) 的 p 个向量。
# 如何一次计算 p 个矩阵乘积的总和？ （结果的形状为 (n，1) ）
# Author: Stefan van der Walt

import numpy as np

p, n = 10, 20
M = np.ones((p, n, n))
V = np.ones((p, n, 1))
S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])
print(S)

# 输出内容：
# [[200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]
#  [200.]]
