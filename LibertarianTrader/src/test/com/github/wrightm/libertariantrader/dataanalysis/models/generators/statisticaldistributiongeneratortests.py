'''
Created on 20 Nov 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.dataanalysis.models.generators.statisticaldistributiongenerator import Guassian
from matplotlib import pyplot


class StatisticalDistributionGeneratorTest(unittest.TestCase):


    def testGussian(self):
        
        guassainDistribution = Guassian(50, 50, 0.0, 100.0, 1000)
        
        x, y = zip(*sorted(guassainDistribution.getPDF().items()))
        pyplot.plot(x, y)
        x, y = zip(*sorted(guassainDistribution.getCDF().items()))
        pyplot.plot(x, y)
        #pyplot.savefig('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/plots/test/testGuassianGenerator.png', format='png', dpi=300)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()