'''
Created on 24 Nov 2013

@author: wrightm
'''

class Helpers(object):
    '''
    General Helper Methods
    '''

    @staticmethod
    def sumWrapper(items):
        
        if len(items) < 1:
            return 0.0
        
        if isinstance(items[0], (int, long, float, complex)):
            return sum(items)
        else:
            ticker = items[0]
            for tick in items[1:]:
                ticker += tick
            return ticker
    
    @staticmethod
    def divideWrapper(obj1, obj2):

        try:
            return obj1 / obj2
        except ZeroDivisionError:
            return 0.0
        
    @staticmethod
    def floorDivideWrapper(obj1, obj2):

        try:
            return obj1 // obj2
        except ZeroDivisionError:
            return 0.0
    
        