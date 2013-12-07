'''
Created on 4 Dec 2013

@author: wrightm
'''

class Fit(object):
    '''
    fit function to data.
    
    While calculate best fit for a given function.
    
    Return:
    -------
    * ceofficients of Model
    * y-model for given xdata
    * y-data
    * x-data
    * Residuals (model - data)**2
    * Sum of Residuals E(model - data)**2
    * Ratio Of Differences (model - data)/data
    * Sum of Ratio OF Differences E((model - data)/data)
    * Average Ratio OF Differences E((model - data)/data)/N
    '''


    def __init__(self, xData, yData, targetFunction=None, polyDegree=None, *guess):
        '''
        Initialise class
        
        Parameters:
        -----------
        
        @param xData: list of floats
        independent variable values
        @param yData: list of floats
        dependent variable values
        '''
        