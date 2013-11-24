'''
Created on 20 Nov 2013

@author: wrightm
'''
from src.main.com.github.wrightm.libertariantrader.datacollection.ticker import Ticker

class DataProcessing(object):
    '''
    Methods for mainpulating and validating objects, file, etc
    '''

    @staticmethod
    def checkSetsAreEqualInLength(firstSet, secondSet):
        
        firstSetLength = len(firstSet)
        secondSetLength = len(secondSet)
        
        if firstSet > secondSet:
            firstSet = firstSet[:secondSetLength]
        elif firstSet < secondSet:
            secondSet = secondSet[:firstSetLength]
            
        return firstSet, secondSet
