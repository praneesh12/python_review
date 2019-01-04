# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 23:23:55 2017

@author: Praneesh
"""

#binary seach for square root
x = 25
epsilon = 0.01
numguesses = 0
low = 0.0
high = x
ans = (low + high)/2.0

while abs(ans**2 - x) >= epsilon :
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numguesses += 1
    if ans**2  > x :
        high = ans
    else :
        low  = ans
    ans = (high + low)/2.0
print('numguesses = ' , str(numguesses))
print(str(ans) , ' is close to square root ' , str(x))


#binary square for cube root
x = 27
epsilon = 0.01
numguesses = 0
low = 0.0
high = x
ans = (low + high)/2.0

while abs(ans**3 - x) >= epsilon :
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numguesses += 1
    if ans**3  > x :
        high = ans
    else :
        low  = ans
    ans = (high + low)/2.0
print('numguesses = ' , str(numguesses))
print(str(ans) , ' is close to square root ' , str(x))





