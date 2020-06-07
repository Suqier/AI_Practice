# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二十九题：如何将浮点数组做四舍五入处理？
# Author: Charles R Harris
import numpy as np

Z = np.random.uniform(-10, +10, 10)
print(Z)
# 输出内容：
# [ 7.42284143  2.38008643 -2.4767967  -2.6985632  -1.2463757   6.90514651
#  -2.5095747   8.95570304  5.09204995  6.70874907]

print(np.copysign(np.ceil(np.abs(Z)), Z))

# 输出内容：
# [ 8.  3. -3. -3. -2.  7. -3.  9.  6.  7.]

# ---------------------------------------------
# 可读性更强但是效率较低的代码：
print(np.where(Z > 0, np.ceil(Z), np.floor(Z)))

# 输出内容：
# [ 8.  3. -3. -3. -2.  7. -3.  9.  6.  7.]

# 说实话吧，两种代码对我来说都不怎么可读......
