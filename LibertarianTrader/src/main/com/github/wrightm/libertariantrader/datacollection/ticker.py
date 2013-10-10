'''
Stock market ticker:
        Holds name, date, open price, highest price, lowest price, close price, volume and adjusted close price
@author: wrightm
'''

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
        self.__date = date
        self.__open = start
        self.__high = high
        self.__low = low
        self.__close = close
        self.__volume = volume
        self.__adjustedClose = adjustedClose
    
    def __eq__(self, other):
        
        if self.__name == other.__name and \
            self.__date == other.__date and \
            self.__open == other.__open and \
            self.__high == other.__high and \
            self.__low == other.__low and \
            self.__close == other.__close and \
            self.__volume == other.__volume and self.__adjustedClose == other.__adjustedClose:
            return True
        else:
            return False
            
    def __str__(self):
        return "name: %s - date: %s - open: %s - high: %s - low: %s - close: %s - volume: %s - adjustedClose: %s" % (self.__name, self.__date, self.__open, self.__high, self.__low, self.__close, self.__volume, self.__adjustedClose)
        
    def getName(self):
        return self.__name
    
    def getDate(self):
        return self.__date
    
    def getOpen(self):
        return self.__open
    
    def getHigh(self):
        return self.__high
    
    def getLow(self):
        return self.__low
    
    def getClose(self):
        return self.__close
    
    def getVolume(self):
        return self.__volume
    
    def getAdjustedClose(self):
        return self.__adjustedClose