#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:38:21 2018
pretty sure i can do this with stacks and no recursion
@author: romandtse
"""

def newInput():
    with open('input.txt') as f:
        inputs = f.read().split(' ')
        
    inputs[-1] = inputs[-1][:-1]
    inputs = [int(num) for num in inputs]
    inputs = inputs[::-1]
    return inputs
    
inputs = newInput()

children = [inputs.pop()]
metas = [inputs.pop()]

num_children = 0
num_metas = 0
da_sum = 0

while inputs:
    if num_children == 0:
        for i in range(num_metas):
            da_sum += inputs.pop()
        try:
            num_children = children.pop()
            num_metas = metas.pop()
        except:
            break
    else:
        children.append(num_children - 1)
        metas.append(num_metas)
        num_children = inputs.pop()
        num_metas = inputs.pop()
        
#OH MY GOD JUST GIVE ME BOTH PARTS OF THE PROBLEM
        
def safePop(stream):
    return stream.pop()

class node:
    def __init__(self):
        self.value = 0
        self.num_children = 0
        self.num_metas = 0
        self.initialized = False
        self.children = []
        self.meta = []
        
    def setParams(self, stream):
        self.num_children = safePop(stream)
        self.num_metas = safePop(stream)
        self.children = [node() for i in range(self.num_children)]
        self.initialized = True
    
    def setValue(self):
        if not self.children:
            self.value = sum(self.meta)
        else:
            #first child was last on the list
            proposed_list = [self.children[::-1][medata - 1].value for medata in self.meta if medata <= self.num_children]
            self.value = sum(proposed_list)
            
    def addMeta(self, stream):
        while len(self.meta) < self.num_metas:
            self.meta.append(safePop(stream))
            
class tree:
    def __init__(self, stream):
        self.root = node()
        self.node_stack = []
        self.node_stack.append(self.root)
        self.root.setParams(stream)
        self.node_stack.extend(self.root.children)
        self.buildTree(stream)
        
    def buildTree(self, stream):
        while stream:
            recent_node = self.node_stack[-1]
            if recent_node.initialized == False:
                recent_node.setParams(stream)
                self.node_stack.extend(recent_node.children)
            else:
                recent_node.addMeta(stream)
                recent_node.setValue()
                self.node_stack.pop()

            
inputs = newInput()
myTree = tree(inputs)