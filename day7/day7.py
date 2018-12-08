#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:31:59 2018
it's become obvious i really need to think about organization if i want to get faster
also fucking unreadable
@author: romandtse
"""
instructions = []
from collections import namedtuple
import re

instruction = namedtuple('instruction', 'parent, child')
with open('input.txt') as f:
    for line in f.read().split('\n')[:-1]:
        upper_cases = re.findall('[A-Z]', line)
        instructions.append(instruction(upper_cases[1], upper_cases[2]))

class step:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        
    def addParent(self, parent_name):
        self.parents.append(parent_name)
        
    def addChildren(self, child):
        self.children.append(child)
        
    def getName(self):
        return self.name
    
    def getParents(self):
        return self.parents
    
    def getChildren(self):
        return self.children
    
    def popParent(self, parent_name):
        try:
            self.parents.remove(parent_name)
        except:
            pass
        
#this is fine, also assuming no parent child loops
nodes = {}
parents = set([])
children = set([])

for pair in instructions:
    if pair.parent not in nodes:
        nodes[pair.parent] = step(pair.parent)
        parents.add(pair.parent)
    if pair.child not in nodes:
        nodes[pair.child] = step(pair.child)
    nodes[pair.parent].addChildren(nodes[pair.child])
    nodes[pair.child].addParent(pair.parent)
    children.add(pair.child)
    
work = list(parents.difference(children))
work.sort(reverse = True)
completed = ''
wait = []
init_lag = 61

def needsWork(child, current, work, wait, finish):
    return not any([child in queue for queue in [current, work, wait, finish]])

class elf:
    def __init__(self):
        self.step = []
        self.time_left = 0
        
        
    def advanceState(self, work, wait, finished):
        if self.time_left > 0:
            self.time_left -= 1
            self.enqueueChildren(work, wait, finished) if self.time_left == 0 else 0
        else:
            pass
        
    def enqueueChildren(self, work, wait, finished):
        finished.append(self.step.pop())
        for item in finished:
            for child in nodes[item].getChildren():
                wait.append(child.getName()) if needsWork(child.getName(), current, work, wait, finished) else 0#can't pass
            
    def grabNext(self, work):
        if self.step or not work:
            return 0
        self.step.append(work.pop())
        self.time_left = init_lag + ord(self.step[0]) - ord('A')
        
def prepareState(work, wait, finish):
    for child in wait:
        for parent in nodes[child].getParents(): #ugh
            nodes[child].popParent(parent) if parent in finished else 0
        if not nodes[child].getParents():
            move_me = nodes[wait.pop(wait.index(child))]
            work.append(move_me.getName())        

elf_list = [elf() for i in range(5)]
finished = []
time = 0

while len(finished) < len(nodes):
    for elf in elf_list:
        elf.grabNext(work)
        current = [elf.step[0] for elf in elf_list if elf.step]
    for elf in elf_list:
        elf.advanceState(work, wait, finished)
    prepareState(work, wait, finished)
    work.sort(reverse=True)
    time += 1

            
            