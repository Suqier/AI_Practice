# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五十八题：减去矩阵每一行的平均值
# Author: Warren Weckesser

import numpy as np

X = np.random.rand(5, 10)
print(X)

print("---------")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)

print("---------")
Y = X - X.mean(axis=1).reshape(-1, 1)
print(Y)

# 输出内容：
# [[0.10390655 0.6600301  0.01434809 0.12482884 0.75715722 0.95909009
#   0.98666232 0.69437215 0.06954609 0.0202844 ]
#  [0.46249362 0.29715481 0.08918475 0.67558941 0.84047092 0.03726131
#   0.36926107 0.43635883 0.18275328 0.92148257]
#  [0.65490981 0.39656296 0.20580925 0.38546453 0.28325033 0.12310282
#   0.4038367  0.71506946 0.13476112 0.91456292]
#  [0.26440613 0.37596305 0.24003645 0.65022313 0.15171946 0.94558686
#   0.26283581 0.80232413 0.47509017 0.68235535]
#  [0.01796809 0.14247757 0.96720642 0.72300312 0.03325496 0.61175663
#   0.67395649 0.65153409 0.37931172 0.54065312]]
# ---------
# [[-0.33511604  0.22100751 -0.42467449 -0.31419375  0.31813464  0.52006751
#    0.54763974  0.25534956 -0.36947649 -0.41873818]
#  [ 0.03129257 -0.13404625 -0.34201631  0.24438835  0.40926986 -0.39393974
#   -0.06193999  0.00515778 -0.24844778  0.49028151]
#  [ 0.23317682 -0.02517003 -0.21592374 -0.03626846 -0.13848266 -0.29863017
#   -0.01789629  0.29333647 -0.28697187  0.49282993]
#  [-0.22064792 -0.109091   -0.24501761  0.16516907 -0.33333459  0.46053281
#   -0.22221825  0.31727008 -0.00996388  0.19730129]
#  [-0.45614413 -0.33163465  0.4930942   0.2488909  -0.44085726  0.13764441
#    0.19984426  0.17742187 -0.0948005   0.0665409 ]]
# ---------
# [[-0.33511604  0.22100751 -0.42467449 -0.31419375  0.31813464  0.52006751
#    0.54763974  0.25534956 -0.36947649 -0.41873818]
#  [ 0.03129257 -0.13404625 -0.34201631  0.24438835  0.40926986 -0.39393974
#   -0.06193999  0.00515778 -0.24844778  0.49028151]
#  [ 0.23317682 -0.02517003 -0.21592374 -0.03626846 -0.13848266 -0.29863017
#   -0.01789629  0.29333647 -0.28697187  0.49282993]
#  [-0.22064792 -0.109091   -0.24501761  0.16516907 -0.33333459  0.46053281
#   -0.22221825  0.31727008 -0.00996388  0.19730129]
#  [-0.45614413 -0.33163465  0.4930942   0.2488909  -0.44085726  0.13764441
#    0.19984426  0.17742187 -0.0948005   0.0665409 ]]
