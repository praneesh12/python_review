#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 01:05:40 2019

@author: praneeshkhanna
"""

from collections import Counter
#from collections import defaultdict

X = int(input())
shoelist = [int(x) for x in input().split(' ')]
n = int(input())
shoelist_counter = Counter(shoelist)

money_earned = 0


for size, amount in [map(int, input().split()) for i in range(n)]:
  if shoelist_counter[size] > 0:
    money_earned += amount
    #print('After selling size {}, money earned  ${}'.format(size ,money_earned))
    shoelist_counter[size] -= 1
    #print('{}'.format(shoelist))
print(money_earned)