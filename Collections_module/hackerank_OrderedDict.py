#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:28:06 2019

@author: praneeshkhanna
"""

from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
  item, price = (input().rsplit(None, 1))
  if item not in d.keys():
    d[item] = int(price)
  else:
    d[item] += int(price)

for k,v in d.items():
  print(k,v)