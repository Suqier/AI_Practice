# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十二题：下面这个表达式是正确的嘛？、
# np.sqrt(-1) == np.emath.sqrt(-1)

import numpy as np

print(np.sqrt(-1) == np.emath.sqrt(-1))

# 输出内容：
# False
