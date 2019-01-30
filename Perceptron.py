import random
from File_Manager import Data
from sklearn.linear_model import Perceptron
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np


def test2(p_rosa, p_can, inpt):
    result = []
    result.append(p_rosa.predict(inpt))
    result.append(p_can.predict(inpt))
    return result


def activation(sum_):
    if sum_ >= 0:
        return 1
    if sum_ < 0:
        return -1


class Perception_:
    def __init__(self, ):
        self.c = .0007  # learning rate
        self.weights = []  # list of weights
        self.correct = 0  # counter for counting correct predictions

        for i in range(8):  # fill weights with random values between 0 and 1
            self.weights.append(random.uniform(.0001, 1))

    def predict(self, inpt):  # generates prediction based on current weights
        sum_ = 0
        for i, val in enumerate(inpt):  # take one array of 7 inputs at a time including bias
            sum_ = sum_ + val * self.weights[i]  # sums weights*input values
        output = activation(sum_)  # calculates activation level, either -1 or 1
        return output

    def train(self, tr_data, target):
        guess = self.predict(tr_data)  # generate prediction
        err = target - guess  # calculate error using difference between answer and guess
        if err == 0:  # if error is zero, guess is correct
            self.correct += 1
        for i, weight in enumerate(self.weights):
            weight = weight + (err * tr_data[i] * self.c)  # adjust weights using error
            self.weights[i] = weight


##### ***Implementation*** #####

fileWrite = True

d = Data()
p_rosa = Perception_()
rosa_init_weights = p_rosa.weights
p_can = Perception_()
can_init_weights = p_can.weights
rosa_correct_trials = []
can_correct_trials = []

##### ***Training*** #####

for j in range(1000):  # number of training cycles
    for i, row in enumerate(d.tr_data):
        p_rosa.train(row, d.rosa_targ[i])
    rosa_correct_trials.append((p_rosa.correct / 165) * 100)
    p_rosa.correct = 0
    for i, row in enumerate(d.tr_data):
        p_can.train(row, d.canadian_targ[i])
    can_correct_trials.append((p_can.correct / 165) * 100)
    p_can.correct = 0

print("# of correct rosa classifications: ", rosa_correct_trials)
print("# of correct can classifications: ", can_correct_trials)
print("############### TESTING ############### \n \n")
print("############### Weights ############### \n")

print("rosa: ", p_rosa.weights)
print("can: ", p_can.weights)

##### ***Testing*** #####

ov_corr = 0

res_out = []
res_list = []

for i, row in enumerate(d.test_data):
    res = test2(p_rosa, p_can, row)

    if res == [-1, -1]:
        result = 1
    elif res == [1, -1]:
        result = 2
    elif res == [-1, 1]:
        result = 3
    else:
        result = res
    string_ = "Predicted Class: " + str(result) + ", Original Class: " + str(d.test_targets[i])
    res_out.append(string_)
    res_list.append(result)

    if result == d.test_targets[i]:
        ov_corr += 1

print(res_list)

print("##### ***SKLearn Tool*** #####")

perceptron = Perceptron(max_iter=1000, tol=0.1)
perceptron.fit(d.tool_tr_data, d.tool_tr_targets)
guess = perceptron.predict(d.tool_test_data)
print("Train accuracy: %.2f \n" % perceptron.score(d.tool_tr_data, d.tool_tr_targets))
print("Test accuracy: %.2f \n" % perceptron.score(d.tool_test_data, d.tool_test_targets))

confusion_mat = confusion_matrix(d.tool_test_targets, guess)
print(confusion_mat)
class_report = classification_report(d.tool_test_targets, guess)
print(class_report)

# write to text file
if fileWrite:
    f = open('452NN_A1_output.txt', 'w')
    f.write('\nTest Results\n\n')
    for i in range(len(res_out)):
        f.write(str(res_out[i]) + '\n')
    f.write('Rosa Initial Weights: ' + str(rosa_init_weights) + '\n')
    f.write('Rosa Trained Weights: ' + str(p_rosa.weights) + '\n')
    f.write('Canadian Initial Weights: ' + str(can_init_weights) + '\n')
    f.write('Canadian Trained Weights: ' + str(p_can.weights) + '\n')
    f.write('\nThe total number of training iterations was 1000 \n')
    f.write('An accuracy threshold could have also been used to avoid \'over training\'\n')
    f.write('but the number of correctly classified seeds increased up to 1000 epochs. \n')
    f.write('This justifies iterations over the threshold in this scenario. \n')
    f.write("\n\nSKLearn Tool\n")
    f.write("Training accuracy: %.2f" % perceptron.score(d.tool_tr_data, d.tool_tr_targets))
    f.write("\nTesting accuracy: %.2f" % perceptron.score(d.tool_test_data, d.tool_test_targets))
    f.write("\nConfusion Matrix from SKLearn Tool: \n")
    f.write(np.array2string(confusion_mat))
    f.write("\nPrecision and Recall: \n")
    f.write(class_report)
    f.write('\nThe tool model shows higher accuracy in both it\'s overall prediction\n')
    f.write('and the recall and precision scores. Although the difference is only a couple percent\n')
    f.write('it is still notable.')
    f.close()

print(d.test_targets)
print(res_out)
print("correct: ", ov_corr)
print("out of: ", len(d.test_targets))
