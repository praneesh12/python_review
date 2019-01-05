#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:19:56 2019

@author: praneeshkhanna
"""

'''
HACKERANK Problem 1

In this challenge, you will be given 2 integers, n and m . There are n words, which
might repeat, in word group A. There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

'''

from collections import defaultdict
alist = ['a', 'a', 'b', 'a', 'b']
blist = ['a', 'b', 'c']

n = len(alist)
m = len(blist)
d = defaultdict(list)

list1 = []

for i in range(n):
    print(alist[i])
    d[alist[i]].append(i+1)
    print(d)

for _ in range(m):
    list1.append(blist[_])
    print(list1)

for x in list1 : 
    if x in d:
        print(' '.join(map(str, d[x])))
    else :    
        print(-1)
