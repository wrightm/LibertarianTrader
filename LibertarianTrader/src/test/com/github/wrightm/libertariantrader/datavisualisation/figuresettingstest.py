'''
Created on 25 Oct 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.datavisualisation.figuresettings import FigureSettings


class FigureSettingsTest(unittest.TestCase):


    def testSettingsLength(self):

        settings = {'title': 'example title', 'xaxis': 'date', 'yaxis': 'stock price'}
        figureSettings = FigureSettings(settings)
        self.assertEqual(len(figureSettings),3,'number of figure settings does not equal 3')

    def testSettingsGet(self):

        settings = {'title': 'example title', 'xaxis': 'date', 'yaxis': 'stock price'}
        figureSettings = FigureSettings(settings)
        self.assertEqual(figureSettings['title'], 'example title', 'title settings does not equal "example title"')
    
    def testSettingsSet(self):
        
        figureSettings = FigureSettings()
        figureSettings['title'] = 'example title'
        self.assertEqual(figureSettings['title'], 'example title', 'title settings does not equal "example title"')
    
    def testSettingsIteritems(self):
        
        settings = {'title': 'example title', 'xaxis': 'date', 'yaxis': 'stock price'}
        figureSettings = FigureSettings(settings)
        duplicateSettings = {}
        for setting, value in figureSettings.iteritems():
            duplicateSettings[setting] = value 
        self.assertEqual(settings, duplicateSettings, 'duplicate settings does not equal original settings')
        
    
    def testSettingsRemove(self):
        
        settings = {'title': 'example title', 'xaxis': 'date', 'yaxis': 'stock price'}
        figureSettings = FigureSettings(settings)
        figureSettings.remove('title')
        otherSettings = {'xaxis': 'date', 'yaxis': 'stock price'}
        self.assertEqual(otherSettings, {'xaxis': 'date', 'yaxis': 'stock price'}, "settings does not equal {'xaxis': 'date', 'yaxis': 'stock price'}")
        
    
    def testSettingsGetSettings(self):
        
        settings = {'title': 'example title', 'xaxis': 'date', 'yaxis': 'stock price'}
        figureSettings = FigureSettings(settings)
        self.assertEqual(figureSettings.getSettings(), settings, 'getSettings does not equal settings')
    
    def testSettingsGetDefualtSetting(self):
        
        settings = {'title': 'example title', 'xaxis': 'date', 'yaxis': 'stock price'}
        figureSettings = FigureSettings(settings)
        self.assertEqual(figureSettings.get('title'), 'example title', 'title settings does not equal "example title"')
    
    
if __name__ == "__main__":
    unittest.main()