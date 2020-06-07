# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十五题：给定一维数组，将 3 到 8 之间的所有元素取反（原地算法）

# Author: Evgeni Burovski

import numpy as np

Z = np.arange(11)

Z[(3 < Z) & (Z < 8)] *= -1
print(Z)

# 输出内容：
# [ 0  1  2  3 -4 -5 -6 -7  8  9 10]
