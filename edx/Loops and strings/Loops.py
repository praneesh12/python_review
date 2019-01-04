#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:51:13 2018

@author: praneeshkhanna
"""
# =============================================================================
# while loo
# =============================================================================
x = 3
ans = 0
itersLeft = x
while itersLeft != 0 :
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + '=' + str(ans))

# =============================================================================
# Guess and check algorithm using while loop
# =============================================================================

x = int(input('Enter an Integer: '))
ans = 0
while ans**3 < 0:
    ans += 1
if ans ** 3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0 :
        ans = -ans
    print('Cube root of' + str(x) + 'is' + str(ans))

# =============================================================================
# using for loop
# =============================================================================
    
x = int(input('Enter an Integer: '))    
for guess in range(x+1):
    if guess ** 3 == x:
        print('Cube root of ' , x, ' is', guess )
        
        
x = int(input('Enter an Integer: '))   
for guess in range(abs(x)+ 1):
    if guess ** 3 >= abs(x):
        break
if guess ** 3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x <0 :
        guess = -guess
        print('Cube root of ' + str(x) + 'is' + str(guess))
        
# =============================================================================
# Assignment 1
# =============================================================================
s = 'azcbobobegghakl'
counter = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        counter = counter + 1
print('Number of Vowels in s are ' , counter )

# =============================================================================
# Assignment 2 count number of times a string occurs in another string
# =============================================================================
s = 'azcbobobegghakl'
p = 'bob'
length = len(s)
counter = 0
for i in range(length) :
    for j in range(length):
        if s[i:j] == p:
            counter = counter + 1
print('Number of bob occurs in s ' , counter)        

# =============================================================================
# Assignment 3 longest substring in alphabetical order         
# =============================================================================
s = 'azcbobobegghakl'
maxLen = 0
current = s[0]
longest = s[0]

for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        current = current + s[i+1]
        # if current length is bigger update
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
        else:
            current = s[i+1]
        i = i + 1
print('Longest substring in alphabetical order is', longest)        
            

















