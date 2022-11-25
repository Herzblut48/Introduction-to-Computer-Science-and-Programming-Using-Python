# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:33:32 2022

@author: Ilya
"""

def getSublists(L, n):
    
    sub_list = []
    while n <= len(L):
        sub_list.append(L[:n])
        L = L[1:]
    return sub_list
    
    
