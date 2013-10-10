'''

@author: wrightm
'''
import datetime
from src.main.com.github.wrightm.libertariantrader.datacollection.yahootickergetter import YahooTickerGetter

class YahooTickerParser(object):
    '''
    Parses Yahoo CSV Files into a usable python object
    '''


    def __isInfoTitleListValid(self, infoTitleList):
        
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
    
    
    def __parseStr(self, yahooStockInfo):
        
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
        
        if isinstance(yahooStockInfo, dict):
            return self.__parseDict(yahooStockInfo)
        elif isinstance(yahooStockInfo, tuple):
            return self.__parseStr(yahooStockInfo)
        else:
            raise ValueError('yahooStockInfo must be of type dict or type tuple')
        
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
        
    def testStringParse(self):
        
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
    yahooTickerParserTest.testStringParse()    
    
if __name__ == "__main__":
    test()    