# coding: utf-8
# Time: 2020/04/14
# Author: Suqier (https://suqier.github.io/)
# Create a Multi-Layer Perceptron,
#   which includes 1 input layer, 2 Hidden layers and 1 output layer,
#   to classify handwritten numbers('0' -> '9').
#    -> 0. Load MNIST data set
#    -> 1. Visualize data
#       2. Define Neural Networks(NN), loss function and optimizer
#    -> 3. Train NN model, observe the training error and validate the change of training error
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


import numpy as np
import torch
import torchvision.transforms as transforms
from matplotlib import pyplot as plt
from torch.utils.data.dataloader import DataLoader as Dataloader
from torch.utils.data.sampler import SubsetRandomSampler
from torchvision import datasets

from net_class import *

# the numbers of cpu we use in loading data
num_workers = 0

# the size of a data batch
batch_size = 20

# the proportion of validation
valid_size = 0.2

# training times
# Traverse all of the picture in the train_data_set every turn
training_times = 50

# transform the data type into Tensor which is defined in PyTorch
# Convert a ``PIL Image`` or ``numpy.ndarray`` to tensor
transform = transforms.ToTensor()

# load data into train_data_set and test_data_set
train_data_set = datasets.MNIST(root='MNIST_data', train=True, download=True, transform=transform)
test_data_set = datasets.MNIST(root='MNIST_data', train=False, download=True, transform=transform)

# shuffle the index of every image in the train data set
num_train = len(train_data_set)
indices = list(range(num_train))
np.random.shuffle(indices)
split = int(np.floor(num_train * valid_size))
train_index, valid_index = indices[split:], indices[:split]

# then separate them into train data set and valid data set according to the train_index and valid_index
# SubsetRandomSampler is a Sampler that always used to separate the data set into train_data_set and valid_data_set
train_sampler = SubsetRandomSampler(train_index)
valid_sampler = SubsetRandomSampler(valid_index)

# create Dataloader of the train_data_set, valid_data_set and test_data_set
# Dataloader: a kind of python builder, which returns a batch of data one time
train_loader = Dataloader(train_data_set, batch_size=batch_size, sampler=train_sampler, num_workers=num_workers)
valid_loader = Dataloader(train_data_set, batch_size=batch_size, sampler=valid_sampler, num_workers=num_workers)
test_loader = Dataloader(test_data_set, batch_size=batch_size, num_workers=num_workers)

# define CrossEntropyLoss as loss function
loss_cal = nn.CrossEntropyLoss()


if __name__ == "__main__":
    # create a example of Net()
    model = Net()
    # define the optimizer(Stochastic Gradient Descent, SGD) and set the learning rate
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    # num_train_data_set = len(train_data_set)

    # set the validate loss as Positive infinity
    valid_loss_min = np.Inf

    # storage train_loss and valid_loss into list
    train_loss_list = []
    valid_loss_list = []

    # every turn of train
    for i in range(0, training_times):
        train_loss = 0.0
        valid_loss = 0.0

        # start training model
        # turn the model into train mode
        model.train()

        for data, target in train_loader:
            optimizer.zero_grad()                     # 3.1
            output = model(data)                      # 3.2
            loss = loss_cal(output, target)           # 3.3
            loss.backward()                           # 3.4
            optimizer.step()                          # 3.5
            train_loss += loss.item() * data.size(0)  # 3.6

        # start validation model
        # turn the model into valid mode, close the dropout and BN layers
        model.eval()

        for data, target in valid_loader:
            output = model(data)
            loss = loss_cal(output, target)
            valid_loss += loss.item() * data.size(0)

        # record two datum: train_loss and valid_loss
        train_loss /= len(train_loader.dataset)
        valid_loss /= len(valid_loader.dataset)
        train_loss_list.append(train_loss)
        valid_loss_list.append(valid_loss)
        print("---The {}th training --- train_loss : {}, valid loss : {}---".format(i, train_loss, valid_loss))

        # if this batch's valid_loss lower than before, than save this model
        if valid_loss <= valid_loss_min:
            print("---valid loss is lower than before for: {:.6f}, "
                  "this model will be saved---".format(valid_loss_min - valid_loss))
            torch.save(model.state_dict(), 'model.pt')
            valid_loss_min = valid_loss

    # 1. visualize the data
    plt.plot(train_loss_list, label='train loss')
    plt.plot(valid_loss_list, label='valid loss')
    plt.legend()
    plt.title('The change of train loss and valid loss')
    plt.show()

    plt.plot(valid_loss_list, label='valid loss', c='r')
    plt.title('valid loss change')
    plt.show()


