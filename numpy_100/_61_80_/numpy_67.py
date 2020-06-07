# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六十七题：考虑一个四维数组，如何一次性获取最后两个轴的总和？

import numpy as np

A = np.random.randint(0, 10, (3, 4, 3, 4))

sum = A.sum(axis=(-2, -1))
print(sum)

print("---------")
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)

# 输出内容：
# [[50 46 55 57]
#  [48 63 64 64]
#  [47 46 45 54]]
# ---------
# [[50 46 55 57]
#  [48 63 64 64]
#  [47 46 45 54]]
