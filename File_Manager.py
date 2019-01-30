import numpy as np
import pandas
import os.path

# Data handler class for reading input files
class Data():
    def __init__(self):
        self.read_training_data()
        self.read_testing_data()
        self.read_tool_tr_data()
        self.read_tool_test_data()
        # Custom targets consisting of 1 and -1 for training specific neurons
        self.rosa_targ = self.clean_rosa()
        self.canadian_targ = self.clean_canadian()

    def clean_rosa(self):
        list_ = []
        for i in range(len(self.targets_or)):
            if self.targets_or[i] != 2:
                list_.append(-1)
            else:
                list_.append(1)
        return list_

    def clean_canadian(self):
        list_ = []
        for i in range(len(self.targets_or)):
            if self.targets_or[i] != 3:
                list_.append(-1)
            else:
                list_.append(1)
        return list_


    def read_training_data(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "Data", "trainSeeds.csv")
        colnames = ['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry coefficient', 'length of kernel groove', 'class']
        data = pandas.read_csv(path, names=colnames)
        self.tr_data = data.drop(columns='class')
        self.tr_data.insert(0, 'bias', 1)
        self.tr_data = self.tr_data.values
        self.targets_or = data['class'].tolist()

    def read_testing_data(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "Data", "testSeeds.csv")
        colnames = ['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry coefficient', 'length of kernel groove', 'class']
        data = pandas.read_csv(path, names=colnames)
        self.test_data = data.drop(columns='class')
        self.test_data.insert(0, 'bias', 1)
        self.test_data = self.test_data.values
        self.test_targets = data['class'].tolist()

    def read_tool_tr_data(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "Data", "trainSeeds.csv")
        colnames = ['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry coefficient', 'length of kernel groove', 'class']
        data = pandas.read_csv(path, names=colnames)
        self.tool_tr_data = data.drop(columns='class')
        self.tool_tr_targets = data['class'].tolist()

    def read_tool_test_data(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "Data", "testSeeds.csv")
        colnames = ['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry coefficient', 'length of kernel groove', 'class']
        data = pandas.read_csv(path, names=colnames)
        self.tool_test_data = data.drop(columns='class')
        self.tool_test_targets = data['class'].tolist()

# d = Data()
# print(len(d.targets_or))
# print(len(d.kama_targ))
# print("rosa targs", d.rosa_targ)
