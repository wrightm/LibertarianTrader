'''
Created on 21 Oct 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.dataanalysis.samplefrequencies import SampleFrequencies
from src.main.com.github.wrightm.libertariantrader.dataanalysis import pmf
from src.main.com.github.wrightm.libertariantrader.dataanalysis.pmf import biasPmf, Bias,\
    unBiasPmf
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.figuresettings import FigureSettings
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.stockplots import Plot

class BiasTest(Bias):
    
    def __init__(self, value):
        Bias.__init__(value)
        self.value = value
        
    def __call__(self):
        return 10;

class PmfTest(unittest.TestCase):

    def testGet(self):
         
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        prob_m_f =  pmf.Pmf(frequencies) 

        self.assertEqual(prob_m_f.get(1), 0.25, "probability does not equal 0.25 for item 1")
        
    def testGetItems(self):
         
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        
        self.assertEqual(p_m_f.getItems(), [1, 2, 4, 5, 6, 7, 8, 9, 10], "items does not [1, 2, 4, 5, 6, 7, 8, 9, 10]")
         
    def testGetProbabilities(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        
        self.assertEqual(p_m_f.getProbabilities(), [0.25, 0.1875, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.125, 0.125], 'probabilities do not equal [0.25, 0.1875, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.125, 0.125]')
        
    def testGetPairs(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        
        self.assertEqual(p_m_f.getPairs(), [(1, 0.25), (2, 0.1875), (4, 0.0625), (5, 0.0625), (6, 0.0625), (7, 0.0625), (8, 0.0625), (9, 0.125), (10, 0.125)], 'pairs do nto equal [(1, 0.25), (2, 0.1875), (4, 0.0625), (5, 0.0625), (6, 0.0625), (7, 0.0625), (8, 0.0625), (9, 0.125), (10, 0.125)]')
        
    def testIterPairs(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        
        testPairs = []
        for k, v in p_m_f.iterPairs():
            testPairs.append((k,v))
            
        self.assertEqual(testPairs, p_m_f.getPairs(), 'iterPairs does not produce original pairs')
            
    def testIterItems(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        
        testItems = []
        for item in p_m_f.iterItems():
            testItems.append(item)
            
        self.assertEqual(testItems, p_m_f.getItems(), 'iterItems does not produce original items')
            
    def testIterProbabilities(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        
        testProbs = []
        for item in p_m_f.iterProbabilities():
            testProbs.append(item)
        
        self.assertEqual(testProbs, p_m_f.getProbabilities(), 'iterProbabilities does not produce original Probabilities')

    def testMean(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        self.assertEqual(p_m_f.getMean(), 4.875, 'mean does not equal 4.875')
        
    def testVariance(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        self.assertEqual(p_m_f.getVariance(), 11.734375, 'variance does not equal 11.734375')
        

    def testStdev(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        self.assertAlmostEqual(p_m_f.getStDev(), 3.425, 2, 'stdev does not equal 3.42554740151')
    
    def testBiasedPmf(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        biasedPmf = biasPmf(p_m_f, BiasTest)
        
        self.assertAlmostEqual(biasedPmf.getStDev(), 3.425, 2, 'stdev does not equal 3.42554740151')
        
    def testUnBiasedPmf(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        biasedPmf = biasPmf(p_m_f, BiasTest)
        unbiasedPmf = unBiasPmf(biasedPmf, BiasTest)
        self.assertAlmostEqual(unbiasedPmf.getStDev(), 3.425, 2, 'stdev does not equal 3.42554740151')
    
    def testPlot(self):    
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies)
        
        figureSettings = FigureSettings()
        figureSettings['xlabel'] = "values"
        figureSettings['ylabel'] = "probability"
        plot = Plot("plot", p_m_f, figureSettings)
        fig, ax = plot.setup()
        plot.save("/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/plots/test/pmfTest")

        
    def testPmfLogPlot(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies, logTransform=True)
        
        figureSettings = FigureSettings()
        figureSettings['xlabel'] = "values"
        figureSettings['ylabel'] = "probability"
        plot = Plot("plot", p_m_f, figureSettings)
        fig, ax = plot.setup()
        plot.save("/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/plots/test/pmfLogTest")

    
    
    def testPmfExpPlot(self):
        
        frequencies = SampleFrequencies()
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(1)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(2)
        frequencies.set(4)
        frequencies.set(5)
        frequencies.set(6)
        frequencies.set(7)
        frequencies.set(8)
        frequencies.set(9)
        frequencies.set(9)
        frequencies.set(10)
        frequencies.set(10)
        
        p_m_f =  pmf.Pmf(frequencies, expoTransform=True)
        
        figureSettings = FigureSettings()
        figureSettings['xlabel'] = "values"
        figureSettings['ylabel'] = "probability"
        plot = Plot("plot", p_m_f, figureSettings)
        fig, ax = plot.setup()
        plot.save("/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/plots/test/pmfExpTest")

        
        
        
        
        
if __name__ == "__main__":
    unittest.main()