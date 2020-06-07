# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十二题：计算矩阵的秩
# Author: Stefan van der Walt

import numpy as np

Z = np.random.uniform(0, 1, (10, 10))
U, S, V = np.linalg.svd(Z)      # Singular Value Decomposition
rank = np.sum(S > 1e-10)
print(rank)

# 输出内容：
# 10
