# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十二题：考虑一个大向量 Z ，使用 3 种不同的方法计算 Z 的 3 次幂
# Author: Ryan G.

import numpy as np

x = np.random.rand(int(5e7))
print(x)

print("---------")
print(np.power(x, 3))


print("---------")
print(x * x * x)

print("---------")
print(np.einsum('i,i,i->i', x, x, x))

# 输出内容：
# [0.63246632 0.89857431 0.82259112 ... 0.02040807 0.76213238 0.96071966]
# ---------
# [2.52995159e-01 7.25541067e-01 5.56611341e-01 ... 8.49974536e-06
#  4.42681362e-01 8.86727217e-01]
# ---------
# [2.52995159e-01 7.25541067e-01 5.56611341e-01 ... 8.49974536e-06
#  4.42681362e-01 8.86727217e-01]
# ---------
# [2.52995159e-01 7.25541067e-01 5.56611341e-01 ... 8.49974536e-06
#  4.42681362e-01 8.86727217e-01]

# 个人感觉速度： SLOW 1 < 2 < 3 FAST
