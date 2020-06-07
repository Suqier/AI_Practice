# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第四十三题：将一个数组设置为不可修改（只读）

import numpy as np

Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1

# 输出内容：\
# ValueError: assignment destination is read-only
