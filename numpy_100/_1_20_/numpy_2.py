# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第二题：尝试打印输出 numpy 当前的版本及其配置

import numpy as np

print(np.__version__)
np.show_config()

# 输出内容：
# 1.18.2
# blas_mkl_info:
#   NOT AVAILABLE
# blis_info:
#   NOT AVAILABLE
# openblas_info:
#     library_dirs = ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas_info']
#     libraries = ['openblas_info']
#     language = f77
#     define_macros = [('HAVE_CBLAS', None)]
# blas_opt_info:
#     library_dirs = ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas_info']
#     libraries = ['openblas_info']
#     language = f77
#     define_macros = [('HAVE_CBLAS', None)]
# lapack_mkl_info:
#   NOT AVAILABLE
# openblas_lapack_info:
#     library_dirs = ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas_lapack_info']
#     libraries = ['openblas_lapack_info']
#     language = f77
#     define_macros = [('HAVE_CBLAS', None)]
# lapack_opt_info:
#     library_dirs = ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas_lapack_info']
#     libraries = ['openblas_lapack_info']
#     language = f77
#     define_macros = [('HAVE_CBLAS', None)]
