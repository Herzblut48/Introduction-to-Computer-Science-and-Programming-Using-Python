# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 23:21:20 2022

@author: Ilya
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def poly_funct(x):
        L.reverse()
        res = 0
        for i in range(len(L)):
            res += L[i] * x**i
        return res
    
    return poly_funct