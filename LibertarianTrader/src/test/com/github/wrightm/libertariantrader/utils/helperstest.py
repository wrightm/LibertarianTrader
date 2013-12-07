'''
Created on 24 Nov 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.datacollection.ticker import Ticker
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
from src.main.com.github.wrightm.libertariantrader.utils.generalhelpers import Helpers


class HelpersTest(unittest.TestCase):


    def testSumWrapper(self):
        
        firstSet = [1,2,3,4,5]
        
        numericCount = Helpers.sumWrapper(firstSet)
        self.assertEqual(numericCount, 15)
        
        tickerOne = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        tickerTwo = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        tickerThree = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        tickerFour = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        tickerFive = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        tickers.append(tickerThree)
        tickers.append(tickerFour)
        tickers.append(tickerFive)
        
        tickerCount = Helpers.sumWrapper(tickers)
        ticker = Ticker("Google", "1986-10-01", "5.00", "5.00", "5.00", "5.00", "5", "5.00")
        self.assertEqual(ticker, tickerCount)
                   

    def testDivideWrapper(self):
        
        self.assertEqual(Helpers.divideWrapper(1.0, 0.0), 0.0)
        
    def testFloorDivideWrapper(self):
        
        self.assertEqual(Helpers.floorDivideWrapper(1.0, 0.0), 0.0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()