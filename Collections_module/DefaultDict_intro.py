#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:36:31 2019

@author: praneeshkhanna
"""

'''
DefaultDict

The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only difference
is that a defaultdict will have a default value if that key has not been
set yet. If you didn't use a defaultdict you'd have to check to see if that
key exists, and if it doesn't, set it to what you want. 

'''

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")

for i in d.items():
    print(i)
    
    
from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55,155,255)
white = Color(255,255,255)

print(color.blue)
