# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十八题：下面的表达式结果是什么？
# " / " 就表示 浮点数除法，返回浮点结果; " // "表示整数除法
# np.array(0) / np.array(0)
# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)

import numpy as np

# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))

# 输出内容：
# nan     # RuntimeWarning
# 0       # RuntimeWarning
# [-2.14748365e+09]
