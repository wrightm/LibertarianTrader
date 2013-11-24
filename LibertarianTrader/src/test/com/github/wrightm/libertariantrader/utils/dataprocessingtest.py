'''
Created on 24 Nov 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.utils.dataprocessing import DataProcessing


class DataProcessingTest(unittest.TestCase):


    def testCheckSetsAreEqualInLength(self):

        firstSet = [1,2,3,4,5,6,7,8,9,10]
        secondSet = [1,2,3,4,5]
        
        first, second = DataProcessing.checkSetsAreEqualInLength(firstSet, secondSet)

        self.assertEqual(first, second)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()