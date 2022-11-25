# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:26:15 2022

@author: Ilya
"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    y = 0
    res = b ** y
    while res < x:
        y += 1
        res = b ** y
    
    if res > x:
        return y - 1
    else:
        return y