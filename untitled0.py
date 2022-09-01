# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 09:22:49 2022

@author: Ilya
"""

s = 'azcbobobegghakl'
count = 0
for i in s:
    if i == 'a' or i == 'e' or \
        i == 'i' or i == 'o' or i == 'u':
        count += 1
print("Number of vowels: ", str(count))