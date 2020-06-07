# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五十四题：读取以下的文件
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11

import numpy as np
from io import StringIO

s = StringIO('''1, 2, 3, 4, 5
                6,  ,  , 7, 8
                 ,  , 9,10,11
''')
Z = np.genfromtxt(s, delimiter=",", dtype=np.int)
print(Z)

# 输出内容：
# [[ 1  2  3  4  5]
#  [ 6 -1 -1  7  8]
#  [-1 -1  9 10 11]]

