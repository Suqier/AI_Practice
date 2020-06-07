# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四十八题：打印出每一个 numpy scalar type 的最小值和最大值

import numpy as np

for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)

for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)

# 输出内容：
# -128
# 127
# -2147483648
# 2147483647
# -9223372036854775808
# 9223372036854775807
# -3.4028235e+38
# 3.4028235e+38
# 1.1920929e-07
# -1.7976931348623157e+308
# 1.7976931348623157e+308
# 2.220446049250313e-16
