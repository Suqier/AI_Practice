# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第九十九题：采用自助法计算给定一维数组在 95% 置信区间上的算术平均值

import numpy as np

X = np.random.randn(100)  # 一维数组
N = 1000  # 自抽取数量

idx = np.random.randint(0, X.size, (N, X.size))  # 生成1000x100的随机索引数组
means = np.mean(X[idx], axis=1)  # 相当于对每一行的100个抽样值计算平均值，结果一个大小为1000的一维数组

confint = np.percentile(means, [2.5, 97.5])  # 计算百分位数 百分位数是统计中使用的度量，表示小于这个值的观察值占总数q的百分比
print(confint)

# 输出内容：
# [-0.10679404  0.23348956]
