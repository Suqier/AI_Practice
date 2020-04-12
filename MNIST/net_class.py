# coding: utf-8
# Time: 2020/04/14
# Author: Suqier (https://suqier.github.io/)
# Create a Multi-Layer Perceptron,
#   which includes 1 input layer, 2 Hidden layers and 1 output layer,
#   to classify handwritten numbers('0' -> '9').
#       0. Load MNIST data set
#       1. Visualize data set
#    -> 2. Define Neural Networks(NN), loss function and optimizer
#       3. Train NN model, observe the training error and validate the change of training error
#       |—— 3.1 clean all gradient()        optimizer.zero_grad()
#       |—— 3.2 forward predict             output = model(data)
#       |—— 3.3 calculate loss function     loss = loss_cal(output, target)
#       |—— 3.4 back propagation            loss.backward()
#       |—— 3.5 optimize parameter          optimizer.step()
#       |—— 3.6 calculator mean train error and validation error every turn
#       4. Test the NN model
# MNIST data set Link:  http://yann.lecun.com/exdb/mnist/
# Keyword: PyTorch, MLP, MNIST
# Copyright 2020 Suqier


import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # set the neural number of the first and the second hidden layer
        hidden_layer_1 = 512
        hidden_layer_2 = 512
        dropout_rate = 0.2

        # define every layer's structure
        # input layer -> hidden layer 1
        #     28 * 28 -> 512
        self.fc1 = nn.Linear(28 * 28, hidden_layer_1)

        # hidden layer 1 -> hidden layer 2
        #            512 -> 512
        self.fc2 = nn.Linear(hidden_layer_1, hidden_layer_2)

        # hidden layer 2 -> output layer(one-hot vector)
        #            512 -> 10
        self.fc3 = nn.Linear(hidden_layer_2, 10)

        # set the rate of Dropout for preventing overfitting
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x):
        # The function of view () is to splice a multi-line Tensor into one line
        x = x.view(-1, 28 * 28)
        # Get through first hidden layer which's Activation Function is Relu(x)
        x = F.relu(self.fc1(x))
        # dropout some neural unit for preventing overfitting
        x = self.dropout(x)
        # Get through second hidden layer which's Activation Function is Relu(x)
        x = F.relu(self.fc2(x))
        # dropout some neural unit for preventing overfitting
        x = self.dropout(x)
        # output layer
        x = self.fc3(x)
        return x


