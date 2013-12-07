'''
Stock market ticker:
        Holds name, date, open price, highest price, lowest price, close price, volume and adjusted close price
@author: wrightm
'''
import datetime
import math
from src.main.com.github.wrightm.libertariantrader.utils.generalhelpers import Helpers

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
        self.__open = float(start)
        self.__high = float(high)
        self.__low = float(low)
        self.__close = float(close)
        self.__volume = long(volume)
        self.__adjustedClose = float(adjustedClose)
        
        if isinstance(date, datetime.datetime):
            self.__date = date
        else:
            self.__date = datetime.datetime.strptime(date,'%Y-%m-%d')
    
    def __eq__(self, other):
        
        if not isinstance(other, Ticker):
            return False
        return (self.__name, self.__date, self.__open, self.__high, self.__low, self.__close, self.__volume, self.__adjustedClose) == \
            (other.__name, other.__date, other.__open, other.__high, other.__low, other.__close, other.__volume, other.__adjustedClose)

    def __hash__(self):
        return hash((self.__name, self.__date, self.__open, self.__high, self.__low, self.__close, self.__volume, self.__adjustedClose))
                
    def __str__(self):
        return "name: %s - date: %s - open: %s - high: %s - low: %s - close: %s - volume: %s - adjustedClose: %s" % (self.__name, self.__date, self.__open, self.__high, self.__low, self.__close, self.__volume, self.__adjustedClose)

    def __gt__(self, other):
        return self.__date > other.__date
    
    def __lt__(self, other):
        return self.__date < other.__date
    
    def __ge__(self, other):
        return self.__date >= other.__date
    
    def __le__(self, other):
        return self.__date <= other.__date
    
    def __pos__(self):
        return Ticker(self.__name,
                      self.__date,
                      self.__open,
                      self.__high,
                      self.__low,
                      self.__close,
                      self.__volume,
                      self.__adjustedClose )
        
    def __neg__(self):
        return Ticker(self.__name,
                      self.__date,
                      -self.__open,
                      -self.__high,
                      -self.__low,
                      -self.__close,
                      -self.__volume,
                      -self.__adjustedClose )
    
    def __abs__(self):
        return Ticker(self.__name,
                      self.__date,
                      abs(self.__open),
                      abs(self.__high),
                      abs(self.__low),
                      abs(self.__close),
                      abs(self.__volume),
                      abs(self.__adjustedClose) )
        
    def __add__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('addition object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open + other,
                          self.__high + other,
                          self.__low + other,
                          self.__close + other,
                          self.__volume + other,
                          self.__adjustedClose + other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open + other.__open,
                          self.__high + other.__high,
                          self.__low + other.__low,
                          self.__close + other.__close,
                          self.__volume + other.__volume,
                          self.__adjustedClose + other.__adjustedClose)
    
    def __sub__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('subtraction object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open - other,
                          self.__high - other,
                          self.__low - other,
                          self.__close - other,
                          self.__volume - other,
                          self.__adjustedClose - other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open - other.__open,
                          self.__high - other.__high,
                          self.__low - other.__low,
                          self.__close - other.__close,
                          self.__volume - other.__volume,
                          self.__adjustedClose - other.__adjustedClose)
    
    def __mul__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('multiplication object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open * other,
                          self.__high * other,
                          self.__low * other,
                          self.__close * other,
                          self.__volume * other,
                          self.__adjustedClose * other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open * other.__open,
                          self.__high * other.__high,
                          self.__low * other.__low,
                          self.__close * other.__close,
                          self.__volume * other.__volume,
                          self.__adjustedClose * other.__adjustedClose)

    def __floordiv__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('floordiv object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          Helpers.floorDivideWrapper(self.__open, other),
                          Helpers.floorDivideWrapper(self.__high, other),
                          Helpers.floorDivideWrapper(self.__low, other),
                          Helpers.floorDivideWrapper(self.__close, other),
                          Helpers.floorDivideWrapper(self.__volume, other),
                          Helpers.floorDivideWrapper(self.__adjustedClose, other))
        else:
            return Ticker(self.__name,
                          self.__date, 
                          Helpers.floorDivideWrapper(self.__open, other.__open),
                          Helpers.floorDivideWrapper(self.__high, other.__high),
                          Helpers.floorDivideWrapper(self.__low, other.__low),
                          Helpers.floorDivideWrapper(self.__close, other.__close),
                          long(Helpers.floorDivideWrapper(float(self.__volume),float(other.__volume))),
                          Helpers.floorDivideWrapper(self.__adjustedClose, other.__adjustedClose))
    
    def __div__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('division object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          Helpers.divideWrapper(self.__open, other),
                          Helpers.divideWrapper(self.__high, other),
                          Helpers.divideWrapper(self.__low, other),
                          Helpers.divideWrapper(self.__close, other),
                          Helpers.divideWrapper(self.__volume, other),
                          Helpers.divideWrapper(self.__adjustedClose, other))
        else:
            return Ticker(self.__name,
                          self.__date, 
                          Helpers.divideWrapper(self.__open, other.__open),
                          Helpers.divideWrapper(self.__high, other.__high),
                          Helpers.divideWrapper(self.__low, other.__low),
                          Helpers.divideWrapper(self.__close, other.__close),
                          long( Helpers.divideWrapper(float(self.__volume), float(other.__volume))),
                          Helpers.divideWrapper(self.__adjustedClose, other.__adjustedClose))
    
    def __iadd__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('addition object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open + other,
                          self.__high + other,
                          self.__low + other,
                          self.__close + other,
                          self.__volume + other,
                          self.__adjustedClose + other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open + other.__open,
                          self.__high + other.__high,
                          self.__low + other.__low,
                          self.__close + other.__close,
                          self.__volume + other.__volume,
                          self.__adjustedClose + other.__adjustedClose)
    
    def __isub__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('subtraction object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open - other,
                          self.__high - other,
                          self.__low - other,
                          self.__close - other,
                          self.__volume - other,
                          self.__adjustedClose - other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open - other.__open,
                          self.__high - other.__high,
                          self.__low - other.__low,
                          self.__close - other.__close,
                          self.__volume - other.__volume,
                          self.__adjustedClose - other.__adjustedClose)
    
    def __imul__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('multiplication object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open * other,
                          self.__high * other,
                          self.__low * other,
                          self.__close * other,
                          self.__volume * other,
                          self.__adjustedClose * other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open * other.__open,
                          self.__high * other.__high,
                          self.__low * other.__low,
                          self.__close * other.__close,
                          self.__volume * other.__volume,
                          self.__adjustedClose * other.__adjustedClose)

    def __ifloordiv__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('floordiv object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open // other,
                          self.__high // other,
                          self.__low // other,
                          self.__close // other,
                          self.__volume // other,
                          self.__adjustedClose // other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open // other.__open,
                          self.__high // other.__high,
                          self.__low // other.__low,
                          self.__close // other.__close,
                          long(float(self.__volume) // float(other.__volume)),
                          self.__adjustedClose // other.__adjustedClose)
    
    def __idiv__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('division object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open / other,
                          self.__high / other,
                          self.__low / other,
                          self.__close / other,
                          self.__volume / other,
                          self.__adjustedClose / other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open / other.__open,
                          self.__high / other.__high,
                          self.__low / other.__low,
                          self.__close / other.__close,
                          long(float(self.__volume) / float(other.__volume)),
                          self.__adjustedClose / other.__adjustedClose)
    
    
    def __mod__(self, other):
        
        if not isinstance(other, (int, long, float, complex, Ticker)):
            raise TypeError('modulus object is not a Numeric or Ticker type')
        
        if isinstance(other, (int, long, float, complex)):
            return Ticker(self.__name,
                          self.__date, 
                          self.__open % other,
                          self.__high % other,
                          self.__low % other,
                          self.__close % other,
                          self.__volume % other,
                          self.__adjustedClose % other)
        else:
            return Ticker(self.__name,
                          self.__date, 
                          self.__open % other.__open,
                          self.__high % other.__high,
                          self.__low % other.__low,
                          self.__close % other.__close,
                          long(float(self.__volume) % float(other.__volume)),
                          self.__adjustedClose % other.__adjustedClose)
    
    def __pow__(self, n):
        return Ticker(self.__name,
                      self.__date, 
                      pow(self.__open,n),
                      pow(self.__high,n),
                      pow(self.__low,n),
                      pow(self.__close,n),
                      pow(self.__volume,n),
                      pow(self.__adjustedClose,n))
        
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