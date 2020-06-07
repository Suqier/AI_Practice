# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五十一题：定义一个结构数组表示一个位置 (x, y) 和一种颜色 (r, g, b)

import numpy as np

Z = np.zeros(10, [('position', [('x', float, 1),
                                ('y', float, 1)]),
                  ('color', [('r', float, 1),
                             ('g', float, 1),
                             ('b', float, 1)])])
print(Z)

# 输出内容：
# [((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
#  ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
#  ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
#  ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))
#  ((0., 0.), (0., 0., 0.)) ((0., 0.), (0., 0., 0.))]
