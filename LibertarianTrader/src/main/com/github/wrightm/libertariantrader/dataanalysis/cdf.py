'''
Created on 28 Oct 2013

@author: wrightm
'''
import bisect
import math
import random

class CDF(object):
    '''
    Cumulative Density Function
    '''
    
    def __init__(self, sample):
        '''
            Produce cdf from sample
            
            Parameters:
            ----------
            @param sample: sample to be used to construct cdf
            
            Exceptions:
            -----------
            @raise AttributeError: if sample does not have getPairs attribute
        '''
        
        if not hasattr(sample, 'getPairs'):
            raise AttributeError('sample does not have getPairs attribute')

        self.__sample = sample
        self.__init()
        
        
    def __init(self):
        """
        Initialise cdf from sample
        """
        runningSum = 0
        self.__xs = []
        self.__cs = []
        for key, value in self.__sample.getPairs():
            runningSum += value
            self.__xs.append(key)
            self.__cs.append(runningSum)
        
        total = float(runningSum)
        self.__ps = map(lambda value: value/total, self.__cs)
        
    def getValue(self, prob):
        """
        Return value for a given probability
            
        Parameters:
        -----------
        @param prob: probability used to retrieve associated value

        Return:
        -------
        @return: value for a given probability
        """
        if prob <= 0.0:
            return self.__xs[0]
        if prob >= 1.0:
            return self.__xs[-1]
        
        index = bisect.bisect(self.__ps, prob)
        if prob == self.__ps[index-1]:
            return self.__xs[index-1]
        else:
            return self.__xs[index]
        
    def getProbability(self, value):
        """
        Return probability for a given value
            
        Parameters:
        -----------
        @param value: value used to retrieve associated probability

        Return:
        -------
        @return: probability for a given value   
        """
        index = bisect.bisect(self.__xs, value)
        if index == 0:
            return self.__ps[index]
        else:
            return self.__ps[index-1]
        
    def getMean(self):
        """
        Return Mean of CDF
        
        Return:
        -------
        @return: mean probability
        """
        oldProb = 0.0
        mu = 0.0
        for value, prob in zip(self.__xs, self.__ps):
            newProb = prob - oldProb
            mu += newProb*value
            oldProb = newProb
        return mu
    
    def getVar(self, mu=None):
        """
        Return variance of CDF
       
        Parameters:
        -----------
        @param mu: mean of CDF
        
        Return:
        -------
        @return: variance of probability
        """
        if mu == None:
            mu = self.getMean()
            
        oldProb = 0.0
        var = 0.0
        for value, prob in zip(self.__xs, self.__ps):
            newProb = prob - oldProb
            var += newProb * pow((value-mu),2)
            
        return var
    
    def getStdDev(self, mu=None):
        """
        Return standard deviation of CDF
       
        Parameters:
        -----------
        @param mu: mean of CDF
        
        Return:
        -------
        @return: stdev of probability
        """
        return math.sqrt(self.getVar(mu))
    
    def getSample(self, sampleSize):
        """
        Return sample of CDF distribution (re-sampling)
        
        Parameters:
        -----------
        @param sampleSize: size of sample to generate
        
        Return:
        -------
        @return: list
        sample of n=sampleSize random cdf values
        """
        return [ self.getRandomValue() for indx in range(sampleSize) ]
        
    def getRandomValue(self):
        """
        Return random value from CDF
        """
        return self.getValue(random.random())
    
    def getPercentile(self, percentile):
        """
        Return Percentile value for CDF
        
        Parameters:
        -----------
        @param percentile: int ranging from 1 to 100
        
        Return:
        -------
        @return: value for given percentile
        
        Exceptions:
        ----------
        @raise ValueError: if percentile is not within [1,100]
        """
        if percentile < 1 or percentile > 100:
            raise ValueError('percentile is not within the range [1,100]')
        
        return self.getValue(float(percentile) / 100.00)
    
    def getPairs(self):
        """
        Return list of (value, probabilities)
        """
        return zip(self.__xs, self.__ps)