'''
First Chapter Of ThinkStats

@author: wrightm
'''
import datetime
from src.main.com.github.wrightm.libertariantrader.datacollection.yahootickergetter import YahooTickerGetter
from src.main.com.github.wrightm.libertariantrader.datacollection.yahootickerparser import YahooTickerParser
import os
from src.main.com.github.wrightm.libertariantrader.datacollection.tickerfile import TickerFile

def main():
    
    filename = '/Volumes/Michael Wright 1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/thinkStatsTickersJSON.json'
    tickerFile = TickerFile(filename)
    
    if not os.path.exists(filename):
        start = datetime.date(2000, 1, 1)
        end = datetime.date(2013, 10, 10)
    
        stockInfo = {'GOOG': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                     'YHOO': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                     'FB': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                     'ORCL': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                     'AMZN': { 'startDate': start, 'endDate': end, 'interval': 'w'},
                     'MSFT': { 'startDate': start, 'endDate': end, 'interval': 'w'}
                     }
             
        tickerInfo = YahooTickerGetter()               
        stocks = tickerInfo.getMultipleHistoricStockMarkgetData(stockInfo)
    
        yahooTickerParser = YahooTickerParser()
        yahooParsedTickerData = yahooTickerParser.parse(stocks)
    
        tickerFile.dump(yahooParsedTickerData)

    tickers = tickerFile.load()
    
    googTickers = filter(lambda ticker: ticker.getName() == 'GOOG', tickers)
    yhooTickers = filter(lambda ticker: ticker.getName() == 'YHOO', tickers)
    fbTickers = filter(lambda ticker: ticker.getName() == 'FB', tickers)
    orclTickers = filter(lambda ticker: ticker.getName() == 'ORCL', tickers)
    amznTickers = filter(lambda ticker: ticker.getName() == 'AMZN', tickers)
    msftTickers = filter(lambda ticker: ticker.getName() == 'MSFT', tickers)
    
    for tickers in [googTickers, yhooTickers, fbTickers, orclTickers, amznTickers, msftTickers]:
        total = 0.0
        for ticker in tickers:
            total += ticker.getClose()
        print '%s Avg Close: %s' % ( ticker.getName(), (total / float(len(tickers))) )

    
    
if __name__ == '__main__':
    main()
    