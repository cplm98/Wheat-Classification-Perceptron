import numpy as np
import pandas
import os.path

class Data():
    def __init__(self):
        self.read_training_data()
        self.kama_targ = self.clean_kama()
        self.rosa_targ = self.clean_rosa()
        self.canadian_targ = self.clean_canadian()

    def clean_kama(self):
        list_ = []
        for i in range(len(self.targets_or)):
            if self.targets_or[i] != 1:
                list_.append(-1)
            else:
                list_.append(1)
        return list_

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
        self.data = pandas.read_csv(path, names=colnames)
        self.tr_data = self.data.drop(columns='class')
        self.tr_data.insert(0, 'bias', 1)
        self.tr_data = self.tr_data.values
        self.targets_or = self.data['class'].tolist()
        #self.targets_or = self.targets_or.values
        # area = data.area.tolist()
        # perimeter = data.perimeter.tolist()
        # compactness = data.compactness.tolist()
        # length = data.length.tolist()
        # width = data.width.tolist()
        # asymCoef = data.asymmetryCoefficient.tolist()
        # lenKernelGroove = data.lengthOfKernelGroove.tolist()
        # class_ = data.class_.tolist()
        #return tr_data, targets


# d = Data()
# print(len(d.targets_or))
# print(len(d.kama_targ))
# print("rosa targs", d.rosa_targ)
