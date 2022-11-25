# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    summed = 1
    prev = 1
    while summed <= k:
        prev += 1
        res = summed
        summed = summed + prev
    
    return res == k

print(is_triangular(6))