# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十六题：使用 5 种不同的方法从一个随机数组中提取整数

import numpy as np

Z = np.random.uniform(0, 10, 10)
print(Z)

print("---------")
print(Z - Z%1)

print("---------")
print(Z // 1)

print("---------")
print(np.floor(Z))

print("---------")
print(Z.astype(int))

print("---------")
print(np.trunc(Z))

# 输出内容：
# [3.87336583 1.65653583 9.84931723 1.49893155 9.56340532 0.56659798
#  2.98708039 3.00108543 3.91187867 3.70038604]
# ---------
# [3. 1. 9. 1. 9. 0. 2. 3. 3. 3.]
# ---------
# [3. 1. 9. 1. 9. 0. 2. 3. 3. 3.]
# ---------
# [3. 1. 9. 1. 9. 0. 2. 3. 3. 3.]
# ---------
# [3 1 9 1 9 0 2 3 3 3]
# ---------
# [3. 1. 9. 1. 9. 0. 2. 3. 3. 3.]
