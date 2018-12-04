#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:39:58 2018
oh my god i haven't used pandas in forever
@author: romandtse
"""
#fuck it
import pandas as pd
import re
from collections import defaultdict

with open('input.txt') as f:
    a = [line[:-1] for line in f]
    
time_end_index = a[0].index(']')
verb_begin_index = time_end_index + 2
verb_end_index = verb_begin_index + 5
a = [[line[1:time_end_index], 
      line[verb_begin_index:verb_end_index], 
      line[verb_end_index+1:]] for line in a]

df = pd.DataFrame(a)
df.columns = ['date', 'state', 'guard']
df.date = df.date.apply(lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M'))
df.sort_values(by='date', inplace=True)
df['time_slept'] = df.date.diff() * df.state.shift(1).apply(lambda x: 1 if x == 'falls' else 0)
df.guard = df.guard.apply(lambda x: re.findall('\d*', x)[1]).apply(lambda x: None if x == '' else x).ffill()

laziest = df.groupby(by='guard').time_slept.sum().sort_values(ascending=False).head(1).index[0]


def getPopularMinute(guard):
    guard_schedule = df.query(f'guard == "{guard}"').assign(wake_time = lambda df: df.date.shift(-1)).query('state == "falls"')
    minute_counter = defaultdict(int)
    for i, row in guard_schedule.iterrows():
        current_time = row.date
        while current_time < row.wake_time:
            minute_counter[current_time.minute] += 1
            current_time += pd.Timedelta('1 min')
            
    popular_min = [(val, key) for key, val in minute_counter.items()]
    popular_min.sort(reverse=True)
    try:
        return popular_min[0]
    except:
        #forgot some don't sleep
        print(guard_schedule)
        return (0, 0)

q1 = int(laziest)*getPopularMinute(laziest)[1]

#gdi i wish i could see the entire question at once
guards = df.guard.unique()
max_guard = 0
max_count = 0
max_min = 0
for guard in guards:
    pop_min = getPopularMinute(guard)
    if pop_min[0] > max_count:
        max_count = pop_min[0]
        max_min = pop_min[1]
        max_guard = int(guard)
        
q2 = max_min * max_guard