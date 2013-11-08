'''
Created on 29 Oct 2013

@author: wrightm
'''
import unittest
import datetime
from src.main.com.github.wrightm.libertariantrader.datacollection.tickerfile import TickerFile
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
from src.main.com.github.wrightm.libertariantrader.dataanalysis.gainandlosses import TickersGainAndLosses


class GainsAndLossesTutorialTest(unittest.TestCase):


    def testGainsAndLossesGeneralAlgo(self):
        
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        tickerOrderedByTime = sorted(tickers, key=lambda tick: tick.getDate())
        nTickers = len(tickerOrderedByTime) -1 
        totalLoss = 0.0
        totalGains = 0.0
        
        nGains = 0
        nLosses = 0
        
        for indx in range(nTickers+1):
            if  indx > 0:
                diff= tickerOrderedByTime[indx].getAdjustedClose() - tickerOrderedByTime[indx-1].getAdjustedClose()
                
                if diff > 0.0:
                    totalGains += diff
                    nGains += 1
                elif diff < 0.0:
                    totalLoss += diff
                    nLosses += 1
        
        analysis = TickersGainAndLosses(tickers)
        
        self.assertEqual(totalLoss, analysis.getTotalLosses())
        self.assertEqual(totalGains, analysis.getTotalGains())
        self.assertEqual(totalGains + totalLoss, analysis.getTotalDifferenceBetweenGainsAndLosses())
        self.assertEqual(nTickers, len(analysis.getPairs()))
        self.assertEqual(nGains, analysis.getTotalNumberOfGains())
        self.assertEqual(nLosses, analysis.getTotalNumberOfLosses())
        probGain = float(nGains) / float(nTickers)
        self.assertEqual(probGain, analysis.getProbabilityOfGain())
        probLosses = float(nLosses) / float(nTickers)
        self.assertEqual(probLosses, analysis.getProbabilityOfLoss())

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()