# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五十三题：将一个32bits的浮点型转换成一个32bits的整型

import numpy as np

Z = np.arange(10, dtype=np.float32)
print(Z)

Z = Z.astype(np.int32, copy=False)
print(Z)

# 输出内容:
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
# [0 1 2 3 4 5 6 7 8 9]
