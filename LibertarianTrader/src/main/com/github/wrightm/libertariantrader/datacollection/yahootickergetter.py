'''
Retrieves Yahoo Ticker data for particular ID's and their respective interval dates

usage:

    import datetime
    
    start = datetime.date(2000, 1, 1)
    end = datetime.date.today()
    stockInfoToGet = {'GOOG': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                      'YHOO': { 'startDate': start, 'endDate': end, 'interval': 'w'}
                    }
             
    tickerInfoGetter = YahooTickerGetter()               
    tickerInfo = tickerInfoGetter.getMultipleHistoricStockMarkgetData(stockInfoToGet)
        
@author: michaelwright
'''

#!/usr/bin/env python

#=====================================
# imports
#=====================================

#=====================================
# python system
#=====================================
import urllib
from Queue import Queue
import threading

class YahooTickerGetter(object):
    '''
        Retrieves Yahoo Ticker data for particular ID's and their respective interval dates
    '''
    def __init__(self):
        self.__rlock = threading.RLock()
        
    def __stockMarketWorker(self, allStockInfo,queue):
        """
            Thread safe stock market ticker info getter
            @param allStockInfo: dictionary of ticker data
            @param queue: thread safe queue of ticker information to retrieve
        """
        data = queue.get()
        ticker = self.getHistoricStockMarkgetData(data[0], data[1], data[2], data[3])
        if ticker:
            allStockInfo[data[0]] = ticker
        queue.task_done()
        
    def getHistoricStockMarkgetData(self, ID, startDate, endDate, interval='w'):
        """
            Return Stock ID INFO From Yahoo
            @param ID: name of ticker
            @param startDate: start date of ticker information
            @param endDate: end date of ticker information
            @param interval: interval of data collection
            @return String of ticker information for date interval
        """
        with self.__rlock:
            url = 'http://ichart.yahoo.com/table.csv?'
    
            query_args = { 's':ID, 'a': startDate.month, 'b': startDate.day, 'c': startDate.year, 
                  'd':endDate.month, 'e':endDate.day, 'f':endDate.year, 'g':interval, 'ignore':'.csv'}

            encoded_args = urllib.urlencode(query_args)
            response = urllib.urlopen(url+encoded_args)
            if response.getcode() != 200:
                return None
            return response.read()

    def getMultipleHistoricStockMarkgetData(self, tickersToDownload):
        '''
            Return dictionary of all stock information
            @param tickersToDownload: dictionary of tickers information to download
        '''
        threadQueue  = Queue()
        allStockInfo = dict() 
    
        for indx in range(len(tickersToDownload)):
            thrd = threading.Thread(target=self.__stockMarketWorker, args=(allStockInfo, threadQueue))
            thrd.setDaemon(True)
            thrd.start()
         
    
        for name, tickerInfo in tickersToDownload.iteritems():
            queueData = [name, tickerInfo['startDate'], tickerInfo['endDate'], tickerInfo['interval']]
            threadQueue.put(queueData)
        
        threadQueue.join()
    
        main_thread = threading.currentThread()
        for thrd in threading.enumerate():
            if thrd is main_thread:
                continue
            thrd.join()
    
        return allStockInfo

