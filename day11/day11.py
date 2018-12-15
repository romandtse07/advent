#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:52:07 2018

@author: romandtse
"""
import numpy as np

def getPowerLevel(x, y, serial = 7139):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level = power_level//100%10
    power_level -= 5
    return power_level

#reversed coords apparently
grid = np.array([[getPowerLevel(x, y) for x in range(300)] for y in range(300)])

def grabGridPower(x, y, size = 3):
    return grid[x:x+size, y:y+size].sum()

q1_vals = {f'{x},{y}': grabGridPower(x,y) for x in range(298) for y in range(298)}
q1 = sorted([(val, key) for key, val in q1_vals.items()], reverse=True)[0]

q2_vals = {f'{x},{y},{d}': grabGridPower(x,y,d) for d in range(300) for x in range(300-d+1) for y in range(300-d+1)}
q2 = sorted([(val, key) for key, val in q2_vals.items()], reverse=True)[0]