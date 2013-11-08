'''
Created on 29 Oct 2013

@author: wrightm
'''
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
from matplotlib.dates import date2num

class TickersGainAndLosses(object):
    '''
    Gains and Losses associated to each ticker from the previous trading day
    '''


    def __init__(self, tickers, sort=True):
        '''
        Initialise and calculate gains and losses for all tickers
        
        Parameters:
        -----------
        @param tickers: Tickers
        list of all tickers
        
        Exceptions:
        -----------
        @raise TypeError: when tickers is not of type Tickers
        '''
        if not isinstance(tickers, Tickers):
            raise TypeError('tickers is not of type Tickers')
        
        self.__tickers = sorted(tickers, key=lambda tick: tick.getDate()) if sort else tickers
        self.__gainsAndLosses = {}
        self.__percentageGainsAndLosses = {}
        self.__calculateGainsAndLosses()
        
    def __calculateGainsAndLosses(self):
        nticks = len(self.__tickers) - 1 
        self.__totalLosses = 0.0
        self.__totalGains = 0.0
        self.__nGains = 0
        self.__nLosses = 0
        for indx, tick in enumerate(self.__tickers):
            if  indx > 0:
                yesterdaysAdjustedClosePrice = self.__tickers[indx-1].getAdjustedClose()
                todaysAdjustedClosePrice = self.__tickers[indx].getAdjustedClose()
                differenceOfAdjustedPrice = todaysAdjustedClosePrice - yesterdaysAdjustedClosePrice
                self.__gainsAndLosses[self.__tickers[indx]] = differenceOfAdjustedPrice
                self.__percentageGainsAndLosses[self.__tickers[indx]] = 100.0 * (differenceOfAdjustedPrice / yesterdaysAdjustedClosePrice)
                if differenceOfAdjustedPrice > 0.0:
                    self.__totalGains += differenceOfAdjustedPrice
                    self.__nGains += 1
                elif differenceOfAdjustedPrice < 0.0:
                    self.__totalLosses += differenceOfAdjustedPrice
                    self.__nLosses += 1
        
        self.__totalDiff = self.__totalGains + self.__totalLosses
        self.__probabilityOfGain = float(self.__nGains) / float(nticks)
        self.__probabilityOfLoss = float(self.__nLosses) / float(nticks)
        
    def __getitem__(self, key):
        return self.__gainsAndLosses.get(key, 0), self.__percentageGainsAndLosses.get(key, 0.0)
    
    def __len__(self):
        return len(self.__gainsAndLosses)
    
    def __delitem__(self, key):
        del self.__gainsAndLosses[key]
        del self.__percentageGainsAndLosses[key]
        
    def getTickers(self):
        """
        Return all tickers in a list
        @return: list
        """
        return self.__gainsAndLosses.keys()
    
    def getGainsAndLosses(self, returnPercentage=False, returnAbsAndPer=False):
        """
        Return all ticker gains and losses in a list
        
        Parameters:
        -----------
        @param returnPercentage: boolean
        if true return all gains and losses as a percentage
        @param returnAbsAndPer: boolean
        if true return all gains and losses as a list of tuples (absolute value, percentage value)
        
        Return:
        -------
        @return: list
        list of gains and losses
        """
        if returnAbsAndPer:
            return zip(self.__gainsAndLosses.values(), self.__percentageGainsAndLosses.values())
        elif returnPercentage:
            return self.__percentageGainsAndLosses.values()
        else:
            return self.__gainsAndLosses.values()
    
    def getPairs(self, returnPercentage=False, returnAbsAndPer=False):
        """
        Return list of tuples either (Ticker, absolute value), (Ticker, percentage) or (Ticker, absolute value, percentage)
        
        Parameters:
        -----------
        @param returnPercentage: boolean
        if true return a list of (Ticker, percentage)
        @param returnAbsAndPer: boolean
        if true return a list of (Ticker, absolute value, percentage)
        
        Return:
        -------
        @return: list of tuples
        returns either (Ticker, absolute value), (Ticker, percentage) or (Ticker, absolute value, percentage)
        """
        if returnAbsAndPer:
            return zip(self.__gainsAndLosses.keys(), self.__gainsAndLosses.values(), self.__percentageGainsAndLosses.values())
        elif returnPercentage:
            dates = [date2num(tick.getDate()) for tick in self.__percentageGainsAndLosses.keys()]
            return zip(dates, self.__percentageGainsAndLosses.values())
        else:
            dates = [date2num(tick.getDate().date()) for tick in self.__gainsAndLosses.keys()]
            return zip(dates, self.__gainsAndLosses.values())
    
    def iteritems(self, returnPercentage=False):
        """
        Return iter of tuples (ticker, gains and losses) either as an absolute value or a percentage
        
        Parameters:
        -----------
        @param returnPercentage: boolean
        if true return iter as a percentage
        
        @return: iter tuples 
        (ticker, gains and losses) either as an absolute value or a percentage
        """
        if returnPercentage:
            return self.__percentageGainsAndLosses.iteritems()
        else:
            return self.__gainsAndLosses.iteritems()
    
    def iterTickers(self):
        """
        Return iter of tickers
        """
        return self.__gainsAndLosses.iterkeys()
    
    def iterGainsAndLossesValue(self):
        """
        Return iter of gains and losses as an absolute value
        """
        return self.__gainsAndLosses.itervalues() 
    
    def iterGainsAndLossesPercentage(self):
        """
        Return iter of gains And losses as a percentage
        """
        return self.__percentageGainsAndLosses.itervalues() 
    
    def getTotalLosses(self):
        """
        Return total losses
        """
        return self.__totalLosses
        
    def getTotalGains(self):
        """
        Return total gains
        """
        return self.__totalGains
    
    def getTotalNumberOfGains(self):
        """
        Return total number of gains
        """
        return self.__nGains
        
    def getTotalNumberOfLosses(self):
        """
        Return total number of losses
        """
        return self.__nLosses
    
    def getTotalDifferenceBetweenGainsAndLosses(self):
        """
        Return total difference between total gains and losses
        """   
        return self.__totalDiff
        
    def getProbabilityOfGain(self):
        """
        Return probability of a gain
        """
        return self.__probabilityOfGain
    
    def getProbabilityOfLoss(self):
        """
        Return probability of a Loss
        """
        return self.__probabilityOfLoss