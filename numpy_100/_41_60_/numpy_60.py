# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六十题：判断一个二维数组里面存在空列
# Author: Warren Weckesser

import numpy as np

Z = np.random.randint(0, 2, (3, 10))
print(Z)
print((~Z.any(axis=0)).any())

# 输出内容：
# [[0 0 1 1 1 1 0 0 0 1]
#  [1 1 1 1 0 0 0 0 1 0]
#  [0 1 1 1 1 0 0 1 0 1]]
# True
