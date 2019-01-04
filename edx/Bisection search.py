#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:53:34 2018

@author: praneeshkhanna
"""

#strings are immutable objects 
s = 'hello'
s[0] = 'y'

#but we can concat strings 
s = 'y' + s[1:]
s = s[0:5] +'w' 

an_letters = 'aefhilmnorsxAEFHILMNORSX'
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm Level (1-10): "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters :
        print("Give me an " + str(char) + "!" + char)
    else :
        print("Give me a " + str(char) + "!" + char)
    i = i +1
print('How does this spell')
for i in range(times) :
    print(word, '!!!')
    
 
# =============================================================================
# Guess and check with approximate solutions
# =============================================================================
x =225
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(round(guess)))
    
# =============================================================================
# Bisection seatch  
# =============================================================================
#square root of a number x lies between 1 and x.
# divide the range 1 to x and check if x/2 is square root of x
# if not, check if (x/2)^2 > x or not. Remove the other part
#repeat previous step, lets say (x/2)**2 > x.
#now x/4 is the new point, check if (x/4)^2 > x
# if yes, remove the other part
    
#code
x = int(input('Enter a number: '))
epsilon = 0.01
numGuesses = 0
low = 1
high = x
ans = (high+low)/2.0

while abs(ans**2 - x) > epsilon :
    print('Low = ' + str(low) + ' High = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' close to square root of x')
    

   
    
    





















