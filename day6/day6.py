#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:47:02 2018

@author: romandtse
"""
import numpy as np

with open('input.txt') as f:
    read_in = f.read()
    
nodes = [[int(coord) for coord in line.split(',')] for line in read_in.split('\n')[:-1]]

x = [pair[0] for pair in nodes]
x_min, x_max = min(x), max(x)

y = [pair[1] for pair in nodes]
y_min, y_max = min(y), max(y)

points = [np.array([x, y]) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)]
nodes = np.array(nodes)

def manhattanD(coordinate, nodes_list):
    return abs(coordinate - nodes_list) @ np.array([1,1])

nearest_nodes = []

for pair in points:
    distances = manhattanD(pair, nodes)
    minimum = min(distances)
    mindex = np.where(distances == minimum)
    if len(mindex[0]) > 1:
        nearest_nodes.append(51)
    else:
        nearest_nodes.append(mindex[0][0])
        
infinites = set([51])
for coord_index, node_index in enumerate(nearest_nodes):
    if points[coord_index][0] in [x_min, x_max] or points[coord_index][1] in [y_min, y_max]:
        infinites.add(node_index)
        
counted_nodes = [node for node in nearest_nodes if node not in infinites]

from collections import Counter
counted_nodes = Counter(counted_nodes)

q1 = counted_nodes.most_common()[0][1]

projector = np.ones(len(nodes))
q2 = sum([manhattanD(pair, nodes) @ projector  < 10000 for pair in points])