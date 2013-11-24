'''
Created on 15 Oct 2013

@author: wrightm
'''
from src.main.com.github.wrightm.libertariantrader.utils.helpers import Helpers
from src.main.com.github.wrightm.libertariantrader.utils.dataprocessing import DataProcessing

class Stats(object):
    '''
        Statistical methods for inferring from data
    '''
    
    descriptive = True

    @staticmethod
    def mean(items):
        
        if not hasattr(items, '__iter__'):
            raise TypeError('items is not an iterable type')

        return Helpers.sumWrapper(items) / float(len(items))
    
    @staticmethod
    def var(items, mu=None):
        
        if not hasattr(items, '__iter__'):
            raise TypeError('items is not an iterable type')
        
        if mu == None:
            mu = Stats.mean(items)
        dev2 = map(lambda item: (item-mu)**2, items )

        if Stats.descriptive:
            return Stats.mean(dev2)
        else:
            return sum(items) / float(len(items) -1)
        
    @staticmethod
    def stdev(items, mu=None):
        
        return (Stats.var(items, mu))**(0.5)
    
    @staticmethod
    def score(value, mean, stdev):        
        return (value - mean) / stdev
        
    @staticmethod
    def zscores(items, mu=None):
        
        if mu == None:
            mu = Stats.mean(items)
        stdev = Stats.stdev(items, mu)
        
        return [ Stats.score(item,mu,stdev) for item in items ]
    
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
        
        return Helpers.sumWrapper(map(lambda item: abs(item - mu), items)) / float(len(items))

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
        
        return Helpers.sumWrapper(map(lambda item: ((item - mu)**power), items)) / ((Stats.stdev(items, mu)**power) * (len(items) - 1)) 
    
    @staticmethod
    def kurtosis(items, mu=None):
        
        return Stats.__moment(items, mu, 4) - 3
    
    @staticmethod
    def skewness(items, mu=None):
        
        return Stats.__moment(items, mu, 4)
    
    @staticmethod
    def standardError(items, mu=None):
        
        return Stats.stdev(items, mu) / (len(items)**(0.5))
    
    @staticmethod
    def covariance(firstValue, firstValueMean, secondValue, secondValueMean, sampleSize):
            return (firstValue - firstValueMean) * (secondValue - secondValueMean) / float(sampleSize)
        
    @staticmethod
    def covarianceFromSets(firstSet, secondSet, firstmu=None, secondmu=None):
        
        firstSet, secondSet = DataProcessing.checkSetsAreEqualInLength(firstSet, secondSet)
        sampleSize = len(firstSet)
        
        if firstmu == None:
            firstmu = Stats.mean(firstSet)
            
        if secondmu == None:
            secondmu = Stats.mean(secondSet)
            
        cov = Stats.covariance(firstSet[0], firstmu, secondSet[0], secondmu, sampleSize)
        firstSet = firstSet[1:]
        secondSet = secondSet[1:]
        for firstValue, secondValue in zip(firstSet, secondSet):
            cov += Stats.covariance(firstValue, firstmu, secondValue, secondmu, sampleSize)
    
        return cov
    
    @staticmethod
    def correlation(firstValue, firstValueMean, firstStdev, secondValue, secondValueMean, secondStdev, sampleSize):
        
        cov = Stats.covariance(firstValue, firstValueMean, secondValue, secondValueMean, sampleSize)
        return cov / (firstStdev * secondStdev)
    
    @staticmethod
    def correlationFromSets(firstSet, secondSet, firstmu=None, firstStdev=None, secondmu=None, secondStdev=None):

        firstSet, secondSet = DataProcessing.checkSetsAreEqualInLength(firstSet, secondSet)
        
        if firstmu == None:
            firstmu = Stats.mean(firstSet)
            
        if secondmu == None:
            secondmu = Stats.mean(secondSet)
            
        if firstStdev == None:
            firstStdev = Stats.stdev(firstSet, firstmu)
            
        if secondStdev == None:
            secondStdev = Stats.stdev(secondSet, secondmu)
        
        return Stats.covarianceFromSets(firstSet, secondSet, firstmu, secondmu) / (firstStdev * secondStdev)
        