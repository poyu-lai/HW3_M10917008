import os
import numpy as np
import csv

class Abalone:
    def __init__(self):
        self.ab_type = [i+1 for i in range(29)] #29 class
        self.ab_typenum = [0 for i in range(29)] #29 class
        self.ab_type_record = []
        self.ab_conarray = []   #cluster train use
        self.ab_conarray_class = [[] for i in range(29)] #cluster predict use
        self.ab_conarray_class_flatten = []

    def loadAbCSV(self, filepath):
        with open(filepath, 'r') as csvfile:
            rows = csv.reader(csvfile)
            self.ab_conarray = []
            for row in rows:
                self.ab_type_record.append(int(row[8]))
                self.ab_typenum[int(row[8])-1]+=1
                self.ab_conarray.append(np.array(row[:8], dtype=float))
                self.ab_conarray_class[int(row[8])-1].append(np.array(row[:8], dtype=float))

        for conarray in self.ab_conarray_class:
            self.ab_conarray_class_flatten.append(conarray)
        self.ab_conarray_class_flatten = np.array(self.ab_conarray)