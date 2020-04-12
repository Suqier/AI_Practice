# coding: utf-8
# King-Rook vs. King
# Video Link   --- https://www.bilibili.com/video/BV1dJ411B7gh
# Data set Link --- https://archive.ics.uci.edu/ml/datasets/Chess+%28King-Rook+vs.+King%29
#
# newX = (X - mean(X)) / std(X)
# This file provides preliminary data processing.

import chardet
import math
import random
from svmutil import *
from svm import *


def switch_alpha(x):
    """
    Implement a simple function like "switch".
    :param x: alpha 'a' -> 'h'
    :return:  corresponding number '1' -> '8'
    """
    return {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
    }.get(x)


def data_process_replace_alpha(filename):
    """
    Basically process data by replace its all alpha.
    :param filename: fill in a filename which is in the same folder
    :return: a list of string
    """
    f = None
    try:
        print("Opening the File ... ")
        f = open(filename, mode='rb')
        old_bytes = f.read()
    except IOError as e:
        print(e)
        print("Read file failure!")
    finally:
        if f:
            f.close()

    new_str_1 = []                              # new a null list to storage the string processed from bytes
    old_str = old_bytes.decode("ISO8859-1")     # bytes -> string
    old_str = old_str.splitlines()              # string -> string list
    for i in range(0, old_str.__len__()):       # replace alpha 'a' -> 'h' by number '1' -> '8'
        tmp_str = list(old_str[i])
        for j in range(0, 9, 4):
            tmp_str[j] = switch_alpha(tmp_str[j])
        new_str_1.append(''.join(tmp_str))

    new_str_2 = []                              # 'draw' -> '1', other labels -> '0'
    for i in range(0, old_str.__len__()):
        tmp_str = list(new_str_1[i])
        tmp_str = tmp_str[0:12]
        if i < 2796:
            tmp_str.append('1')
        else:
            tmp_str.append('0')
        new_str_2.append(''.join(tmp_str))

    return new_str_2                            # preliminarily process data, return a string list


def str_2_float(str_list):
    """
    Turn the string list into a new list which's type is float
    :param str_list: fill in a string list
    :return: a float type list, all data will not be change
    """
    float_list = []
    tmp_list = []
    for i in range(0, 28056):
        for j in range(0, 13, 2):
            tmp = ord(str_list[i][j]) - ord('0')
            tmp_list.append(tmp)
        float_list.append(tmp_list)
        tmp_list = []

    return float_list


def std_data(float_list):
    """
    Deliver a float list to standardization data
    newX = (X - mean(X)) / std(X)
    :param float_list: a float list needs standardization data
    :return:a standardization data float list
    """
    mean = []
    std = []
    for i in range(0, 11, 2):       # calculate mean(X)
        tmp = 0.0
        for j in range(0, len(float_list)):
            tmp += float_list[j][i]
        tmp /= len(float_list)
        mean.append(tmp)

    for i in range(0, 11, 2):       # calculate std(X)
        tmp = 0.0
        for j in range(0, len(float_list)):
            tmp += pow(float_list[j][i], 2)
        tmp /= len(float_list)
        std.append(tmp)

    standard_data = []              # storage new data
    tmp_data = []
    for i in range(0, len(float_list)):
        for j in range(0, 11, 2):
            tmp_data.append(float_list[i][j] / std[int(j / 2)])
        if i < 2796:
            tmp_data.append(1)
        else:
            tmp_data.append(0)
        standard_data.append(tmp_data)
        tmp_data = []

    return standard_data            # return a std float list


def std_data_2(float_list):
    """
    Deliver a float list to standardization data
    :param float_list: a float list needs to be storage as a file
    :return:a std float list
    """
    min = -1.0
    max = +1.0
    for i in range(0, len(float_list)):
        for j in range(0, 6):
            float_list[i][j] = min + (max - min) * (float_list[i][j] - min) / (max - min)

    return float_list


def pick_train_data_set(data_set, num):
    """
    Take 'num' samples and return a list with the samples
    :param data_set:Original data set
    :param num:how many samples does the train data set need, 0 ~ 28056
    :return:two float list, the first one is train data set, the second one is test data set
    """
    a = range(0, len(data_set))
    b = random.sample(a, num)
    b.sort()

    train_data_set = []
    for i in range(0, len(b)):
        train_data_set.append(data_set[b[i]])

    train_data_set = std_data_2(train_data_set)
    data_set = std_data_2(data_set)

    for i in range(0, len(b)):
        del data_set[b[i]-i]

    return train_data_set, data_set


