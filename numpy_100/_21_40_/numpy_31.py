# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第三十一题：如何忽略所有的来自于 numpy 的 warning 警告 （不被推荐）

import numpy as np

# 忽略 warning 提示
defaults = np.seterr(all="ignore")      # np.seterr: 设置如何处理浮点错误。
Z = np.ones(1) / 0

# 打开 warning 提示
_ = np.seterr(**defaults)

# 等效于上下文管理器
with np.errstate(all="ignore"):
    np.arange(3) / 0
