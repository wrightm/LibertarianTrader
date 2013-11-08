'''
Created on 15 Oct 2013

@author: wrightm
'''
import math

class Stats(object):
    '''
        Statistical methods for inferring from data
    '''

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
            
        dev2 = [ math.pow((item-mu),2) for item in items ]
        
        return Stats.mean(dev2)
        
    @staticmethod
    def stdev(items, mu=None):
        return math.sqrt(Stats.var(items, mu))
    
