# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四十一题：如何求解一个小数组元素之和（比使用 np.sum 快）
# Author: Evgeni Burovski

import numpy as np

Z = np.arange(10)
np.add.reduce(Z)
