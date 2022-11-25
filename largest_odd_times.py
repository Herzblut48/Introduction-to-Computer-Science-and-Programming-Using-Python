# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:33:23 2022

@author: Ilya
"""

def largest_odd_times(L: list) -> int or None:
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    max_count = 0
    element_odd = None
    for e in L:
        current_count = L.count(e)
        if current_count % 2:
            if element_odd is None:
                element_odd = e
                max_count = current_count
            elif e >= element_odd:
                element_odd = e
                max_count = current_count

    return element_odd

print(largest_odd_times([2,2,4,4]))