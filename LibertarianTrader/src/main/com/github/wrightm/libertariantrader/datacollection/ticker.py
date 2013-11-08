'''
Stock market ticker:
        Holds name, date, open price, highest price, lowest price, close price, volume and adjusted close price
@author: wrightm
'''
import datetime

#!/usr/bin/env python

class Ticker(object):
    '''
    Stock market ticker:
        Holds name, date, open price, highest price, lowest price, close price, volume and adjusted close price
    '''


    def __init__(self, name, date, start, high, low, close, volume, adjustedClose):
        '''
        Initialise ticker data
        
        @param name: ticker code
        @param date: date of trading day of ticker
        @param start: price of ticker at start of day
        @param high: highest price of ticker during the trading day
        @param low: lowest price of ticker during the trading day
        @param close: closing price of ticker
        @param volume: number of shares or contracts traded
        @param adjustedClose: adjusted closing price of ticker
        '''
        self.__name = name
        self.__date = datetime.datetime.strptime(date,'%Y-%m-%d')
        self.__open = float(start)
        self.__high = float(high)
        self.__low = float(low)
        self.__close = float(close)
        self.__volume = long(volume)
        self.__adjustedClose = float(adjustedClose)
    
    def __eq__(self, other):
        return (self.__name, self.__date, self.__open, self.__high, self.__low, self.__close, self.__volume, self.__adjustedClose) == \
            (other.__name, other.__date, other.__open, other.__high, other.__low, other.__close, other.__volume, other.__adjustedClose)
    
    def __hash__(self):
        return hash((self.__name, self.__date, self.__open, self.__high, self.__low, self.__close, self.__volume, self.__adjustedClose))
                
    def __str__(self):
        return "name: %s - date: %s - open: %s - high: %s - low: %s - close: %s - volume: %s - adjustedClose: %s" % (self.__name, self.__date, self.__open, self.__high, self.__low, self.__close, self.__volume, self.__adjustedClose)
        
    def getName(self):
        '''
            Returns name of ticker
        '''
        return self.__name
    
    def getDate(self):
        '''
            Returns date of ticker
        '''
        return self.__date
    
    def getOpen(self):
        '''
            Returns open price of ticker
        '''
        return self.__open
    
    def getHigh(self):
        '''
            Returns highest price of ticker
        '''
        return self.__high
    
    def getLow(self):
        '''
            Returns lowest price of ticker
        '''
        return self.__low
    
    def getClose(self):
        '''
            Returns close price of ticker
        '''
        return self.__close
    
    def getVolume(self):
        '''
            Returns volume (number of buys and sells) of ticker
        '''
        return self.__volume
    
    def getAdjustedClose(self):
        '''
            Returns adjusted close price of ticker
        '''
        return self.__adjustedClose