# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六十一题：从一个给定的数组中找到一个最近的值

import numpy as np

Z = np.random.uniform(0,1,10)
print(Z)

z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)

# 输出结果：
# [0.40274056 0.8709391  0.68230226 0.51206309 0.15856052 0.32765433
#  0.6976465  0.16289206 0.86834854 0.44532821]
# 0.5120630876746566
