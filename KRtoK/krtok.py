# coding: utf-8
# King-Rook vs. King
# Video Link   --- https://www.bilibili.com/video/BV1dJ411B7gh
# Data set Link --- https://archive.ics.uci.edu/ml/datasets/Chess+%28King-Rook+vs.+King%29
#
# 5-fold SVM to solve King-Rook vs. King
# CScale = [2^(-5), 2^(15)]; gamma = [2^(-15), 2^3]
# Kernel function: rbf
# This file try to train a SVM to solve the question.

from svmutil import *
from svm import *
from data_process import *
from torch.utils.tensorboard import SummaryWriter
import chardet
import math
import random


def train_with_svm(train_data_set, c, gamma):
    """
    Use the function which is defined by "svmutil" to train a SVM model
    :param train_data_set:the data set which is used to train a SVM model
    :param c: penalty parameter
    :param gamma: kernel parameter
    :return:the SVM training model m
    """
    train_data_set_x = []
    train_data_set_y = []
    for i in range(0, len(train_data_set)):
        train_data_set_x.append(train_data_set[i][0:6])
        train_data_set_y.append(train_data_set[i][6])

    # when using the svm_train function, if there is a "-v" in the input parameter,
    # then the return of this function will be a number,
    # which is the accuracy of cross validation or the error of regression

    options = "-s 0 -t 2 -c " + str(c) + " -g " + str(gamma)
    m = svm_train(train_data_set_y, train_data_set_x, options)

    print("-------------------")
    return m


def find_best_c_gamma(train_data_set, c, gamma):
    """
    Use the function which is defined by "svmutil" to train a SVM model
    :param train_data_set:the data set which is used to train a SVM model
    :param c: penalty parameter
    :param gamma: kernel parameter
    :return:accuracy of the SVM training model
    """
    train_data_set_x = []
    train_data_set_y = []
    for i in range(0, len(train_data_set)):
        train_data_set_x.append(train_data_set[i][0:6])
        train_data_set_y.append(train_data_set[i][6])

    # when using the svm_train function, if there is a "-v" in the input parameter,
    # then the return of this function will be a number,
    # which is the accuracy of cross validation or the error of regression
    options_1 = "-s 0 -t 2 -c 256.0 -g 0.0625"
    options = "-s 0 -t 2 -c " + str(c) + " -g " + str(gamma) + " -v 5 -q"
    acc = svm_train(train_data_set_y, train_data_set_x, options)
    # "-s 0 -t 2 -c 16 -g 0.0825 -v 5"   b = 6.2863 support vector number: 358(162+ / 196-)

    # the number of the Support Vector in the training model should be 20% ~ 30% of the all training data set,
    # which indicates this training model is proper

    print("-------------------")
    return acc


def test_with_svm(test_data_set, model):
    """
    Testing function which is used to test the model's performance
    :param test_data_set: test data set
    :param model:the SVM model which trained just now
    :return:accuracy of model
    """
    test_data_set_x = []
    test_data_set_y = []
    for i in range(0, len(test_data_set)):
        test_data_set_x.append(test_data_set[i][0:6])
        test_data_set_y.append(test_data_set[i][6])

    [pred, acc, preb] = svm_predict(test_data_set_y, test_data_set_x,  model)
    return acc[0]


if __name__ == '__main__':
    str_data = data_process_replace_alpha('krkopt.data')                    # data : string list
    float_data = str_2_float(str_data)                                      # string list ->  float list
    train_data_set, test_data_set = pick_train_data_set(float_data, 5000)

    # CScale = [2^(-5), 2^(15)]; gamma = [2^(-15), 2^3]
    c = pow(2, -5)
    gamma = pow(2, -15)

    # Use cross validation to find the best parameter C and Gamma
    best_para = [0.0, 0.0, 0.0]     # best_para [accuracy, c, gamma]
    temp_para = [0.0, 0.0, 0.0]
    c_gamma_para = []
    for i in range(0, 21):
        for j in range(0, 19):
            accuracy = find_best_c_gamma(train_data_set, c, gamma)
            temp_para[0] = accuracy
            temp_para[1] = c
            temp_para[2] = gamma
            c_gamma_para.append(temp_para)

            tmp_acc = best_para[0]
            print(i, j, accuracy, tmp_acc)
            if accuracy > tmp_acc:
                best_para[0] = accuracy
                best_para[1] = c
                best_para[2] = gamma
            print(best_para)
            gamma *= 2
        c *= 2
        gamma = pow(2, -15)

    # Use the best parameter C and Gamma to train the whole training set
    print("-------------train_svm--------------------")
    print(best_para)
    model = train_with_svm(train_data_set, best_para[1], best_para[2])
    # model = train_with_svm(train_data_set, '256', '0.0625')

    # Test
    print("-------------test_svm--------------------")
    accuracy = test_with_svm(test_data_set, model)
    print(accuracy)

    f = None
    try:
        f = open('c_gamma_acc.data', 'a+')
        for i in range(0, len(c_gamma_para)):
            str_tmp = str(c_gamma_para[i]) + "\n"
            f.write(str_tmp)
    except IOError as e:
        print(e)
        print("Write file failure!")
    finally:
        if f:
            f.close()

