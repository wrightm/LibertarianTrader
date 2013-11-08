'''
Parses Yahoo CSV Files into a usable python object

usage:

    Downloading more than one ticker
    
    import datetime
    
    start = datetime.date(2000, 1, 1)
    end = datetime.date.today()
    stockInfoToGet = {'GOOG': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                     'YHOO': { 'startDate': start, 'endDate': end, 'interval': 'w'}
                    }
             
    tickerInfoGetter = YahooTickerGetter()               
    tickerInfo = tickerInfoGetter.getMultipleHistoricStockMarkgetData(stockInfoGetter)
    
    yahooTickerParser = YahooTickerParser()
    yahooParsedTickerData = yahooTickerParser.parse(tickerInfo)

    ============
    ============

    Downloading one ticker
    
    import datetime
    
    start = datetime.date(2000, 1, 1)
    end = datetime.date.today()
        
    tickerInfoGetter = YahooTickerGetter()               
    tickerInfo = tickerInfo.getHistoricStockMarkgetData('GOOG', start, end, 'w')
        
    yahooTickerParser = YahooTickerParser()
    yahooParsedTickerData = yahooTickerParser.parse(('GOOG',tickerInfo))

@author: wrightm
'''
#!/usr/bin/env python

#=====================================
# imports
#=====================================

#=====================================
# python system
#=====================================
import datetime

#=====================================
# LibertarianTrader system
#=====================================
from src.main.com.github.wrightm.libertariantrader.datacollection.yahootickergetter import YahooTickerGetter

class YahooTickerParser(object):
    '''
        Parses Yahoo CSV Files into a usable python object
    '''


    def __isInfoTitleListValid(self, infoTitleList):
        '''
            Check whether title of downloaded yahoo csv ticker information has valid column headers
            @param infoTitleList: list of column headers
            @return: True if column headers are valid. Else False
        '''
        if 'Date' in infoTitleList and \
        'Open' in infoTitleList and \
        'High' in infoTitleList and \
        'Low' in infoTitleList and \
        'Close' in infoTitleList and \
        'Volume' in infoTitleList and \
        'Adj Close' in infoTitleList:
            return True
        else:
            return False
    
    
    def __parseDict(self, yahooStockInfo):
        '''
            Parse stock information data that is in a dictionary format. 
            The data will be given to the method by the YahooTickerGetter objects               
            getMultipleHistoricStockMarkgetData method
            
            @precondition: yahooStockInfo will be the output from YahooTickerGetter::getMultipleHistoricStockMarkgetData
            @param yahooStockInfo: dictionary of stock information
            @return: parsed stock information
        '''
        stockData = {}
        for name, info in yahooStockInfo.iteritems():
            stockData[name] = {} 
            listOfTickerInfoByDate = info.split('\n')
            for pos, item in enumerate(listOfTickerInfoByDate):
                if pos == 0:
                    infoTitleList = item.split(',')
                    if len(infoTitleList) != 7 and self.__isInfoTitleListValid(infoTitleList):
                        raise ValueError('yahoo csv column title is not valid')
                else:
                    infoDataList = item.split(',')
                    if len(infoDataList) != 7:
                        continue
                
                    date = infoDataList[0]
                    start = infoDataList[1]
                    high = infoDataList[2]
                    low = infoDataList[3]
                    close = infoDataList[4]
                    volume = infoDataList[5]
                    adjustedClose = infoDataList[6]
                
                    stockData[name][date] = {}
                    stockData[name][date]['open'] = start
                    stockData[name][date]['high'] = high
                    stockData[name][date]['low'] = low
                    stockData[name][date]['close'] = close
                    stockData[name][date]['volume'] = volume
                    stockData[name][date]['adjustedClose'] = adjustedClose
                 
        return stockData
    
    
    def __parseTuple(self, yahooStockInfo):
        '''
            Parse stock information data that is in a tuple format. 
            The data will be given to the method by the YahooTickerGetter objects               
            getHistoricStockMarkgetData method
            
            @precondition: yahooStockInfo will be the output from YahooTickerGetter::getHistoricStockMarkgetData
            @param yahooStockInfo: tuple of stock information
            @return: parsed stock information
        '''
        name = yahooStockInfo[0]
        info = yahooStockInfo[1]
        stockData = {}
        stockData[name] = {}
        listOfTickerInfoByDate = info.split('\n')
        for pos, item in enumerate(listOfTickerInfoByDate):
            if pos == 0:
                infoTitleList = item.split(',')
                if len(infoTitleList) != 7 and self.__isInfoTitleListValid(infoTitleList):
                    raise ValueError('yahoo csv column title is not valid')
            else:
                infoDataList = item.split(',')
                if len(infoDataList) != 7:
                    continue
                date = infoDataList[0]
                start = infoDataList[1]
                high = infoDataList[2]
                low = infoDataList[3]
                close = infoDataList[4]
                volume = infoDataList[5]
                adjustedClose = infoDataList[6]
                
                stockData[name][date] = {}
                stockData[name][date]['open'] = start
                stockData[name][date]['high'] = high
                stockData[name][date]['low'] = low
                stockData[name][date]['close'] = close
                stockData[name][date]['volume'] = volume
                stockData[name][date]['adjustedClose'] = adjustedClose
                 
        return stockData
    
    
    def parse(self, yahooStockInfo):
        '''
            Return parsed stock information
            @param yahooStockInfo: either tuple or dictionary stock information
            @return parsed stock information
            @raise TypeError: when yahooStockInfo is not of type dict or tuple
        '''
        if isinstance(yahooStockInfo, dict):
            return self.__parseDict(yahooStockInfo)
        elif isinstance(yahooStockInfo, tuple):
            return self.__parseTuple(yahooStockInfo)
        else:
            raise TypeError('yahooStockInfo must be of type dict or type tuple')
        
    def testDictParser(self):

        start = datetime.date(2000, 1, 1)
        end = datetime.date.today()
        stockInfo = {'GOOG': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                 'YHOO': { 'startDate': start, 'endDate': end, 'interval': 'w'}
                }
             
        tickerInfo = YahooTickerGetter()               
        stocks = tickerInfo.getMultipleHistoricStockMarkgetData(stockInfo)
    
        yahooTickerParser = YahooTickerParser()
        yahooStockData = yahooTickerParser.parse(stocks)

        assert(len(yahooStockData) > 0) 
        
    def testTupleParse(self):
        
        start = datetime.date(2000, 1, 1)
        end = datetime.date.today()
        
        tickerInfo = YahooTickerGetter()               
        stock = tickerInfo.getHistoricStockMarkgetData('GOOG', start, end, 'w')
        
        yahooTickerParser = YahooTickerParser()
        yahooStockData = yahooTickerParser.parse(('GOOG',stock))
        
        assert(len(yahooStockData) > 0) 
        
def test():
    
    yahooTickerParserTest = YahooTickerParser()
    yahooTickerParserTest.testDictParser()
    yahooTickerParserTest.testTupleParse()    
    
if __name__ == "__main__":
    test()    