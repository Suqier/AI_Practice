# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第六十四题：对于给定向量，如何对由第二个向量索引的每个元素加1（注意重复索引）
# Author: Brett Olsen

import numpy as np

Z = np.ones(10)
I = np.random.randint(0, len(Z), 20)
print(Z)
print(I)

print("---------")
Z += np.bincount(I, minlength=len(Z))
print(Z)


# 另一种写法：
# Author： Bartosz Telenczuk
print("---------")
np.add.at(Z, I, 1)
print(Z)

# 输出内容：
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# [2 6 7 9 7 8 6 8 3 2 3 9 5 1 0 1 5 9 7 4]
# ---------
# [2. 3. 3. 3. 2. 3. 3. 4. 3. 4.]
# ---------
# [3. 5. 5. 5. 3. 5. 5. 7. 5. 7.]
