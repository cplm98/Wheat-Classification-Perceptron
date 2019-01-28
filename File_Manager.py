import numpy as np
import pandas
import os.path

class Data():
    def __init__(self):
        self.read_training_data()
        self.clean_kama()  # adjusts data to only have to classifications, kama or not
        self.clean_rosa()
        self.clean_canadian()



    def clean_kama(self):
        print(self.targets_or)
        self.kama_targ = self.targets_or
        for i in range(len(self.kama_targ)):
            if self.kama_targ[i] != 1:
                self.kama_targ[i] = 0

    def clean_rosa(self):
        self.rosa_targ = self.targets_or
        for i in range(len(self.rosa_targ)):
            if self.rosa_targ[i] != 1:
                self.rosa_targ[i] = 0

    def clean_canadian(self):
        self.canadian_targ = self.targets_or
        for i in range(len(self.canadian_targ)):
            if self.canadian_targ[i] != 1:
                self.canadian_targ[i] = 0


    def read_training_data(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "Data", "trainSeeds.csv")
        colnames = ['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry coefficient', 'length of kernel groove', 'class']
        self.data = pandas.read_csv(path, names=colnames)
        self.tr_data = self.data.drop(columns='class')
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
# print(d.kama_targ)
