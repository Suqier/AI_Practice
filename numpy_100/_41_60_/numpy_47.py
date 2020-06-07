# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四十七题： 给定两个数组 X 和 Y，建立柯西矩阵C(Cij = 1/(xi - yj))
# Author: Evgeni Burovski

import numpy as np

X = np.arange(8)
print(X)

Y = X + 0.5
print(Y)

C = 1.0 / np.subtract.outer(X, Y)
print(C)

print(np.linalg.det(C))

# 输出内容：
# [0 1 2 3 4 5 6 7]
# [0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5]
# [[-2.         -0.66666667 -0.4        -0.28571429 -0.22222222 -0.18181818
#   -0.15384615 -0.13333333]
#  [ 2.         -2.         -0.66666667 -0.4        -0.28571429 -0.22222222
#   -0.18181818 -0.15384615]
#  [ 0.66666667  2.         -2.         -0.66666667 -0.4        -0.28571429
#   -0.22222222 -0.18181818]
#  [ 0.4         0.66666667  2.         -2.         -0.66666667 -0.4
#   -0.28571429 -0.22222222]
#  [ 0.28571429  0.4         0.66666667  2.         -2.         -0.66666667
#   -0.4        -0.28571429]
#  [ 0.22222222  0.28571429  0.4         0.66666667  2.         -2.
#   -0.66666667 -0.4       ]
#  [ 0.18181818  0.22222222  0.28571429  0.4         0.66666667  2.
#   -2.         -0.66666667]
#  [ 0.15384615  0.18181818  0.22222222  0.28571429  0.4         0.66666667
#    2.         -2.        ]]
# 3638.163637117973
