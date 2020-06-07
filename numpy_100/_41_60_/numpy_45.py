# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四十五题：创建一个长度为 10 的随机向量并将其中的最大值替换为 0

import numpy as np

Z = np.random.random(10)
print(Z)
print("Z.argmax() = {}".format(Z.argmax()))

Z[Z.argmax()] = 0
print(Z)

# 输出内容：
# [0.49144213 0.96593108 0.36073926 0.0887971  0.98528178 0.53003355
#  0.41547721 0.47948056 0.05217259 0.14704299]
# Z.argmax() = 4
# [0.49144213 0.96593108 0.36073926 0.0887971  0.         0.53003355
#  0.41547721 0.47948056 0.05217259 0.14704299]
