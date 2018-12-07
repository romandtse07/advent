#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:31:08 2018

@author: romandtse
"""
#how many times will i bank on neat input? all the times
#holy shit i have to stop doing these patchwork try/excepts
def reverseCase(char):
    try:
        return (1 - 2*(char > 90))*(ord('a') - ord('A')) + char #who's reading this anyway
    except:
        print(char)
        return ''

def parseFile(ignored = 0):
    muh_stack = []
    to_destroy = 0
    ignore_these = [ignored, reverseCase(ignored)]
    
    with open('input.txt') as f:
        while True:
            try:
                char_in = ord(f.read(1))
            except:
                break
            if char_in in ignore_these:
                    next
            elif char_in != to_destroy:
                muh_stack.append(char_in)
                to_destroy = reverseCase(char_in)
            else:
                muh_stack.pop()
                try:
                    to_destroy = reverseCase(muh_stack[-1])
                except:
                    pass
    return muh_stack[:-1]

muh_stack = parseFile()    
q1 = ''.join([chr(ordinal) for ordinal in muh_stack])

letters = [ord('a') + i for i in range(ord('z') - ord('a') + 1)]
poly_lengths = {chr(letter):len(parseFile(letter)) for letter in letters}

#did not think the dictionary thing through again
q2 = [(length, letter) for letter, length in poly_lengths.items()]
q2.sort()