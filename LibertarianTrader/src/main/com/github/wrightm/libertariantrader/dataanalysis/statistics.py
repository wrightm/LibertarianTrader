'''
Created on 15 Oct 2013

@author: wrightm
'''
import math

class Stats(object):
    '''
        Statistical methods for inferring from data
    '''
    
    descriptive = True

    @staticmethod
    def mean(items):
        
        if not isinstance(items, list):
            raise TypeError('items is not of type list')
        
        return float(sum(items)) / len(items)
    
    @staticmethod
    def var(items, mu=None):
        
        if not isinstance(items, list):
            raise TypeError('items is not of type list')
        
        if mu == None:
            mu = Stats.mean(items)
            
        dev2 = map(lambda item: math.pow((item-mu),2), items )

        if Stats.descriptive:
            return Stats.mean(dev2)
        else:
            return float(sum(items)) / (len(items) -1)
        
    @staticmethod
    def stdev(items, mu=None):
        
        return math.sqrt(Stats.var(items, mu))
    
    @staticmethod
    def zscores(items, mu=None):
        
        if mu == None:
            mu = Stats.mean(items)
        
        stdev = Stats.stdev(items, mu)
        
        return [ float(item - mu) / float(stdev) for item in items ]
    
    @staticmethod
    def trimmed(items, percentage=0.01, sortLambda=None):
        
        if sortLambda != None:
            items.sort(key=sortLambda)
        n = int(round(percentage * len(items)))
        
        if n == 0:
            return items
        else:
            return items[n:-n]
    
    @staticmethod
    def mad(items, mu=None):
        
        if mu == None:
            mu = Stats.mean(items)
        
        return sum(map(lambda item: math.fabs(item - mu), items)) / len(items)

    @staticmethod
    def min(items):
        
        return min(items)

    @staticmethod
    def max(items):
        
        return max(items)
    
    @staticmethod
    def range(items):
        
        return max(items) - min(items)
    
    @staticmethod
    def __moment(items, mu=None, power=3):

        if mu == None:
            mu = Stats.mean(items)
            
        return sum(map(lambda item: math.pow(item - mu, power), items)) / ((len(items) - 1) * math.pow(Stats.stdev(items, mu), power)) 
    
    @staticmethod
    def kurtosis(items, mu=None):
        
        return Stats.__moment(items, mu, 4) - 3
    
    @staticmethod
    def skewness(items, mu=None):
        
        return Stats.__moment(items, mu, 4)
    
    @staticmethod
    def standardError(items, mu=None):
        
        return Stats.stdev(items, mu) / math.sqrt(len(items))
    