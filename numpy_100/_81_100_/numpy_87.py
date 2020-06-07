# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第八十七题：考虑一个 16 x 16 的数组，如何获取块总和（块大小为 4 x 4 ）
# Author: Robert Kern

import numpy as np

Z = np.ones((16, 16))
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                    np.arange(0, Z.shape[1], k), axis=1)
print(S)

# 输出内容：
# [[16. 16. 16. 16.]
#  [16. 16. 16. 16.]
#  [16. 16. 16. 16.]
#  [16. 16. 16. 16.]]
