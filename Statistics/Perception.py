import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# class Perception(object):

#     def __init__(self,eta = 0.01, n_iter=10):
#         self.eta = eta
#         self.n_iter = n_iter
    
#     def fit(self,X,y):
#         self.w_ = np.zeros( 1 + X.shape[1])
#         self.errors_ = []

#         for _ in range(self.n_iter):
#             errors = 0
#             for xi, target in zip(X,y):
#                 update = self.eta * (target - self.predict(xi))
#                 self.w_[1:] += update * xi
#                 self.w_[0] +=update
#                 errors += int(update != 0.0)
#             self.errors_.append(errors)
#         return self
    
#     def net_input(self,X):
#         return np.dot(X,self.w_[1:]) + self.w_[0]

#     def predict(self,X):
#         return np.where(self.net_input(X) >= 0.0,1,-1)


class Perception(object):

    def sigmod(v):
        if ( v > 0):
            return 1
        else:
            return -1

    def __init__(self, x, y, eta = 0.01, iter = 10):
        self.x = x
        self.y = y
        self.b = 0
        self.eta = eta
        self.iter = iter
        self.w = np.zeros(x.shape[1])
    
      

    def run(self):
        length = self.x.shape[0];

        while( error!=0):
            error = length
            randomSample = random.randint(0,length)
            self.w = self.w + self.eta * self.x[randomSample] * self.y[randomSample]
            self.b = self.b + self.eta * self.y[randomSample]

            for index in range(0,length):
                sample = x[index]
                result = self.sigmod(np.dot(sample,self.w) + self.b)
                if(result == self.y[index]):
                    error = error - 1 
                



    
