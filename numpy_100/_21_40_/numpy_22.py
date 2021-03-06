# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十二题：标准化一个 5 * 5 的随机矩阵

import numpy as np

Z = np.random.random((5, 5))
Z = (Z - np.mean(Z)) / (np.std(Z))
print(Z)

# 输出内容：
# [[-0.41385017 -0.12246501 -0.24678733  1.26145706 -0.94010373]
#  [-0.54032354  0.86548363  1.6279542  -1.48722093 -0.81624013]
#  [-0.88303895 -0.02645589  0.90420215 -0.47426838 -1.10258196]
#  [ 0.01382214 -1.19919708  1.61705344  0.89042187  1.02472124]
#  [-0.17255784  1.51810484 -1.39233451 -1.07010344  1.1643083 ]]
