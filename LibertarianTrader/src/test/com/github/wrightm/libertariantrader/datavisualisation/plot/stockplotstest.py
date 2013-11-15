'''
Created on 23 Oct 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.datacollection.tickerfile import TickerFile
import datetime
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
import os
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.figuresettings import FigureSettings
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.stockplots import CandleSticks
     

class StockPlotTests(unittest.TestCase):


    def testCandleSticks(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 9, 10), tickers) 
        tickers = Tickers(tickers)
        figureSetting = FigureSettings()
        candlesticks = CandleSticks(tickers, figureSetting)
        
        filename = "/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/plots/test/testGoogleTickerWeek.pdf"
        candlesticks.save(filename)
        self.assertEqual(os.path.exists(filename), True,"testTickersJSONDump.json does not exist")
        os.remove(filename)
        
    def testCandleSticksSave(self):

        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 9, 10), tickers) 
        tickers = Tickers(tickers)
        figureSetting = FigureSettings()
        figureSetting['title'] = 'Google Stock price'
        figureSetting['xlabel'] = 'date'
        figureSetting['ylabel'] = 'price ($)'
        candlesticks = CandleSticks(tickers, figureSetting)
        
        filename = "/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/plots/test/testGoogleTickerWeekCandles.pdf"
        candlesticks.save(filename)
        
if __name__ == "__main__":
    unittest.main()