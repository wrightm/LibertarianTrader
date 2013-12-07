'''
Created on 23 Nov 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
import math
from src.main.com.github.wrightm.libertariantrader.datacollection.ticker import Ticker
from src.main.com.github.wrightm.libertariantrader.dataanalysis.statistics.helpermethods import Stats

class StatisticsTickerTest(unittest.TestCase):


    def testMean(self):
        
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
        
        tickerMean = Stats.mean(tickers)

        self.assertEqual(tickerMean, tickerOne)
        
    def testVar(self):
        
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
        
        tickerVar = Stats.var(tickers)
        
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        
        self.assertEqual(tickerVar,ticker)
        
    def testStdev(self):
        
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
        
        tickerTest = Stats.stdev(tickers)
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest,ticker)
        
    def testScore(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        tickerTest = Stats.score(tickerOne, 0.0, 1.0)
        
        self.assertEqual(tickerTest, tickerOne)
        
    def testZscores(self):
        
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
        
        tickerTest = Stats.zscores(tickers)
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        for test in tickerTest:
            self.assertEqual(test, ticker)
        
    def testMad(self):
        
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
        
        tickerTest = Stats.mad(tickers)
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
    
    def testMin(self):
        
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
        
        tickerTest = Stats.min(tickers)
        
        self.assertEqual(tickerTest, tickerOne)
    
    def testMax(self):
        
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
        
        tickerTest = Stats.max(tickers)
        
        self.assertEqual(tickerTest, tickerOne)
        
    def testRange(self):
        
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
        
        tickerTest = Stats.range(tickers)
        
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
        
    def testKurtosis(self):
        
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
        
        tickerTest = Stats.kurtosis(tickers)
        
        ticker = Ticker("Google", "1986-10-01", "-3.00", "-3.00", "-3.00", "-3.00", "-3", "-3.00")
        self.assertEqual(tickerTest, ticker)
        
    def testSkewness(self):
        
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
        
        tickerTest = Stats.skewness(tickers)
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
        
        
    def testStandardError(self):
        
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
        
        tickerTest = Stats.standardError(tickers)
        
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
        
    def testCovariance(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        tickerTwo = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        
        tickerTest = Stats.covariance(tickerOne, 1, tickerTwo, 1, 1)
        
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
    
    def testCovarianceFromSets(self):
        
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
        
        tickerTest = Stats.covarianceFromSets(tickers, Tickers(tickers.getTickerList()))
        
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
        
    def testCorrelation(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        tickerTwo = Ticker("Google", "1986-10-01", "1.00", "1.00", "1.00", "1.00", "1", "1.00")
        
        tickerTest = Stats.correlation(tickerOne, 1, 1, tickerTwo, 1, 1, 1)
        
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
    
    def testCorrelationFromSets(self):
        
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
        
        tickerTest = Stats.correlationFromSets(tickers, Tickers(tickers.getTickerList()))
        
        ticker = Ticker("Google", "1986-10-01", "0.00", "0.00", "0.00", "0.00", "0", "0.00")
        self.assertEqual(tickerTest, ticker)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()