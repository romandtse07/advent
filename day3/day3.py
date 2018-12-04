#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:29:51 2018

@author: romandtse
"""
from collections import defaultdict
        
import re
#starting to see a pattern opening these gdi
with open('input.txt') as f:
    a = [line for line in f]
    
params = [re.split('\D*', line) for line in a]
def elementsToInt(param):
    try:
        return int(param)
    except:
        return param
params = [[elementsToInt(param) for param in line] for line in params]

map = [[[] for i in range(1000)] for j in range(1000)]
neighbors_dict = defaultdict(int)

for line in params:
    claim, off_x, off_y, width_x, width_y = line[1], line[2], line[3], line[4], line[5]
    current_neighbors = set([])
    for x in range(off_x, off_x + width_x):
        for y in range(off_y, off_y + width_y):
            current_neighbors.update(map[y][x])
            map[y][x].append(claim)
    for claim_neighbor in current_neighbors:
        neighbors_dict[claim_neighbor] += 1
    neighbors_dict[claim] += len(current_neighbors)
                
#q1
print(sum([sum([len(element) > 1 for element in line]) for line in map]))

#q2
print([claim for claim, count in neighbors_dict.items() if count == 0])