# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十九题：创建一个长度为 10 的向量，并使它的值从 0 到 1 均匀分布（不包括 0 和 1）

import numpy as np

Z = np.linspace(0, 1, 11, endpoint=False)[1:]
print(Z)

# 输出内容：
# [0.09090909 0.18181818 0.27272727 0.36363636 0.45454545 0.54545455
#  0.63636364 0.72727273 0.81818182 0.90909091]


