'''
Records the frequency of a object within a group
@author: wrightm
'''
import copy

class SampleFrequencies(object):
    '''
        Records the frequency of a object within a group
    '''

    def __init__(self, frequencies=None):
        '''
            Initialise frequency dictionary if frequencies is None. Otherwise deepcopy dictionary
        
            @param frequencies: dictionary of value, frequencies
        '''
        if frequencies:
            self.__frequencies = copy.deepcopy(frequencies)
        else:
            self.__frequencies = {}
    
    def __eq__(self, other):
            if self.__frequencies == other.__frequencies:
                return True
            else:
                return False
                
    def set(self, item):
        '''
            set item. Increments the number of occurrences of the item
            
            @param item: object to keep count of
        '''
        
        self.__frequencies[item] = self.__frequencies.get(item, 0) + 1
        
    def get(self, item):
        '''
            get frequency of item
            
            @param item: object to get frequency of
            @return: frequency of item 
        '''
        return self.__frequencies.get(item,0)
    
    def getItems(self):
        '''
            Returns all items
            
            @return: list of items 
        '''
        return self.__frequencies.keys()
    
    def getFrequencies(self):
        '''
            Return all frequencies
            
            @return: list of frequencies
        '''
        return self.__frequencies.values()
    
    def getPairs(self):
        '''
            Return tuple list of (item, frequency) pairs
            
            @return: tuple list of (item, frequency) pairs
        '''
        return self.__frequencies.items()
    
    def iterPairs(self):
        '''
            Return iterator of key, value
            
            @return key, value iter
        '''
        return self.__frequencies.iteritems()
    
    def iterItems(self):
        '''
            Return iterator of key
            
            @return key iter
        '''
        return self.__frequencies.iterkeys()
    
    def iterFrquencies(self):
        '''
            Return iterator of value
            
            @return value iter
        '''
        return self.__frequencies.itervalues()
    
    def copy(self):
        '''
            Return deepcopy of Frequency
            
            @return new deep copied Frequencies object
        '''
        return SampleFrequencies(self.__frequencies)
    
    def hasKey(self, item):
        '''
            Check whether item exists in frequencies
            @return True if item exists, otherwise false
        '''
        return self.__frequencies.has_key(item)
    
    def pop(self, item=None):
        '''
            Remove item and frequency. 
            @param item: item to remove
            @return frequency if only item is given or return (item, frequency) if item and frequency is given
            @raise KeyError: if item does not exist.  
        '''
        if not item:
            return self.__frequencies.popitem()
        else:
            return self.__frequencies.pop(item)