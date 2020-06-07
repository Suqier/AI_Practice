# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十题：在一个 (6, 7, 8) 的三维数组中，第一百个元素的索引是多少？

import numpy as np

print(np.unravel_index(99, (6, 7, 8)))

# 输出内容：
# (1, 5, 3)

# 解释：100 = 99 + 1 = 1 * (7 * 8) + 5 * (8) + 3 * (1) + 1
