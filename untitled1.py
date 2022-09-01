# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:39:19 2022

@author: Ilya
"""

s = 'bobobobobobobobobobobobob'
target = 'bob'
count = 0
i = 0
while i <= len(s)-len(target):
    if s[i] == 'b' :
        i += 1
        if s[i] == 'o':
            i += 1
            if s[i] == 'b':
                count += 1
    else:
        i += 1
print("Number of times bob occurs is: " + str(count))