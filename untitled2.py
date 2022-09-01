# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:25:31 2022

@author: Ilya
"""

s = 'capskglxeipbht'
abc = 'abcdefghijklmnopqrstuvwxyz'
current_str = ''
long_str = ''
current_inx = 0
prev_inx = 0
i = 0

while i < len(s):
    while s[i] != abc[current_inx]:
        current_inx += 1
    if current_inx >= prev_inx:
        current_str += s[i]
        prev_inx = current_inx
        i += 1
    else:
        if len(current_str) > len(long_str): 
            long_str = current_str    
        current_str = ''
        prev_inx = 0
    current_inx = 0
if len(current_str) > len(long_str): 
    long_str = current_str
print('Longest substring in alphabetical order is: ' + long_str)
    