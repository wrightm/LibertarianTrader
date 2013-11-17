'''
Created on 17 Nov 2013

@author: wrightm
'''

import numpy as np
from abc import ABCMeta, abstractmethod

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
        self.__min = mininum
        self.__max = max
        self.__steps = steps
        self.__sample = np.linspace(mininum, maximum, steps)
        self.__mean = mean
        self.__variance = variance
        
    def getMean(self):
        """
        Return mean of distribution
        """
        return self.__mean
    
    def getVariance(self):
        """
        Return variance of distribution
        """
        return self.__variance
    
    def getSample(self):
        """
        Return sample points
        """
        return self.__sample
    
    @abstractmethod
    def getPDFValue(self, value):
        """
        For a given value return the distributions pdf value
        
        Parameters:
        -----------
        
        @param value: float
        
        Return:
        @return: pdf for given value
        """
        raise NotImplementedError("getPDFValue is an abstract method and should only be used by derived classes")
    
    @abstractmethod
    def getPDF(self):
        """
        Return the distributions pdf value
        
        Return:
        @return: list of tuples (value, pdf) 
        All values and pdf values 
        """
        raise NotImplementedError("getPDF is an abstract method and should only be used by derived classes")
    
    @abstractmethod
    def getCDFValue(self, value):
        """
        For a given value return the distributions cdf value
        
        Parameters:
        -----------
        
        @param value: float
        
        Return:
        @return: cdf for given value
        """
        raise NotImplementedError("getCDFValue is an abstract method and should only be used by derived classes")
    
    @abstractmethod
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
        raise NotImplementedError("getCDF is an abstract method and should only be used by derived classes")
    
    