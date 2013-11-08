'''
Probability Mass Function

@author: wrightm
'''
from src.main.com.github.wrightm.libertariantrader.dataanalysis.samplefrequencies import SampleFrequencies
import math
import decimal

class Pmf(object):
    '''
    Probability Mass Function
    '''
    
    def __init__(self, frequencies, normFactor=1.0):
        '''
            initialise SampleFrequencies, normalisation factor and Pmf directory
            @param frequencies: dictionary of items and there frequencies
            @param normFactor: factor to multiple the probability for each item
            @raise TypeError: when frequencies is not of type SampleFrequencies
        '''
        if not isinstance(frequencies, SampleFrequencies):
            raise TypeError('frequencies param is not of type SampleFrequencies')
        
        self.__frequencies = frequencies
        self.__factor = normFactor
        self.__pmf = {}
        self.__normalise()
        self.__mu = None
        self.__variance = None
        self.__stdev = None
        
    def __total(self):
        return sum(self.__frequencies.getFrequencies())
    
    def __normalise(self):
        '''
            normalise frequencies to produce probabilities 
        '''
        norm = self.__factor / self.__total()
        for item, frequency in self.__frequencies.iterPairs():
            self.__pmf[item] = frequency * norm
    
    def get(self, item):
        '''
            Return probability of item
            @param item: object to retrieve probability 
        '''
        return self.__pmf.get(item, 0)
    
    def getItems(self):
        '''
            Return list of items
        '''
        return self.__pmf.keys()
    
    def getProbabilities(self):
        '''
            Return list of probabilities
        '''
        return self.__pmf.values()
    
    def getPairs(self):
        '''
            Return tuple list of (items, probs)
        '''
        return self.__pmf.items()
    
    def iterPairs(self):
        '''
            Return item, probability iter
        '''
        return self.__pmf.iteritems()
    
    def iterItems(self):
        '''
            Return items iter
        '''
        return self.__pmf.iterkeys()
    
    def iterProbabilities(self):
        '''
            Return probabilities iter
        '''
        return self.__pmf.itervalues()
    
    def getMean(self):
        '''
            calculate and return mean of pmf
            @param pmf: probability mass function of type Pmf
            @return: mean of Pmf
        '''
        if self.__mu != None:
            return self.__mu
        
        self.__mu = 0.0
        for item, prob in self.iterPairs():
            self.__mu += item*prob
        return self.__mu
    
    def getVariance(self):
        '''
            calculate and return variance of pmf
            @param pmf: probability mass function of type Pmf
            @return: variance of Pmf
        '''
        if self.__variance != None:
            return self.__variance
        
        if self.__mu == None:
            self.__mu = self.getMean()
        
        self.__variance = 0.0
        for item, prob in self.getPairs():
            self.__variance += prob * pow((item - self.__mu), 2)
        return self.__variance

    def getStDev(self):
        '''
            calculate and return stdev of pmf
            @param pmf: probability mass function of type Pmf
            @return: stdev of Pmf
        '''
        if self.__stdev != None:
            return self.__stdev
        
        if self.__mu == None:
            self.__mu = self.getMean()
        
        self.__stdev = math.sqrt(self.getVariance())
        return self.__stdev
    
    def getPercentileRank(self, value):
        """
        Return the percentile rank for a given value
            
        Parameters:
        -----------
        @param value: variable value to find percentile of
            
        Return:
        -------
        @return: percentile for value
        """
        count = 0
        keys = self.__pmf.keys()
        for key in keys:
            if key <= value:
                count +=1
                
        return long( 100 * (decimal.Decimal(count) / decimal.Decimal(len(keys))) )
    
    def getPercentile(self, percentile):
        """
        Return value for a given percentile
        
        Parameters:
        ----------
        @param percentile: 
        
        Return:
        -------
        @return: return value for given percentile
        
        Exception:
        ----------
        @raise ValueError: when percentile is outside range 0-100
        """
        
        if percentile < 0 or percentile > 100:
            raise ValueError('percentile is not with 0-100 range')
        
        keys = sorted(self.__pmf.keys())
        index = long( percentile * (decimal.Decimal(len(keys)-1)/ 100))
        return keys[index]
    
 
    
    
    