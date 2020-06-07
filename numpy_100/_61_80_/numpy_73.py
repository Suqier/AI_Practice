# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第七十三题：考虑一组描述三个三角形（带有共享顶点）的 10 个三元组，找到组成所有三角形的一组唯一线段
# Author: Nicolas P. Rougier

import numpy as np

faces = np.random.randint(0, 100, (10, 3))
F = np.roll(faces.repeat(2, axis=1), -1, axis=1)
F = F.reshape(len(F) * 3, 2)
F = np.sort(F, axis=1)
G = F.view(dtype=[('p0', F.dtype), ('p1', F.dtype)])
G = np.unique(G)
print(G)

# 输出内容：
# [(11, 88) (11, 90) (12, 54) (12, 73) (23, 63) (23, 94) (26, 35) (26, 49)
#  (29, 38) (29, 67) (29, 76) (29, 95) (33, 47) (33, 55) (35, 49) (37, 53)
#  (37, 68) (38, 67) (47, 55) (53, 68) (54, 73) (58, 73) (58, 86) (63, 94)
#  (73, 86) (76, 95) (83, 87) (83, 88) (87, 88) (88, 90)]







