import random
from File_Manager import Data

def activation(sum_):  # so the training works its adjusting the weights, but my activation function is not right, so gotta fix that
    if sum_ > 0 and sum_ <= 1:
        return 1
    if sum_ > 1 and sum_ <= 2:
        return 2
    else:
        return 3

class Perceptron:
    def __init__(self,):
        #self.type = type  # this will indicate which activation function it will use
        self.c = .002  # learning rate
        self.weights = []
        for i in range(7):
            self.weights.append(random.uniform(.0001, 1))

    def predict(self, inpt):
        sum_ = 0
        for i, val in enumerate(inpt):  # take one array of 6 inputs at a time
            sum_ = sum_ + val*self.weights[i]
        print("sum: ", sum_)

        output = activation(sum_)  # have to define the activation function still
        return output

    def train(self, tr_data, target):
        guess = self.predict(tr_data)
        print("guess:", guess)
        print("target:", target)
        err = target - guess
        print("error: ", err)
        for i, weight in enumerate(self.weights):
            weight = weight + (err*tr_data[i] * self.c)
            self.weights[i] = weight
        print(self.weights)

d = Data()
p = Perceptron()
print(p.weights)
inpt = [15.26,14.84,0.871,5.763,3.312,2.221,5.22]
print(p.predict(inpt))
for j in range(1):
    for i, row in enumerate(d.data):
        p.train(row, d.targets_or[i])
