# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十九题：如何获得数组的 n 个最大值

import numpy as np

Z = np.arange(10000)
np.random.shuffle(Z)
n = 5

# 慢的写法：
print(Z[np.argsort(Z)[-n:]])

print("---------")
# 快的写法：
print(Z[np.argpartition(-Z, n)[:n]])

# 输出内容：
# [9995 9996 9997 9998 9999]
# ---------
# [9999 9998 9997 9996 9995]
