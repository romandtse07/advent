#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:41:35 2018

@author: romandtse
"""
from collections import Counter

def checkRow(string):
    times_dict = Counter(string)
    return (2 in times_dict.values(), 3 in times_dict.values())

twos, threes = 0, 0
with open('input.txt') as f:
    for line in f:
        is_in = checkRow(line)
        twos += is_in[0]
        threes += is_in[1]

#q1
checksum = twos * threes

#q2
with open('input.txt') as f:
    a = [line for line in f]
    
found = False
req_len = len(a[0]) - 1

for i in range(len(a)):
    if found:
        break
    print(f'looked through pairs for {i}')
    for j in range(i+1, len(a)):
        comparison = [letter_i for letter_i, letter_j in zip(a[i], a[j]) if letter_i == letter_j]
        if len(comparison) == req_len:
            print(''.join(comparison))
            found = True
            break