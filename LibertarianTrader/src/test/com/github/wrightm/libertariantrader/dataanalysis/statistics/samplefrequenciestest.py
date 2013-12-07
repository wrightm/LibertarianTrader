'''
Created on 17 Oct 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.dataanalysis.statistics.samplefrequencies import SampleFrequencies

class SampleFrequenciesTest(unittest.TestCase):


    def testSetGet(self):
        
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        self.assertEquals(sampleFrequencies.get('SAM'),4,"There is not 4 Sam's")
        self.assertEquals(sampleFrequencies.get('JOHN'),2,"There is not 2 John's")
        self.assertEquals(sampleFrequencies.get('JOE'),1,"There is not 1 Joe")
        
        
    def testGetItems(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        self.assertEqual(sampleFrequencies.getItems(), ['JOHN', 'JOE', 'SAM'], "getItems does not equal ['JOHN', 'JOE', 'SAM']") 
    
    def testGetFrequencies(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')

        self.assertEqual(sampleFrequencies.getFrequencies(), [2, 1, 4], "getFrequencies does not equal [2, 1, 4]") 
        
    def testGetPairs(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')

        self.assertEqual(sampleFrequencies.getPairs(), [('JOHN', 2), ('JOE', 1), ('SAM', 4)], "getFrequencies does not equal [('JOHN', 2), ('JOE', 1), ('SAM', 4)]") 
    
    def testIterPairs(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        pairListTest = []
        for item, frequency in sampleFrequencies.iterPairs():
            pairListTest.append((item, frequency))
        
        self.assertEqual(pairListTest, [('JOHN', 2), ('JOE', 1), ('SAM', 4)], "pairListTest does not equal [('JOHN', 2), ('JOE', 1), ('SAM', 4)]")     
        
    def testIterItems(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        itemListTest = []
        for item in sampleFrequencies.iterItems():
            itemListTest.append(item)
        
        self.assertEqual(itemListTest, ['JOHN', 'JOE', 'SAM'], "itemListTest does not equal ['JOHN', 'JOE', 'SAM']")     
        
    def testIterFrequencies(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        frequencyListTest = []
        for frequency in sampleFrequencies.iterFrquencies():
            frequencyListTest.append(frequency)
        
        self.assertEqual(frequencyListTest, [2, 1, 4], "frequencyListTest does not equal [2, 1, 4]")     
    
    def testCopy(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        frequencyCopy = sampleFrequencies.copy()
        
        self.assertEqual(sampleFrequencies, frequencyCopy, "copy method is not equal to original object")
        
    def testHasKey(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        self.assertEqual(sampleFrequencies.hasKey('SAM'), True, 'SAM does not exist in Frequencies object')
    
    def testPopWithoutFrequency(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        self.assertEqual(sampleFrequencies.pop('SAM'),  4, 'SAM item frequency is not 4')
        
    def testPop(self):
        
        sampleFrequencies = SampleFrequencies()
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('SAM')
        sampleFrequencies.set('JOHN')
        sampleFrequencies.set('JOE')
        sampleFrequencies.set('JOHN')
        
        self.assertEqual(sampleFrequencies.pop(),  ('JOHN',2), '(JOHN,2) does not exist')
        
if __name__ == "__main__":
    unittest.main()