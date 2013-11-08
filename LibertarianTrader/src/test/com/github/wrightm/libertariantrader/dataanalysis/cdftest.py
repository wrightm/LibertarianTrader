'''
Created on 28 Oct 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.dataanalysis.samplefrequencies import SampleFrequencies
from src.main.com.github.wrightm.libertariantrader.dataanalysis.cdf import CDF


class CDFTest(unittest.TestCase):


    def testValue(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertEqual(cdf.getValue(0.9), 3, '0.9 did not return a value of 3')

    def testProbability(self):
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertAlmostEqual(cdf.getProbability(3), 0.92, 2, '3 did not return a probability of 0.92')

    def testMean(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertAlmostEqual(cdf.getMean(), 3.74, 2, 'cdf mean does not equal 3.74')

    def testVar(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertAlmostEqual(cdf.getVar(), 3.73, 2, 'cdf variance does not equal 3.73')

    def testStdDev(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertAlmostEqual(cdf.getStdDev(), 1.93, 2, 'cdf standard deviation does not equal 1.93')

    def testSample(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertEqual(len(cdf.getSample(38)), 38, 'sample size is not 38')
        
    def testRandomValue(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        values = [1,2,3,4]
        assert cdf.getRandomValue() in values
        
    def testPercentile(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertEqual(cdf.getPercentile(90), 3, 'cdf 90th percentile doesnt = 3')

    def testPairs(self):
        
        sample = {1:10,
                  2:5,
                  3:20,
                  4:3 }
        sampleFrequency = SampleFrequencies(sample)
        cdf = CDF(sampleFrequency)
        self.assertEqual(len(cdf.getPairs()), 4, 'cdf pair size is not equal to 4')   

if __name__ == "__main__":
    unittest.main()