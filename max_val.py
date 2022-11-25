# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:56:15 2022

@author: Ilya
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
        
    def helper_finder(list_int_h, el_h):
        for e in el_h:
            if type(e) is int:
                list_int_h.append(e)
            else:
                helper_finder(list_int_h,e)
    
    list_int = []
    
    for el in t:
        if type(el) is int:
            list_int.append(el)
        else:
            helper_finder(list_int,el)
    
    return max(list_int)