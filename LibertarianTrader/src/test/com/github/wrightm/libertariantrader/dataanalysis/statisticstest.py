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
        
    def testZScore(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        zscores = Stats.zscores(items)
        self.assertEqual(len(zscores), len(items))
        
    def testTrimmed(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        trimmed = Stats.trimmed(items, percentage=0.1, sortLambda=lambda item: item)
        
        self.assertEqual(trimmed, [2,4,5,6,7,8,9])
        
    def testMad(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        mad = Stats.mad(items)
        self.assertAlmostEqual(mad, 2.47, 2)
        
    def testMin(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        min = Stats.min(items)
        self.assertEqual(min, 1)
        
    def testMax(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        max = Stats.max(items)
        self.assertEqual(max, 10)
        
    def testRange(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        range = Stats.range(items)
        self.assertEqual(range, 9)
        
    def testKurtosis(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        kurtosis = Stats.kurtosis(items)
        self.assertAlmostEqual(kurtosis, -0.89, 2) 
    
    def testSkewness(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        skewness = Stats.skewness(items)
        self.assertAlmostEqual(skewness, 2.11, 2)
        
    def testStandardError(self):
        
        items=[1,2,4,5,6,7,8,9,10]
        standardError = Stats.standardError(items)
        self.assertAlmostEqual(standardError, 0.97, 2)
        
    def testCovariance(self):
    
        cov = Stats.covariance(10, 5, 10, 5, 25)
        self.assertEqual(cov, 1.0)
        
    def testCovarianceFromSet(self):

        setOne = [10,10,10,10,10]
        setTwo = [10,10,10,10,10]
        cov = Stats.covarianceFromSets(setOne, setTwo, 5, 5)
        self.assertEqual(cov, 25.0)
        
    def testCorrelation(self):
        
        cor = Stats.correlation(10, 5, 1, 10, 5, 1, 5)
        self.assertEqual(cor, 5)
        
    def testCorrelationFromSet(self):
        
        setOne = [10,10,10,10,10]
        setTwo = [10,10,10,10,10]
        cov = Stats.correlationFromSets(setOne, setTwo, 5, 1, 5, 1)
        self.assertEqual(cov, 25.0)
        

if __name__ == "__main__":
    unittest.main()