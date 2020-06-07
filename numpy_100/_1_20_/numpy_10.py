# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第十题：找到一个数组中的非零元素索引，这里的数组譬如：[1, 2, 0, 0, 4, 0]

import numpy as np

nz = np.nonzero([1, 2, 0, 0, 4, 0])
print(nz)

# 输出内容：
# (array([0, 1, 4], dtype=int64),)
