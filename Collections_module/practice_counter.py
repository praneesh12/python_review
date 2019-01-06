#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 23:44:54 2019

@author: praneeshkhanna
"""

from collections import Counter
import random

exmaplelist = [random.randint(1,100) for x in range(20)]

counts = Counter(exmaplelist)

# 5 most common elements
counts.most_common(5) # [(1, 5), (79, 3), (14, 1), (80, 1), (32, 1)]
counts.most_common(5)[0] # most common element within top 5



counts[1] = 5
counts[55] = 0

del counts[55]

count_lst = list(counts.elements())

# adding two counters

examplelist2 = [random.randint(1,20) for x in range(20)]

counts2 = Counter(examplelist2)
final_counts = counts + counts2 

# =============================================================================
# Using defaultdict
# =============================================================================
for size, cost in [map(int, input().split()) 
                      for _ in range(int(input()))]:
    if stock[size]>0:
        stock[size]-=1
        money+=cost
print(money)


shoelist_counter = Counter(shoelist)
d = defaultdict(list)
cust_list = []
for i in range(n):
  cust_list.append(list(map(int, input().split(' '))))
  print(list(map(int, input().split(' ')))[0])
  print(list(map(int, input().split(' ')))[1])

for c in cust_list:
  d[c[0]].append(c[1])

amount_earned = 0
for k,v in d.items():
  if k in shoelist_counter.keys():
    amount_earned += v[0]
    del d.val

  cust_list.append(list(map(int, input().split(' '))))

cust_counter = Counter([l[0] for l in cust_list])
not_present = cust_counter - shoelist_counter
present = cust_counter - not_present

print(present)
print(shoelist_counter)

amount_earned = 0
print(cust_list)
for size in cust_list:
  if size[0] in present.keys():
    print('Amount earned for size {} is {}'.format(size[0], size[1]))
    amount_earned += size[1]
    del cust_list[size[0]]
print(amount_earned)