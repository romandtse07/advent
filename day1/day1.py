#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:19:10 2018
day 1 of advent coding challenge thing
@author: romandtse
"""

import re
with open('input.txt') as f:
    a = [int(re.findall('-?\d+', line)[0]) for line in f]
    
#q1
print(sum(a))

#q2
frequencies = set([0])
current = 0
i = 0
found = False

while not found:
    current += a[i%len(a)]
    if current in frequencies:
        print(current)
        print(i)#wtf zero
        break
    frequencies.add(current)
    i += 1