'''
Created on 15 Nov 2013

@author: wrightm
'''
import unittest
import matplotlib
from src.main.com.github.wrightm.libertariantrader.datacollection.tickerfile import TickerFile
from src.main.com.github.wrightm.libertariantrader.datacollection.tickers import Tickers
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.figuresettings import FigureSettings
from src.main.com.github.wrightm.libertariantrader.datavisualisation.plots.stockplots import CandleSticks
import datetime
from matplotlib import animation


class ExampleTest(unittest.TestCase):


    def Pendulum(self):
        matplotlib.use('TKAgg')
        from numpy import sin, cos, pi, array
        import numpy as np
        import matplotlib.pyplot as plt
        import scipy.integrate as integrate
        import matplotlib.animation as animation
        G =  9.8 # acceleration due to gravity, in m/s^2
        L1 = 1.0 # length of pendulum 1 in m
        L2 = 1.0 # length of pendulum 2 in m
        M1 = 1.0 # mass of pendulum 1 in kg
        M2 = 1.0 # mass of pendulum 2 in kg


        def derivs(state, t):

            dydx = np.zeros_like(state)
            dydx[0] = state[1]

            del_ = state[2]-state[0]
            den1 = (M1+M2)*L1 - M2*L1*cos(del_)*cos(del_)
            dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_)
                       + M2*G*sin(state[2])*cos(del_) + M2*L2*state[3]*state[3]*sin(del_)
                       - (M1+M2)*G*sin(state[0]))/den1

            dydx[2] = state[3]

            den2 = (L2/L1)*den1
            dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_)
                       + (M1+M2)*G*sin(state[0])*cos(del_)
                       - (M1+M2)*L1*state[1]*state[1]*sin(del_)
                       - (M1+M2)*G*sin(state[2]))/den2

            return dydx

        # create a time array from 0..100 sampled at 0.1 second steps
        dt = 0.05
        t = np.arange(0.0, 20, dt)

        # th1 and th2 are the initial angles (degrees)
        # w10 and w20 are the initial angular velocities (degrees per second)
        th1 = 120.0
        w1 = 0.0
        th2 = -10.0
        w2 = 0.0

        rad = pi/180

        # initial state
        state = np.array([th1, w1, th2, w2])*pi/180.

        # integrate your ODE using scipy.integrate.
        y = integrate.odeint(derivs, state, t)

        x1 = L1*sin(y[:,0])
        y1 = -L1*cos(y[:,0])

        x2 = L2*sin(y[:,2]) + x1
        y2 = -L2*cos(y[:,2]) + y1

        fig = plt.figure()
        ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
        ax.grid()

        line, = ax.plot([], [], 'o-', lw=2)
        time_template = 'time = %.1fs'
        time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

        def init():
            line.set_data([], [])
            time_text.set_text('')
            return line, time_text

        def animate(i):
            thisx = [0, x1[i], x2[i]]
            thisy = [0, y1[i], y2[i]]

            line.set_data(thisx, thisy)
            time_text.set_text(time_template%(i*dt))
            return line, time_text

        ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
        interval=25, blit=True, init_func=init)

        #ani.save('double_pendulum.mp4', fps=15, clear_temp=True)
        plt.show()
        
        
    def CandleSticks(self):
        
        
        tickerFile = TickerFile('/Volumes/MichaelWright1/Dropbox/Projects/LibertarianTrader/LibertarianTrader/resources/testTickersJSONDump.json')
        tickers = tickerFile.load()
            
        tickersBefore = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() <= datetime.date(2012, 9, 10) and ticker.getDate().date() > datetime.date(2008, 9, 10), tickers)
        tickersAfter = filter(lambda ticker: ticker.getName() == 'GOOG' and ticker.getDate().date() > datetime.date(2012, 9, 10), tickers)
        tickersAfter = sorted(tickersAfter, key=lambda ticker: ticker.getDate())
        tickersBefore = Tickers(tickersBefore)
        tickersAfter = Tickers(tickersAfter)
        
        figureSetting = FigureSettings()
        candlesticks = CandleSticks(tickersBefore, figureSetting)
        
        class Counter(object):
            
            def __init__(self, start=0):
                self.start = start
                
            def incr(self):
                self.start += 1
            
            def get(self):
                return self.start
        
        n = Counter()
        def addTicker(*args):
            tickers = args[1]
            candlesticks = args[3]
            if n.get() < len(tickers) :
                print tickers[n.get()].getDate()
                candlesticks.addTicker(tickers[n.get()])
                candlesticks.getCandleAxis().autoscale_view()
                candlesticks.getVolumeAxis().autoscale_view()
                n.incr()

        ani = animation.FuncAnimation(candlesticks.getFigure(), addTicker, fargs=[tickersAfter, n, candlesticks], interval=1000)
        
        candlesticks.show()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()