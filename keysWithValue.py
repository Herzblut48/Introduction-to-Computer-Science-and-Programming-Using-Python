# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:52:30 2022

@author: Ilya
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    ''' 
    
    list_keys = [k for k,v in aDict.items() if v == target]
    return sorted(list_keys)