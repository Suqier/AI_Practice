# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十七题：对于一个整数向量Z，以下哪个表达式是合法的？
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z

Z**Z            # 不合法
2 << Z >> 2     # 合法
Z <- Z          # 合法
1j*Z            # 合法
Z/1/1           # 合法
Z<Z>Z           # 不合法
