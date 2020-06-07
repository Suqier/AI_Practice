# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十八题：定义一个可以生成 10 个整数的函数，并使用它创建一个数组

import numpy as np


def generate():
    for x in range(10):
        yield x


Z = np.fromiter(generate(), dtype=float, count=-1)
print(Z)

# 输出内容：
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]