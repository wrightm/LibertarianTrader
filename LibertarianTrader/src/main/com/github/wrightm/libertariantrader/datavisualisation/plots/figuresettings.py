'''
Figure settings that are used for setting plot images.
        
@author: wrightm
'''

#!/usr/bin/env python

#=====================================
# imports
#=====================================

#=====================================
# python system
#=====================================
import copy

class FigureSettings(object):
    '''
    Figure settings to be used with plots
    '''
    def __init__(self, settings = None):
        '''
            initialise settings dictionary or deep copy existing tickers
            @param settings: dictionary of settings
        '''
        self.__settings = copy.deepcopy(settings) if settings else {}
    
    def __len__(self):
        return len(self.__settings)
    
    def __getitem__(self, key):
        return self.__settings[key]
    
    def __setitem__(self, key, value):
        self.__settings[key] = value
    
    def __delitem__(self, key):
        del self.__settings[key]
    
    def iteritems(self):
        return self.__settings.iteritems()
    
    def get(self, setting, default=None):
        '''
            Return setting value
            @param setting: setting key
            @param default: if setting does not exist return default 
        '''
        return self.__settings.get(setting, default)
    
    def remove(self, setting):
        '''
           Remove setting from dictionary.
           @param setting: key to be removed from dictionary settings 
        '''
        value = self.__settings[setting]
        del self.__settings[setting]
        return value
    
    def getSettings(self):
        '''
            Return dictionary of settings 
        '''
        return copy.deepcopy(self.__settings)