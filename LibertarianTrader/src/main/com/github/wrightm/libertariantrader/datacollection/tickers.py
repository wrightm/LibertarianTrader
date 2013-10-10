'''
A collection of tickers that can be viewed in a number of Orders:
        name, date, open price, highest price, lowest price, close price, volume and adjusted close price
@author: wrightm
'''
import copy
from src.main.com.github.wrightm.libertariantrader.datacollection.ticker import Ticker

class Tickers(object):
    '''
    A collection of tickers that can be viewed in a number of Orders:
        name, date, open price, highest price, lowest price, close price, volume and adjusted close price
    '''
    def __init__(self, tickers = None):
        '''
            initialise tickers list or deep copy existing tickers
            @param tickers: list of Ticker objects
            @raise ValueError: when ticker is not of type list
        '''
        if not self.isTickerListValid(tickers) and tickers:
            raise ValueError('tickers is not a valid ticker list')
        self.__tickers = copy.deepcopy(tickers) if tickers else []
    
    def __len__(self):
        return len(self.__tickers)
    
    def __getitem__(self, key):
        return self.__tickers[key]
    
    def __setitem__(self, key, value):
        if not isinstance(value, Ticker):
            raise ValueError('value must be of type Ticker')
        self.__tickers[key] = value
    
    def __delitem__(self, key):
        del self.__tickers[key]
    
    def __iter__(self):
        return iter(self.__tickers)
    
    def __reversed__(self):
        return Tickers(reversed(self.__tickers))
    
    def head(self):
        '''
            Return first ticker in list
        '''
        return self.__tickers[0]
    
    def tail(self):
        return self.__tickers[1:]
    
    def init(self):
        '''
            Return list of tickers apart from last ticker in original list.
        '''
        return self.__tickers[:-1]
    
    def last(self):
        '''
            Return last ticker
        '''
        return self.__tickers[-1]
    
    def drop(self, n):
        '''
            Drops first n tickers in list and returns list
            @param n: first n tickers in list 
            @return list of left over tickers from n
        '''
        return self.__tickers[n:]
    
    def take(self, n):
        '''
            Returns first n tickers in list
            @param n: first n tickers in list
            @return list of first n tickers
        '''
        return self.__tickers[:n]
    
    def isTickerListValid(self, tickers):
        '''
            Checks whether ticker list is valid
            @param tickers: list of Ticker objects
            @return: boolean. True is ticker list is valid, False is ticker list is invalid 
        '''
        if not isinstance(tickers, list):
            return False
        
        for ticker in tickers:
            if not isinstance(ticker, Ticker):
                return False
        
        return True
    
    def append(self, ticker):
        '''
           Add ticker to ticker list.
           @param ticker: Ticker object to be added to Ticker list 
           @raise ValueError:  when argument is not of type ticker 
        '''    
        if not isinstance(ticker, Ticker):
            raise ValueError('ticker argument must be of type Ticker')
        
        self.__tickers.append(ticker)    
    
    def remove(self, ticker):
        '''
           Remove first instance of ticker from ticker list.
           @param ticker: Ticker object to be removed from Ticker list 
           @raise ValueError:  when argument is not of type ticker 
        '''  
        if not isinstance(ticker, Ticker):
            raise ValueError('ticker argument must be of type Ticker')
        
        self.__tickers.remove(ticker)
        
    def removeAll(self, ticker):
        '''
           Remove all instances of ticker from ticker list.
           @param ticker: Ticker object to be removed from Ticker list 
           @raise ValueError:  when argument is not of type ticker 
        '''  
        if not isinstance(ticker, Ticker):
            raise ValueError('ticker argument must be of type Ticker')
 
        self.__tickers = filter(lambda element: element != ticker, self.__tickers)
        
    def getTickerList(self):
        return copy.deepcopy(self.__tickers)