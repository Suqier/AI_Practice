# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第十七题：以下表达式的结果是怎样的？
#           0 * np.nan
#           np.nan == np.nan
#           np.inf > np.nan
#           np.nan - np.nan
#           np.nan in set([np.nan])
#           0.3 == 3 * 0.1

import numpy as np

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

# 输出内容：
# nan
# False
# False
# nan
# True
# False
