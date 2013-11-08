'''
Unit Testing Tickers Object

@author: wrightm
'''
from src.main.com.github.wrightm.libertariantrader.datacollection.ticker import Ticker
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers

import unittest


class TickersTest(unittest.TestCase):
    '''
    Unit Testing Tickers Object
    '''

    def testNumberOfTickersUsingConstructor(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickerList = [tickerOne, tickerTwo]
        
        tickers = Tickers(tickerList)
        
        self.assertEqual(len(tickers), 2, "Number of tickers is not equal to 2")
        
    def testNumberOfTickersUsingAppend(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(len(tickers), 2, "Number of tickers is not equal to 2")
        
    def testGetTickerUsingScopeOperator(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers[0], tickerOne, "First ticker does not equal tickerOne")
        
    def testSetTickerUsingScopeOperator(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        tickers[0] = tickerOne
        tickers[1] = tickerTwo
        
        self.assertEqual(tickers[0], tickerOne, "First ticker does not equal tickerOne")
        self.assertEqual(tickers[1], tickerTwo, "Second ticker does not equal tickerTwo")
        
    def testHeadTicker(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers.head(), tickerOne, "Head ticker does not equal tickerOne")
        
    def testTailTickers(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers.tail(), [tickerTwo], "Tail tickers does not equal [tickerTwo]")
    
    def testInitTickers(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers.init(), [tickerOne], "Init tickers does not equal [tickerOne]")
        
    def testLastTicker(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers.last(), tickerTwo, "Last ticker does not equal tickerTwo")
        
    def testDropFirstTicker(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers.drop(1), [tickerTwo], "Tail tickers does not equal [tickerTwo]")
        
    def testTakeTickers(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers.take(-1), [tickerOne], "Take tickers does not equal [tickerOne]")
        
    def testRemovingTicker(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        tickers.remove(tickerTwo)
        self.assertEqual(tickers.getTickerList(), [tickerOne], "tickers does not equal [tickerOne]")
        
    def testAllTickers(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        tickers.append(tickerTwo)
        tickers.append(tickerTwo)
        tickers.append(tickerTwo)
        
        self.assertEqual(len(tickers), 5)
        tickers.removeAll(tickerTwo)
        self.assertEqual(tickers.getTickerList(), [tickerOne], "tickers does not equal [tickerOne]")
        
    def testGetTickers(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1985-10-01", "105.00", "115.00", "95.00", "110.00", "1005", "110.00")
        
        tickers = Tickers()
        tickers.append(tickerOne)
        tickers.append(tickerTwo)
        
        self.assertEqual(tickers.getTickerList(), [tickerOne,tickerTwo], "tickers does not equal [tickerOne,tickerTwo]")    