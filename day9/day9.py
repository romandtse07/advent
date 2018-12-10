#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:00:24 2018
shit inserting into list IT'S A TRAP
@author: romandtse
"""
from collections import defaultdict

def runGame(players, marbles):
    game = [0,1]
    current_position = 1
    scores = defaultdict(int)
    
    for marble in range(2, marbles + 1):
        player = marble%players
        current_position = (current_position + 2)%len(game)
        if marble%23 == 0:
            current_position = (current_position - 9)%len(game)
            scores[player] += (marble + game.pop(current_position))
        elif current_position != 0:
            game.insert(current_position, marble)
        else:
            game.append(marble)
            current_position = len(game) - 1
    return scores

q1 = runGame(410, 72059)
scorganized = [(value, key) for key, value in q1.items()]
scorganized.sort(reverse = True)
q1 = scorganized[0][0]

winning_elf = scorganized[0][1]

class Marble:   
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self, marble):
        self.next = marble
        
    def setPrevious(self, marble):
        self.previous = marble
        
class Chain:
    def __init__(self):
        self.resetSystem()
        
    def resetSystem(self):
        self.current = Marble(0)
        self.root = self.current
        self.current.setNext(self.current)
        self.current.setPrevious(self.current)
        self.num_marbles = 0
        self.scores = defaultdict(int)
        
    def goForward(self, forwards):
        for i in range(forwards):
            self.current = self.current.getNext()
            
    def goBack(self, backs):
        for i in range(backs):
            self.current = self.current.getPrevious()
    
    def insertMarble(self, value):
        current_marble = self.current
        next_marble = self.current.getNext()
        new_marble = Marble(value)
        current_marble.setNext(new_marble)
        next_marble.setPrevious(new_marble)
        new_marble.setNext(next_marble)
        new_marble.setPrevious(current_marble)
        self.current = self.current.getNext()
        
    def removeMarble(self):
        next_marble = self.current.getNext()
        previous_marble = self.current.getPrevious()
        next_marble.setPrevious(previous_marble)
        previous_marble.setNext(next_marble)
        self.current = next_marble
        
    def getList(self):
        current = self.root
        results = [current.value]
        current = current.getNext()
        while current.value != self.root.value:
            results.append(current.value)
            current = current.getNext()
        return results
        
    def solveSystem(self, players, marbles):
        self.resetSystem()
        for i in range(1, marbles + 1):
            player = i % players
            if i % 23 == 0:
                self.scores[player] += i
                self.goBack(7)
                self.scores[player] += self.current.value
                self.removeMarble()
            else:
                self.goForward(1)
                self.insertMarble(i)
                
    def getHighestScore(self):
        sort_me = [(value, key) for key, value in self.scores.items()]
        sort_me.sort(reverse=True)
        return sort_me[0]
