import numpy as np
import pandas as pd
from collections import Counter

class NavieBayes(object):

    def __init__(self,data,label):
        self.data = data
        self.label = label
    
    def train(self,testEntry):
        x1Set = set(self.data.iloc[:,0].values)
        x2Set = set(self.data.iloc[:,1].values)
        
        length = len(self.label)
        labelSet = set(self.label)
    
        count = Counter(self.label)
        priorProbability = {}
        conditionProbability = {}
        for label in count.keys():
            prior = count[label] / length
            probability = 1
            for index in range(len(testEntry)-1):
                x = testEntry[index]
                temp1 = [example for example in self.data  if((example[index])==x and (testEntry[-1]==label))]
                temp2 = [example for example in self.data if(testEntry[-1]==label)]
                proba = temp1 / temp2
                probability = probability * proba
            priorProbability[label] = prior
            conditionProbability[label] = probability
        
        result = 0
        maxProbability = 0 
        for label in count.keys():
            totalProbability = 0
            totalProbability = totalProbability + conditionProbability[label]
            probability = conditionProbability[label] * priorProbability[label] / totalProbability

            if(maxProbability < probability):
                result = label
                maxProbability = probability
        
        return result , maxProbability

        


            

        
            