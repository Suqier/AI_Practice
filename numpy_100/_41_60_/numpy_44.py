# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四十四题：将一个随机 10 * 2 的矩阵所代表笛卡尔直角坐标系，转换为极坐标系

import numpy as np

Z = np.random.random((10, 2))
print(Z)
X, Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2 + Y**2)
T = np.arctan2(Y, X)
print(R)
print(T)

# 输出内容：
# [[0.61999853 0.61010719]
#  [0.54858923 0.04905299]
#  [0.65774281 0.59063217]
#  [0.13931777 0.66686489]
#  [0.22346634 0.52678883]
#  [0.01589509 0.87348848]
#  [0.532719   0.94491916]
#  [0.47117303 0.17688632]
#  [0.75746751 0.56644667]
#  [0.97481017 0.56193747]]
# [0.86984421 0.55077794 0.88400903 0.68126223 0.57222694 0.8736331
#  1.08474041 0.50328202 0.94584293 1.12517936]
# [0.77735729 0.08917945 0.73169146 1.36484397 1.16959943 1.55260108
#  1.0574411  0.35913614 0.64210218 0.52292959]
