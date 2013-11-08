'''
Created on 16 Oct 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.dataanalysis.statistics import Stats


class StatsTest(unittest.TestCase):


    def testMean(self):
        
        ls=[1,2,4,5,6,7,8,9,10]
        
        mu = Stats.mean(ls)
        self.assertAlmostEqual(mu, 5.777, 2, 'mean does not equal 5.77 to 2 decimal places')
    
    def testVar(self):

        var=[1,2,4,5,6,7,8,9,10]
        
        var = Stats.var(var)
        self.assertAlmostEqual(var, 8.395, 2, 'var does not equal 8.39 to 2 decimal places')
    
    def testStdev(self):
        
        stdev=[1,2,4,5,6,7,8,9,10]
        
        stdev = Stats.stdev(stdev)
        self.assertAlmostEqual(stdev, 2.897, 2, 'stdev does not equal 2.89 to 2 decimal places')
        
        
if __name__ == "__main__":
    unittest.main()