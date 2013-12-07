'''
Created on 29 Nov 2013

@author: wrightm
'''
import unittest
from src.main.com.github.wrightm.libertariantrader.utils.dataprocessing import DataProcessing
from matplotlib import pyplot
import numpy
import scipy.interpolate
import scipy.optimize
import scipy.special
from src.main.com.github.wrightm.libertariantrader.datacollection.tickerfile import TickerFile
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.figuresettings import FigureSettings
import datetime
from src.main.com.github.wrightm.libertariantrader.utils.generalhelpers import Helpers
from src.main.com.github.wrightm.libertariantrader.dataanalysis.statistics.helpermethods import Stats


class LeastSquaresTest(unittest.TestCase):


    def testLinearModelOneDimension(self):
        
        X = [1.0,3.0,4.0,6.0,8.0,9.0,11.0,14.0]
        Y = [1.0,2.0,4.0,4.0,5.0,7.0,8.0,9.0]
        Y, X = DataProcessing.checkSetsAreEqualInLength(Y,X)
        numberOfElements = len(Y)
        sumX  = Helpers.sumWrapper(X)
        sumXSquared = Helpers.sumWrapper(map(lambda xi: xi**2, X))
        squaredSumX = sumX**2
        sumY  = Helpers.sumWrapper(Y)
        sumXY = Helpers.sumWrapper(map( lambda pair: pair[0]*pair[1], zip(Y,X) ))

        def a1(Y, X):
            
            numerator = (numberOfElements*sumXY) - (sumX*sumY)
            denominator = (numberOfElements*sumXSquared) - squaredSumX 
            return numerator / denominator
        
        def a0(Y, X):

            numerator = (sumY*sumXSquared) - (sumX*sumXY) 
            denominator = (numberOfElements*sumXSquared) - (squaredSumX)
            return numerator / denominator
        
        def model(X, _a0, _a1):
            
            return map(lambda xi: (_a0 + _a1*xi), X)
        
        _a0 = a0(Y, X)
        _a1 = a1(Y, X)
        
        # simple linear model y = ao + a1X
        _model = model(X, _a0, _a1)
        # polynomial of 5 degrees
        # y = a0 + a1X + a2X^2 + a3X^3 + a4X^4 + a5X^5
        line, residual,_,_,_  = numpy.polyfit(X, Y, deg=5, full=True)
        polyValues = numpy.polyval(line, X)
        # splines
        spline = scipy.interpolate.UnivariateSpline(X, Y, k=4)
        splineModel = spline(X)
        # curve fit
        target_function = lambda x, a0, a1, a2, a3, a4: a0+(a1*x)+(a2*(numpy.power(x,2))) + (a3*(numpy.power(x,3))) + (a4*(numpy.power(x,4))) 
        pF, pVar = scipy.optimize.curve_fit(target_function, X, Y)
        curveFitModel = [target_function(x, pF[0], pF[1], pF[2], pF[3], pF[4]) for x in X]
        
        residualMyModel = []
        residualRatioMyModel = []
        for rec, actual in zip(sorted(_model), sorted(Y)):
            residualMyModel.append((rec-actual)**2)
            residualRatioMyModel.append(abs(rec-actual)/actual)
        
        residualSciPiModel = []
        for rec, actual in zip(sorted(polyValues), sorted(Y)):
            residualSciPiModel.append((rec-actual)**2)
        
        pyplot.scatter(sorted(X),sorted(Y))
        pyplot.plot(sorted(X),sorted(_model))
        #pyplot.plot(sorted(X),sorted(polyValues))
        #pyplot.plot(sorted(X),sorted(splineModel))
        #pyplot.plot(sorted(X),sorted(curveFitModel))
        #pyplot.plot(sorted(X),residualSciPiModel)
        #pyplot.show()
            
    def testSinModelOneDimension(self):
        
        x = numpy.linspace(0, 1, 100)
        amplitude = 18
        frequency = 2
        angularFrequency = 2*numpy.pi * frequency
        phase = 0.5
        time = 2;
        y = amplitude*numpy.sin(angularFrequency*x + phase)
        target_function = lambda xi, AA, ww, hh: AA*numpy.sin(ww*xi+hh)
        
        # need to guess parameters not very good
        pF, pVar = scipy.optimize.curve_fit(target_function, x, y, [16,11,0.5])
        
        line, residual,_,_,_  = numpy.polyfit(x, y, deg=5, full=True)
        
        spline = scipy.interpolate.UnivariateSpline(x, y, k=2)

        # generate models
        x = numpy.append(x, [1.1, 1.2])
        y = amplitude*numpy.sin(angularFrequency*x + phase)
        model1 = [ target_function(xi, pF[0], pF[1], pF[2]) for xi in x]
        model2 = numpy.polyval(line, x)
        splineModel = spline(x)
        '''
        pyplot.ylim((-20,20))
        pyplot.scatter(x,y)
        pyplot.plot(x,model1)
        pyplot.plot(x,model2)
        pyplot.plot(x,splineModel)
        pyplot.show()
        '''
        
    def testStockDataFit(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = sorted(filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2011, 9, 10), tickers), key=lambda tick: tick.getDate()) 
        tickers = Tickers(tickers)
        
        price = []
        low = []
        high = []
        id = []
        volume = []
        for indx, tick in enumerate(tickers):
            price.append(float(tick.getAdjustedClose()))
            low.append(tick.getLow())
            high.append(tick.getHigh())
            id.append(indx)
            volume.append(float(tick.getVolume()))
        
        
        line, residual,_,_,_  = numpy.polyfit(id[:-2], price[:-2], deg=5, full=True)
        
        targetFunction = lambda x, gradient, intercept: (gradient*x**2) + intercept
        pVal, pCor = scipy.optimize.curve_fit(targetFunction, numpy.array(id), numpy.array(price))
        
        polyValues = numpy.polyval(line, id)
        # splines
        spline = scipy.interpolate.UnivariateSpline(id[:-2], price[:-2], k=2)
        splineModel = spline(id)
        
        #pyplot.plot(id,price)
        #pyplot.plot(id,polyValues)
        #pyplot.plot(id,[targetFunction(i, pVal[0], pVal[1]) for i in id])
        #pyplot.plot(id,polyValuesHigh)
        #pyplot.show()
        
    def testChiSquaredOfFit(self):
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickers = sorted(filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() >= datetime.date(2011, 9, 10), tickers), key=lambda tick: tick.getDate()) 
        tickers = Tickers(tickers)
        
        price = []
        low = []
        high = []
        id = []
        volume = []
        for indx, tick in enumerate(tickers):
            price.append(float(tick.getAdjustedClose()))
            low.append(tick.getLow())
            high.append(tick.getHigh())
            id.append(indx)
            volume.append(float(tick.getVolume()))
        
        
        targetFunction = lambda x, gradient, intercept: (gradient*x**2) + intercept
        pVal, cov = scipy.optimize.curve_fit(targetFunction, numpy.array(id), numpy.array(price))
        
        dof = len(id) - len(pVal)
        
        sigmaPrice = Stats.stdev(price)
        chiSquared =  sum( [ ((price[indx] - targetFunction(x, *pVal))/sigmaPrice)**2 for indx, x in enumerate(id)])
        chiSquared
        
        cov = cov*dof/chiSquared
        for i,row in enumerate(cov):
            for j in xrange(len(pVal)) :
                cor = (cov[i,j]/numpy.sqrt(cov[i,i]*cov[j,j]))

        ### Only for guassian approximation
        '''
        print chiSquared
        cdf = scipy.special.chdtrc(dof,chiSquared)
        print "\nChi-Squared/dof = %10.5f, CDF = %10.5f%%"\
            %(chiSquared/dof, 100.*cdf)
        if cdf < 0.05 :
            print "\nNOTE: This does not appear to be a great fit, so the"
            print "      parameter uncertainties may underestimated."
        elif cdf > 0.95 :
            print "\nNOTE: This fit seems better than expected, so the"
            print "      data uncertainties may have been overestimated."
        ''' 
        #pyplot.plot(id,price)
        #pyplot.plot(id,[targetFunction(i, *pVal) for i in id])
        #pyplot.show()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()