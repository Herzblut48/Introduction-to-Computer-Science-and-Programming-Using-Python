# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:57:40 2022

@author: Ilya
"""
from typing import List

def uniqueValues(aDict: dict) -> List:
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    
    if not aDict:
        return []
    
    res_list = []
    vals = list(aDict.values())
    for k,v in aDict.items():
        if vals.count(v) == 1:
            res_list.append(k)
    res_list.sort()
    return res_list

print(uniqueValues({1: 1, 2: 1, 3: 1}))