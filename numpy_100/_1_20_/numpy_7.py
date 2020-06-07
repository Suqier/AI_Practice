# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第七题：创建一个包含从 10 数到 49 的向量

import numpy as np

Z = np.arange(10, 50)   # 左闭右开 [10, 50) == [10, 49]
print(Z)
print("Z.size = %d" % Z.size)

# 输出内容：
# [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
#  34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
# Z.size = 40
