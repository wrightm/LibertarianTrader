'''
@author: wrightm
'''

import unittest
from src.main.com.github.wrightm.libertariantrader.datacollection.ticker import Ticker
import datetime

class TickerTest(unittest.TestCase):
    '''
    unit test Ticker class
    '''

    def testEqualTickers(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        self.assertEqual(tickerOne, tickerTwo, "Ticker one is not the same object as ticker two")
        
    def testNotEqualTickerWithDifferentNames(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("NotGoogle", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when Name is different")
        
    
    def testNotEqualTickerWithDifferentDates(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "2013-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when Date is different")
    
    def testNotEqualTickerWithDifferentOpen(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "1000000.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when Opening Price is different")
    
    def testNotEqualTickerWithDifferentHigh(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "100.00", "110000.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when High is different")
    
    def testNotEqualTickerWithDifferentLow(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "100.00", "110.00", "90000.00", "105.00", "1000", "105.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when Low is different")
    
    def testNotEqualTickerWithDifferentClose(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105000.00", "1000", "105.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when Close is different")
    
    def testNotEqualTickerWithDifferentVolume(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "10000000", "105.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when Volume is different")
    
    def testNotEqualTickerWithDifferentAdjustedClose(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105000.00")
        
        self.assertNotEqual(tickerOne, tickerTwo, "ticker one is equal to ticker two when Adjusted Close is different")
    
    def testGetName(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getName(), "Google", "ticker one Name is not Google")
    
    def testGetDate(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getDate(), datetime.datetime.strptime("1986-10-01",'%Y-%m-%d'), "ticker one Date is not 1986-10-01")
    
    def testGetOpen(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getOpen(), 100.00, "ticker one Open is not 100.00")
    
    def testGetHigh(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getHigh(), 110.00, "ticker one High is not 110.00")
    
    def testGetLow(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getLow(), 90.00, "ticker one Low is not 90.00")
    
    def testGetClose(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getClose(), 105.00, "ticker one Close is not 105.00")
    
    def testGetVolume(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getVolume(), 1000, "ticker one Volume is not 1000")
    
    def testGetAdjustedClose(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        
        self.assertEqual(tickerOne.getAdjustedClose(), 105.00, "ticker one Adjusted Close is not 105.00")
    
    def testPosMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = +tickerOne        
        self.assertEqual(tickerOne, tickerTwo, "tickerOne does not equal tickerTwo")

    def testNegMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "-100.00", "-110.00", "-90.00", "-105.00", "-1000", "-105.00")

        tickerThree = -tickerOne
        
        self.assertEqual(tickerTwo, tickerThree, "ticker Two does not equal ticker three when ticker one is negative")
        
    def testAbsMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "100.00", "110.00", "90.00", "105.00", "1000", "105.00")
        tickerTwo = Ticker("Google", "1986-10-01", "-100.00", "-110.00", "-90.00", "-105.00", "-1000", "-105.00")

        tickerThree = abs(tickerOne)
        
        self.assertEqual(tickerOne, tickerThree, "ticker One does not equal ticker three when ticker two is abs(negative)")
    
    def testAddMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "10.00", "10.00", "10.00", "10.00", "10", "10.00")
        tickerTwo = Ticker("Google", "1986-10-01",  "20.00", "20.00", "20.00", "20.00", "20", "20.00")

        tickerThree = tickerOne + tickerOne
        
        self.assertEqual(tickerTwo, tickerThree, "ticker Two does not equal ticker three when tickerOne + tickerOne")
        
    def testSubtractMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "10.00", "10.00", "10.00", "10.00", "10", "10.00")
        tickerTwo = Ticker("Google", "1986-10-01",  "20.00", "20.00", "20.00", "20.00", "20", "20.00")

        tickerThree = tickerTwo - tickerOne
        
        self.assertEqual(tickerOne, tickerThree, "ticker One does not equal ticker three when tickerTwo - tickerOne")
  
    
    def testMultipleMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "10.00", "10.00", "10.00", "10.00", "10", "10.00")
        tickerTwo = Ticker("Google", "1986-10-01",  "100.00", "100.00", "100.00", "100.00", "100", "100.00")

        tickerThree = tickerOne * tickerOne
        
        self.assertEqual(tickerTwo, tickerThree, "ticker Two does not equal ticker three when tickerOne * tickerOne")
    
    def testFloorDivideMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "10.00", "10.00", "10.00", "10.00", "10", "10.00")
        tickerTwo = Ticker("Google", "1986-10-01",  "1.00", "1.00", "1.00", "1.00", "1", "1.00")

        tickerThree = tickerOne // tickerOne
        
        self.assertEqual(tickerTwo, tickerThree, "ticker Two does not equal ticker three when tickerOne / tickerOne")
  
    def testDivideMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "10.00", "10.00", "10.00", "10.00", "10", "10.00")
        tickerTwo = Ticker("Google", "1986-10-01",  "1.00", "1.00", "1.00", "1.00", "1", "1.00")

        tickerThree = tickerOne // tickerOne
        
        self.assertEqual(tickerTwo, tickerThree, "ticker Two does not equal ticker three when tickerOne / tickerOne")
  
    def testModMagicMethod(self):
        
        tickerOne = Ticker("Google", "1986-10-01", "2.00", "2.00", "2.00", "2.00", "2", "2")
        tickerTwo = Ticker("Google", "1986-10-01",  "3.00", "3.00", "3.00", "3.00", "3", "3")

        tickerThree = tickerOne % tickerTwo
        
        self.assertEqual(tickerOne, tickerThree, "ticker Two does not equal ticker three when tickerOne % tickerOne")
  
    def testPowMagicMethod(self):
        
        
        tickerOne = Ticker("Google", "1986-10-01", "10.00", "10.00", "10.00", "10.00", "10", "10.00")
        tickerTwo = Ticker("Google", "1986-10-01",  "100.00", "100.00", "100.00", "100.00", "100", "100.00")

        tickerThree = pow(tickerOne, 2)
        
        self.assertEqual(tickerTwo, tickerThree, "ticker Two does not equal ticker three when ticker one is pow(ticker, 2)")
    
