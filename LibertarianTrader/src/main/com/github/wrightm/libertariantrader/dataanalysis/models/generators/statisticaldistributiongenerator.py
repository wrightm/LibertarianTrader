'''
Created on 17 Nov 2013

@author: wrightm
'''

import numpy as np
from abc import ABCMeta, abstractmethod
from src.main.com.github.wrightm.libertariantrader.dataanalysis.statistics import Stats
import math
import scipy.special

class __Distribution(object):
    '''
    Abstract Base Distribution class for all distributions
    '''
    __metaclass__ = ABCMeta

    def __init__(self, mean, variance, mininum=0.0, maximum=0.0, steps=0):
        '''
        Initialise class and generate sample
        
        Parameters:
        -----------
        
        @param mean: float
        mean value of the distribution
        @param variance: float 
        variance of the distribution 
        @param mininum: float
        minimum value to generate distribution from
        @param maximum: float
        maximum value to generate distribution to
        @param steps: int
        number of distribution points to generate from minimum to maximum
        '''
        self.min = mininum
        self.max = max
        self.steps = steps
        self.sample = np.linspace(mininum, maximum, steps)
        self.mean = mean
        self.variance = variance
        self.pdfSample = {}
        self.cdfSample = {}
        
    @abstractmethod
    def pdfFunction(self, value):
        raise NotImplementedError()
    
    @abstractmethod
    def generatePDFSample(self):
        raise NotImplementedError()
    
    @abstractmethod
    def cdfFunction(self, value):
        raise NotImplementedError()
    
    @abstractmethod
    def generateCDFSample(self):
        raise NotImplementedError()
    
    def getMean(self):
        """
        Return mean of distribution
        """
        return self.mean
    
    def getVariance(self):
        """
        Return variance of distribution
        """
        return self.__variance
    
    def getSample(self):
        """
        Return sample points
        """
        return self.sample
    
    def getPDFValue(self, value):
        """
        For a given value return the distributions pdf value
        
        Parameters:
        -----------
        
        @param value: float
        
        Return:
        @return: pdf for given value
        """
        pdfValue = self.pdfSample.get(value, None)
        if pdfValue != None:
            return pdfValue
        
        pdfValue = self.__pdfFunction(value)
        self.pdfSample[value] = pdfValue
        return pdfValue
            
    
    def getPDF(self):
        """
        Return the distributions pdf value
        
        Return:
        @return: list of tuples (value, pdf) 
        All values and pdf values 
        """
        return self.pdfSample
    
    def getCDFValue(self, value):
        """
        For a given value return the distributions cdf value
        
        Parameters:
        -----------
        
        @param value: float
        
        Return:
        @return: cdf for given value
        """
        cdfValue = self.cdfSample.get(value, None)
        if cdfValue != None:
            return cdfValue
        
        cdfValue = self.cdfFunction(value)
        self.cdfSample[value] = cdfValue
        return cdfValue
    
    def getCDF(self):
        """
        Return the distributions cdf value
        
        Parameters:
        -----------
        
        @param value: float
        
        Return:
        @return: list of tuples (value, cdf) 
        All (values, cdf values) 
        """
        return self.cdfSample
    
class Guassian(__Distribution):
    """
    Guassian Distribution
    """
    
    def __init__(self,  mean, variance, mininum=0.0, maximum=0.0, steps=0):
        super(Guassian, self).__init__(mean, variance, mininum, maximum, steps)
        
        self.pdfSample = self.generatePDFSample()
        self.cdfSample = self.generateCDFSample()
    
    def pdfFunction(self, value):
        
        stdev = math.sqrt(self.variance)
        scoreSquared = math.pow(Stats.score(value, self.mean, stdev), 2)
        sqrt2pi = math.sqrt(2*math.pi)
        
        return (1.0 / (stdev * sqrt2pi)) * math.exp( (-0.5) * scoreSquared)
    
    def generatePDFSample(self):
        
        pdfSample = {}
        for item in self.sample:
            pdfSample[item] = self.pdfFunction(item)

        return pdfSample
        
    def cdfFunction(self, value):
        
        stdev = math.sqrt(self.variance)
        score = Stats.score(value, self.mean, stdev)
        
        return 0.5 * (1 + scipy.special.erf( score * math.sqrt(2) ))
    
    def generateCDFSample(self):
        
        cdfSample = {}
        for item in self.sample:
            cdfSample[item] = self.cdfFunction(item)

        return cdfSample
    