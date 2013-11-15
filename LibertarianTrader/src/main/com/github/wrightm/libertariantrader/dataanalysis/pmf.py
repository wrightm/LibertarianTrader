'''
Probability Mass Function

@author: wrightm
'''
from src.main.com.github.wrightm.libertariantrader.dataanalysis.samplefrequencies import SampleFrequencies
import math
import decimal
import copy

class Pmf(object):
    '''
    Probability Mass Function
    '''
    
    def __init__(self, frequencies, normFactor=1.0, logTransform=False, expoTransform=False):
        '''
            initialise SampleFrequencies, normalisation factor and Pmf directory
            
            Parameters:
            -----------
            @param frequencies: dictionary 
            items and there frequencies
            @param normFactor: float
            factor to multiple the probability for each item
            @param logTransform: boolean
            transform pmf to logarithm
            @param expoTransform: boolean
            transform pmf to exponetial 
            
            Exceptions:
            -----------
            @raise TypeError: when frequencies is not of type SampleFrequencies
        '''
        if not isinstance(frequencies, SampleFrequencies):
            raise TypeError('frequencies param is not of type SampleFrequencies')
        
        self.__frequencies = frequencies.copy()
        self.__factor = normFactor
        self.__logTransform = logTransform
        self.__expoTransform = expoTransform
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
        maxValue = max(self.__frequencies.getFrequencies())
        for item, frequency in self.__frequencies.iterPairs():
            
            if self.__logTransform:
                self.__pmf[item] = math.log((frequency * norm) / maxValue)
            elif self.__expoTransform:
                self.__pmf[item] = math.exp((frequency * norm) / maxValue)
            else:
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
    
    def getFrequencies(self):
        """
        Return Frequencies
        """
        return copy.deepcopy(self.__frequencies)
    
    def copy(self):
        """
        Return deep copy of Pmf
        """
        return Pmf(self.__frequencies, self.__factor)
    
class Bias(object):
    '''
    Base class for Biases for a given Pmf
    '''

    def __call__(self, value):
        '''
        Calculate bias for particular value from pmf
        
        @param value: value from pmf
        @return: bias factor for particular pmf value
        '''
        return value
    
    
def biasPmf(pmf, bias,invert=False):
    
    """
        Oversampled pmf will not show the true distribution of the sample.
        An e.x. of this is class sizes:
        
        From the view of the dean we see a true sample of the average class sizes,
        but from the student view this is oversampled as there are more students in the bigger class sizes.
        Hence more students will say there classes are large
    
    Parameters:
    -----------
    @param bias: Bias
    bias to use for biasing pmf
    @param pmf: Pmf
    pmf distribution of sample
    @param invert: boolean
    if false pmf is biased else unbiased
    
    Return:
    -------
    @return: Pmf
    return modified pmf biased or unbiased      
    """
    if not issubclass(bias, Bias) and not isinstance(bias, Bias):
        raise TypeError('bias is not type or sub type of Bias')

    newFrequencies = {}    
    for value, freq in pmf.getFrequencies().iterPairs():
        if invert:
            if value:
                newFrequencies[value] = float(freq) * float(1.0/bias(value)())
        else:
            newFrequencies[value] = freq * bias(value)()
    return Pmf(SampleFrequencies(newFrequencies))

def unBiasPmf(pmf, bias):
    """
    Return unbiased pmf, should be the same as original
        
    Parameters:
    -----------
    @param pmf: Pmf
    pmf distribution of sample
    
    Return:
    -------
    @return: Pmf
    return modified unbiased pmf
    """
    return biasPmf(pmf, bias, invert=True)
    
    
    