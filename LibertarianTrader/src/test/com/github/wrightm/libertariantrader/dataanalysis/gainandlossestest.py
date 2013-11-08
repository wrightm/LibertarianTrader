'''
Created on 5 Nov 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.dataanalysis.gainandlosses import TickersGainAndLosses
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
from src.main.com.github.wrightm.libertariantrader.datacollection.tickerfile import TickerFile
import datetime
from src.main.com.github.wrightm.libertariantrader.datavisualisation.stockplots import Plot
from src.main.com.github.wrightm.libertariantrader.datavisualisation.figuresettings import FigureSettings
import matplotlib


class GainAndLossesTest(unittest.TestCase):


    def testGetScopeOperator(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        orderedTickers = sorted(tickers, key=lambda tick: tick.getDate())
        analysis = TickersGainAndLosses(tickers)
        
        ticker = orderedTickers[1]
        self.assertEqual(analysis[ticker], (-6.009999999999991, -1.0256147715831312) )
    
    
    def testGetTickersMethod(self):
    
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        orderedTickers = sorted(tickers, key=lambda tick: tick.getDate())
        analysis = TickersGainAndLosses(tickers)
    
        self.assertEqual(len(analysis.getTickers()), len(orderedTickers[1:]))
    
    def testGetGainsAndLossesAbsolutValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for value, ticker in zip(analysis.getGainsAndLosses(), analysis.getTickers()):
            self.assertEqual(value, analysis[ticker][0])
    
    def testGetGainsAndLossesPercentageValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for percentage, ticker in zip(analysis.getGainsAndLosses(returnPercentage=True), analysis.getTickers()):
            self.assertEqual(percentage, analysis[ticker][1])
            
            
    def testGetGainsAndLossesPercentageAndAbsoluteValues(self):

        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for value, percentage, ticker in zip(analysis.getGainsAndLosses(), analysis.getGainsAndLosses(returnPercentage=True), analysis.getTickers()):
            self.assertEqual((value, percentage), analysis[ticker])
    
    def testGetPairsAbsoluteValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        self.assertEqual(len(tickers)-1,len(analysis.getPairs()))
        
    def testGetPairsPercentageValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        self.assertEqual(len(tickers)-1,len(analysis.getPairs(returnPercentage=True)))
    
    def testGetPairsPercentageAndAbsoluteValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for ticker, value, percentage in analysis.getPairs(returnAbsAndPer=True):
            self.assertEqual((ticker, value, percentage), (ticker, analysis[ticker][0], analysis[ticker][1]))
    
    def testIterItemsAbsoluteValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for ticker, value in analysis.iteritems():
            self.assertIn(value, analysis.getGainsAndLosses()) 
        
    
    def testIterItemsPercentageValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for ticker, percentage in analysis.iteritems(returnPercentage=True):
            self.assertIn(percentage, analysis.getGainsAndLosses(returnPercentage=True)) 
    
    def testIterTickers(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        count = 0
        for ticker in analysis.iterTickers():
            count += 1
            
        self.assertEqual(count, len(tickers)-1)
    
    def testIterGainsAndLossesValues(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for value in analysis.iterGainsAndLossesValue():
            self.assertIn(value, analysis.getGainsAndLosses()) 
    
    def testIterGainsAndLossesPercentage(self):

        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        for percentage in analysis.iterGainsAndLossesPercentage():
            self.assertIn(percentage, analysis.getGainsAndLosses(returnPercentage=True)) 
    
    
    def testGetTotalGains(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        
        #self.assertEqual(analysis.getTotalGains(), )
    
    def testGetTotalNumberOfGains(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        self.assertEqual(analysis.getTotalNumberOfGains(), 53)
    
    def testGetTotalNumberOfLosses(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        self.assertEqual(analysis.getTotalNumberOfLosses(), 37)
    
    def testGetTotalDifferenceBetweenGainsAndLosses(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        self.assertEqual(analysis.getTotalDifferenceBetweenGainsAndLosses(), 269.87)
    
    def testGetProbabilityOfGain(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        self.assertAlmostEqual(analysis.getProbabilityOfGain(), 0.59,2)
    
    def testGetProbabilityOfLoss(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        self.assertAlmostEqual(analysis.getProbabilityOfLoss(), 0.411, 2)
    
    def testGainsAndLossesPlotting(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2012, 01, 10), tickers) 
        tickers = Tickers(tickers)
        analysis = TickersGainAndLosses(tickers)
        figureSettings = FigureSettings()
        figureSettings["color"] = 'green'
        figureSettings["linestyle"] = 'solid'
        figureSettings["marker"] = 'o'
        figureSettings["markerfacecolor"] = 'blue'
        figureSettings["markersize"] = 4
        figureSettings["xlabel"] = 'date'
        figureSettings["ylabel"] = 'percentage change'
        figureSettings["fmt"] = ''
        plot = Plot("plot_date", analysis, figureSettings, returnPercentage=True)
        fig, ax = plot.setup()
        # Set minor x ticks on Mondays.
        ax.xaxis.set_minor_locator(matplotlib.dates.WeekdayLocator(byweekday=matplotlib.dates.MO))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b\n%Y'))
        plot.save("/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/plots/test/gainsAndLossesTest")
    
if __name__ == "__main__":
    unittest.main()