#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:48:23 2019

@author: praneeshkhanna
"""

from collections import Counter
n = int(input())
wordlist = [input().strip() for i in range(n)]
dist_words = len(set(wordlist))
word_count = Counter(wordlist)
print(dist_words)
wordorder = ' '.join([str(val) for val in word_count.values()])
print(wordorder)