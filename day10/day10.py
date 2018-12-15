#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:18:53 2018
count straight lines?  looking and guessing isn't cutting it even with the initial guess
@author: romandtse
"""
import re
import numpy as np
import matplotlib.pyplot as plt

positions = []
velocities = []

with open('input.txt') as f:
    line = f.readline()
    while line:
        params = re.findall('<([^<^>]*)>', line)
        x = [int(coord) for coord in params[0].split(',')]
        v = [int(velocity) for velocity in params[1].split(',')]
        positions.append(x)
        velocities.append(v)
        line = f.readline()
        
positions = np.matrix(positions)
velocities = np.matrix(velocities)

yrange = max(positions[:,1]) - min(positions[:,1])
yrange_previous = yrange


while yrange <= yrange_previous:
    yrange_previous = yrange
    positions += velocities * yrange_previous.sum()//100
    yrange = max(positions[:,1]) - min(positions[:,1])
    
def getVector(positions, index):
    return np.asarray(positions[:, index].T).reshape(-1)
  
while sum(getVector(positions, 1) == max(getVector(positions, 1))) < 10:
    yrange_previous = yrange
    positions += velocities
    yrange = max(positions[:,1]) - min(positions[:,1])

def display(positions):
    plt.figure(figsize = (20,5))
    plt.scatter(getVector(positions, 0), getVector(positions, 1))
    plt.show()
    
def f(seconds = 1):
    global positions
    positions += velocities * seconds
    display(positions)
    
def b(seconds = 1):
    global positions
    positions -= velocities * seconds
    display(positions)
    

