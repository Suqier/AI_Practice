# coding:utf-8
import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

if __name__ == '__main__':
    f = None
    try:
        f = open('c_gamma.data', 'r')
        f_str = f.read()
    except IOError as e:
        print(e)
        print("Read file failure!")
    finally:
        if f:
            f.close()

    data_str = f_str.splitlines()
    data_str_2 = []
    for i in range(1, len(data_str), 2):
        data_str_2.append(data_str[i])

    data_str_3 = []
    for i in range(0, len(data_str_2), 2):
        data_str_3.append(data_str_2[i] + data_str_2[i + 1])

    for i in range(0, len(data_str_3)):
        data_str_3[i] = data_str_3[i][-6:]

    for i in range(0, len(data_str_3)):
        for j in range(0, len(data_str_3[i])):
            ch = data_str_3[i][j]
            if ch == '=' or ch == ' ' or ch == '%':
                tmp_str = data_str_3[i].replace('=', '')
                tmp_str = tmp_str.replace(' ', '')
                tmp_str = tmp_str.replace('%', '')
                data_str_3[i] = tmp_str
                break
    print(len(data_str_3))

    data_float = []
    tmp_float = []
    for i in range(0, 21):
        for j in range(0, 19):
            tmp_float.append(i)
            tmp_float.append(j)
            tmp_float.append(float(data_str_3[i * 19 + j]))
            data_float.append(tmp_float)
            tmp_float = []

    # print(data_float)
    c = []
    gamma = []
    acc = []
    azz = []
    for i in range(0, 21):
        x = pow(2, i - 5)
        c.append(x)
    for i in range(0, 19):
        y = pow(2, i - 15)
        gamma.append(y)
    for i in range(0, 21):
        for j in range(0, 19):
            z = data_float[i * 19 + j][2]
            azz.append(z)
        acc.append(azz)
        azz = []

    print(c)
    print(gamma)
    print(acc)


