'''
Candlestick plot of tickers
@author: wrightm
'''
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers

import matplotlib.pyplot as plt
from matplotlib.dates import  DateFormatter, DayLocator, date2num
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib import pyplot
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.figuresettings import FigureSettings
     
class CandleSticks(object):
    '''
        Candlestick plot of tickers
    '''


    def __init__(self, tickers, figureSettings):
        '''
        Plot the time, open, high, low, close as a vertical line ranging
        from low to high. Use a rectangular bar to represent the
        open-close span. If close >= open, use colorup to color the bar,
        otherwise use colordown
        
        Parameters
        ----------
        @param tickers: Tickers
        holds ticker information for n tickers
        @param figureSettings: FigureSettings
        settings for plot
        
        Exceptions
        ----------
        @raise TypeError: when tickers is not of type Tickers or figureSettings is not of type FigureSettings
        '''
        if not isinstance(tickers, Tickers):
            raise TypeError("tickers is not of type Tickers")
        
        if not isinstance(figureSettings, FigureSettings):
            raise TypeError("figureSettings is not of type FigureSettings")
        
        self.__tickers = tickers
        self.__setTitle = figureSettings.get('title', '')
        self.__setXTitle = figureSettings.get('xlabel', '')
        self.__setYTitle = figureSettings.get('ylabel', '')
        self.__grid = figureSettings.get('grid', True)
        self.__candleWidth = figureSettings.get('candleWidth', 0.6)
        self.__colorup = figureSettings.get('colorup', 'k') 
        self.__colordown = figureSettings.get('colordown', 'r')
        self.__alpha = figureSettings.get('alpha', 1.0)
        self.__offset = self.__candleWidth / 2.0
        self.__setupfigureSettings() 
        self.__setupTickerAndVolume()
        
    def __setupfigureSettings(self):
        '''
        Initialise plots and setup plot settings
        '''
        self.__fig, (self.__axCandle, self.__axVolume) = plt.subplots(nrows=2, ncols=1, sharex=True, facecolor='w' )
        self.__fig.subplots_adjust(bottom=0.2)
        
        self.__axCandle.set_title(self.__setTitle)
        self.__axCandle.set_ylabel(self.__setYTitle)
        self.__axCandle.xaxis.set_minor_locator(DayLocator())
        self.__axCandle.xaxis.set_major_formatter( DateFormatter('%b %d %Y'))
        self.__axCandle.grid(self.__grid)
        
        self.__axVolume.set_xlabel(self.__setXTitle)
        self.__axVolume.set_ylabel('volume')
        self.__axVolume.xaxis.set_minor_locator(DayLocator())
        self.__axVolume.xaxis.set_major_formatter( DateFormatter('%b %d %Y'))
        
        
    def __setupTickerAndVolume(self):

        '''
            construct and fill tickers/volume into plots
        '''

        for ticker in self.__tickers:
            self.addTicker(ticker)
            
    def addTicker(self, ticker):
        
        t = date2num(ticker.getDate())
        open = ticker.getOpen()
        close = ticker.getAdjustedClose()
        high = ticker.getHigh()
        low = ticker.getLow()
        volume = ticker.getVolume()
             
        if close >= open:
            color = self.__colorup
            lower = open
            height = close - open
        else:
            color = self.__colordown
            lower = close
            height = open - close

        vline = Line2D(
                       xdata=(t, t), ydata=(low, high),
                       color='k',
                       linewidth=1,
                       antialiased=True,
                       )

        rectTicker = Rectangle(
                               xy=(t - self.__offset, lower),
                               width = self.__candleWidth,
                               height = height,
                               facecolor = color,
                               edgecolor = color,
                               )
            
        rectTicker.set_alpha(self.__alpha)

        rectVolume = Rectangle(
                               xy=(t - self.__offset, 0),
                               width = self.__candleWidth,
                               height = volume,
                               facecolor = color,
                               edgecolor = color,
                               )

        self.__axCandle.add_line(vline)
        self.__axCandle.add_patch(rectTicker)
        self.__axVolume.add_patch(rectVolume)
        
        
    def __isFilenameValid(self, filename):
        '''
            check filename is valid
            
            
            Return
            -------
            @return: boolean
            true if filename is valid, false if filename is not valid
            
            Exceptions
            ----------
            @raise ValueError: when file is not of supported type
        '''
        splitFilename = filename.split('.')
        fileType = splitFilename[len(splitFilename)-1]
        
        allowedFileTypes = ['png', 'pdf', 'ps', 'eps', 'svg']
        
        if fileType in allowedFileTypes:
            return True
        return False
        
    def show(self):
        '''
            draw plot to screen
        '''
        self.__axCandle.xaxis_date()
        self.__axVolume.xaxis_date()
        self.__axCandle.autoscale_view()
        self.__axVolume.autoscale_view()
        plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()
        
    def save(self, filename):
        '''
            write plot image to a file
            
            Parameters
            ----------
            
            @param filename: name of file to save
            
            
            Exceptions
            ----------
            @raise ValueError: when file is not of supported type
        '''
        if not self.__isFilenameValid(filename):
            raise ValueError("filename is not in list of support file types. current support for png', 'pdf', 'ps', 'eps', 'svg'")
        
        self.__axCandle.xaxis_date()
        self.__axVolume.xaxis_date()
        self.__axCandle.autoscale_view()
        self.__axVolume.autoscale_view()
        plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.savefig(filename)
        
    def getFigure(self):
        return self.__fig
    
    def getCandleAxis(self):
        return self.__axCandle

    def getVolumeAxis(self):
        return self.__axVolume
        
