'''
Created on 7 Oct 2013

@author: wrightm
'''

import json
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
from src.main.com.github.wrightm.libertariantrader.datacollection.ticker import Ticker

class TickerFile(object):
    '''
        JSON File Writer - Downloads and write ticker data to file
    '''
    def __init__(self, filename):
        self.__filename = filename
        
    def dump(self, tickerInfo):
        '''
            Write dictionary
        '''
        with open(self.__filename, 'wb') as fp:
            json.dump(tickerInfo, fp)
        
    def load(self):
        
        with open(self.__filename, 'rb') as fp:
            tickersJSON = json.load(fp)
         
        tickers = Tickers()   
        for tickerName, tickerInfo in tickersJSON.iteritems():
            for date , info in tickerInfo.iteritems():
                ticker = Ticker(tickerName, 
                                date, 
                                info['open'], 
                                info['high'],
                                info['low'],
                                info['close'],
                                info['volume'],
                                info['adjustedClose'])
                tickers.append(ticker)
            
        return tickers
