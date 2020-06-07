# !/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2020/06/06
# author: Suqier
# email: suqier5637@foxmail.com
# 在这里尝试着翻译并自己练习黄海广博士的numpy-100项目
# 项目原地址：https://github.com/rougier/numpy-100

# 第五题：如何从命令行获取numpy add函数的文档？
# windows系统下的操作：
# 0. 同时按下：win + R
# 1. 输入 cmd 并回车调出命令行
# 2. 输入 python -c "import numpy; numpy.info(numpy.add)"

# （命令行）输出内容：
# add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
#
# Add arguments element-wise.
#
# Parameters
# ----------
# x1, x2 : array_like
#     The arrays to be added. If ``x1.shape != x2.shape``, they must be broadcastable to a common shape (which becomes the shape of the output).
# out : ndarray, None, or tuple of ndarray and None, optional
#     A location into which the result is stored. If provided, it must have
#     a shape that the inputs broadcast to. If not provided or None,
#     a freshly-allocated array is returned. A tuple (possible only as a
#     keyword argument) must have length equal to the number of outputs.
# where : array_like, optional
#     This condition is broadcast over the input. At locations where the
#     condition is True, the `out` array will be set to the ufunc result.
#     Elsewhere, the `out` array will retain its original value.
#     Note that if an uninitialized `out` array is created via the default
#     ``out=None``, locations within it where the condition is False will
#     remain uninitialized.
# **kwargs
#     For other keyword-only arguments, see the
#     :ref:`ufunc docs <ufuncs.kwargs>`.
#
# Returns
# -------
# add : ndarray or scalar
#     The sum of `x1` and `x2`, element-wise.
#     This is a scalar if both `x1` and `x2` are scalars.
#
# Notes
# -----
# Equivalent to `x1` + `x2` in terms of array broadcasting.
#
# Examples
# --------
# >>> np.add(1.0, 4.0)
# 5.0
# >>> x1 = np.arange(9.0).reshape((3, 3))
# >>> x2 = np.arange(3.0)
# >>> np.add(x1, x2)
# array([[  0.,   2.,   4.],
#        [  3.,   5.,   7.],
#        [  6.,   8.,  10.]])