class Plot(object):
    '''
        Plot variable
    '''


    def __init__(self, plottingMethod, sample, figureSettings, *pairMethodArgs, **pairMethodKargs):
        '''
        Uses the LibertarianTrader object method getPairs to produce a plot using a pyplot plotting attribute
        
        Parameters
        ----------
        @param plottingMethod: string
        name of pyplot attribute 
        @param sample: object
        sample with variable and frequencies
        @param figureSettings: FigureSettings
        settings for plot
        @param pairMehtodArgs: list
        list of arguments for the getPair Method
        @param pairMethodKargs: dictionary
        dictionary of key=value arguments for the getPair Method
        
        Exceptions
        ----------
        @raise TypeError: figureSettings is not of type FigureSettings
        @raise AttributeError: if sample does not have attr getPairs
        '''
        if not isinstance(figureSettings, FigureSettings):
            raise TypeError("figureSettings is not of type FigureSettings")
        
        if not hasattr(sample, 'getPairs'):
            raise AttributeError('sample does not have attribute getPairs')
        
        self.__plottingMethod = plottingMethod
        self.__sample = sample    
        self.__figureSettings = figureSettings
        self.__pairMethodArgs = pairMethodArgs
        self.__pairMethodKargs = pairMethodKargs
        
    def setup(self):
        """
        Setup plot and return figure and axis for further formatting if needed
        
        Return:
        -------
        @return: 
        return figure and axis for further formatting if needed
        """
        fig = pyplot.figure()
        ax  = fig.gca(xlabel=self.__figureSettings.remove('xlabel'), ylabel=self.__figureSettings.remove('ylabel'))
        fig.set_facecolor('white')
        pyplot.grid(True)
        
        xs, ps = zip(*sorted(self.__sample.getPairs(*self.__pairMethodArgs, **self.__pairMethodKargs)))
        try:
            plot = getattr(ax, self.__plottingMethod)
            plot(xs, ps,**self.__figureSettings.getSettings())
        except AttributeError as error:
            print "Warning attribute %s was not found. Using pyplot.plot method. Error msg: %s" % (self.__plottingMethod, error)
            pyplot.plot(xs, ps, **self.__figureSettings.getSettings())
        return fig, ax
    
    def save(self, root=None, formats=None):
        """
        Saves the plot in the given formats.

        Parameters:
        ----------
          @param root: string filename root
          @param formats: list of string formats
        """

        if formats is None:
            formats = ['pdf', 'png']

        if root:
            for format in formats:
                self.saveFormat(root, format)


    def saveFormat(self, root, format='eps'):
        """Writes the current figure to a file in the given format.

        Parameters:
        ----------
          @param root: string filename root
          @param format: string format
        """
        filename = '%s.%s' % (root, format)
        print 'Writing', filename
        pyplot.autoscale()
        pyplot.savefig(filename, format=format, dpi=300)
    
    def show(self):
        """
        draw plot in screen
        used for quick review of plot
        """
        pyplot.autoscale()
        pyplot.show()
