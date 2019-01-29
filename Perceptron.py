import random
from File_Manager import Data


def test(p_kama, p_rosa, p_can, inpt):  # takes in the three trained perceptrons and a set of data
    result = []
    result.append(p_kama.predict(inpt))
    result.append(p_rosa.predict(inpt))
    result.append(p_can.predict(inpt))
    return result


def activation_kama(sum_):
    if sum_ >= 0:
        return 1
    if sum_ < 0:
        return -1


class Perceptron:
    def __init__(self,):
        #self.type = type  # this will indicate which activation function it will use
        self.c = .0001  # learning rate
        self.weights = []
        self.correct = 0
        for i in range(8):
            self.weights.append(random.uniform(.0001, 1))

    def predict(self, inpt):
        sum_ = 0
        for i, val in enumerate(inpt):  # take one array of 6 inputs at a time
            sum_ = sum_ + val*self.weights[i]

        output = activation_kama(sum_)  # have to define the activation function still
        return output

    def train(self, tr_data, target):
        guess = self.predict(tr_data)
        print("guess:", guess)
        print("target:", target)
        err = target - guess
        if err == 0:
            self.correct += 1
        print("error: ", err)
        for i, weight in enumerate(self.weights):
            weight = weight + (err*tr_data[i] * self.c)  # adjust weights using error
            self.weights[i] = weight
        print(self.weights)



d = Data()
p_kama = Perceptron()
print(d.kama_targ)
p_rosa = Perceptron()
p_can = Perceptron()
kama_correct_trials = []
rosa_correct_trials = []
can_correct_trials = []
print("Initial Weights: ", p_kama.weights)

for j in range(100):  # number of training cycles
    for i, row in enumerate(d.tr_data):
        p_kama.train(row, d.kama_targ[i])
    kama_correct_trials.append((p_kama.correct/165)*100)
    p_kama.correct = 0
    for i, row in enumerate(d.tr_data):
        p_rosa.train(row, d.rosa_targ[i])
    rosa_correct_trials.append((p_rosa.correct/165)*100)
    p_rosa.correct = 0
    for i, row in enumerate(d.tr_data):
        p_can.train(row, d.canadian_targ[i])
    can_correct_trials.append((p_can.correct/165)*100)
    p_can.correct = 0
print("# of correct kama classifications: ", kama_correct_trials)
print("# of correct rosa classifications: ", rosa_correct_trials)
print("# of correct can classifications: ", can_correct_trials)
print("############### TESTING ############### \n \n")
print("############### Weights ############### \n")
print("kama: ", p_kama.weights)
print("rosa: ", p_rosa.weights)
print("can: ", p_can.weights)

print("############### Brainstorming ############### \n")
# print("solo predict: ", (p_rosa.predict([1,15.26,14.84,0.871,5.763,3.312,2.221,5.22])))
corr = 0
ov_corr = 0
for i, row in enumerate(d.tr_data):
    # pred = p_rosa.predict(row)
    # ans = d.rosa_targ[i]
    # print("prediction: ", pred)
    # print("answer: ", ans)
    # if pred == ans:
    #     corr += 1
#     # print("data in", row)
    res = test(p_kama, p_rosa, p_can, row)
    if res == [-1, -1, -1]:
        result = 0
        print(result)
    elif res == [1, -1, -1]:
        result = 1
        print(1)
    elif res == [-1, 1, -1]:
        result = 2
        print(result)
    elif res == [-1, -1, 1]:
        result = 3
        print(result)
    else:
        print(res)

    if result == d.targets_or[i]:
        ov_corr += 1

print("correct: ", ov_corr)


