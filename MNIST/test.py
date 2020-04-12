# coding: utf-8
# Time: 2020/04/14
# Author: Suqier (https://suqier.github.io/)
# Create a Multi-Layer Perceptron,
#   which includes 1 input layer, 2 Hidden layers and 1 output layer,
#   to classify handwritten numbers('0' -> '9').
#       0. Load MNIST data set
#       1. Visualize data set
#       2. Define Neural Networks(NN), loss function and optimizer
#       3. Train NN model, observe the training error and validate the change of training error
#       |—— 3.1 clean all gradient()        optimizer.zero_grad()
#       |—— 3.2 forward predict             output = model(data)
#       |—— 3.3 calculate loss function     loss = loss_cal(output, target)
#       |—— 3.4 back propagation            loss.backward()
#       |—— 3.5 optimize parameter          optimizer.step()
#       |—— 3.6 calculator mean train error and validation error every turn
#    -> 4. Test the NN model
# MNIST data set Link:  http://yann.lecun.com/exdb/mnist/
# Keyword: PyTorch, MLP, MNIST
# Copyright 2020 Suqier


from mnist import *


if __name__ == '__main__':
    model = Net()
    model.load_state_dict(torch.load('model.pt'))

    test_loss = 0.0

    model.eval()

    for data, target in test_loader:
        output = model(data)
        loss = loss_cal(output, target)
        test_loss += loss.item() * data.size(0)
        _, pred = torch.max(output, 1)
        correct = np.squeeze(pred.eq(target.data.view_as(pred)))

    test_loss /= len(test_loader.dataset)
    print('Test correct rate for this model: {:.2f} %'.format((1 - test_loss) * 100))


