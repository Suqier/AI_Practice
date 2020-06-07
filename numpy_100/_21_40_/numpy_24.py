# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十四题：将一个 5 * 3 的矩阵和一个 3 * 2 的矩阵进行矩阵乘法（生成一个 5 * 2 的矩阵）

import numpy as np

Z = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print(Z)

# 输出内容：
# [[3. 3.]
#  [3. 3.]
#  [3. 3.]
#  [3. 3.]
#  [3. 3.]]

# 在 Python 3.5+ 版本之中，还可以这样写：
Z = np.ones((5,3)) @ np.ones((3,2))
print(Z)

# 输出内容：
# [[3. 3.]
#  [3. 3.]
#  [3. 3.]
#  [3. 3.]
#  [3. 3.]]
