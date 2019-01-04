#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:12:56 2018

@author: praneeshkhanna
"""

''' Inductive Reasoning '''

def mult_iter(a,b):
    result = 0
    while b >0 :
        result += a
        b -= 1
    return result

def mult_recur(a,b):
    if b == 1:
        return a
    else :
        return a + mult_recur(a,b-1)
    
# =============================================================================
# Mathematical Induction - Tower of Hanoi
# =============================================================================
''' To prove a statement indexed on integers is true for all values of n:
    Just prove it is true for smallest value of n and an arbitarty value of n. 
    Then one can show that it will be true for n+1 values 
'''

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))        
    
# =============================================================================
# Fibonnacci Numbers - Rabbit mating problem
# =============================================================================
    
'''base cases
   Female(0)= 1
   Female(1)= 1
   
   Recursive case
   Female(n) = Female(n-1) + Female(n-2)
'''

def fib(x):
    """ assume x is int>0
        returns fibonacci of x 
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
    
# =============================================================================
# Palindrone - Recursively
# =============================================================================
''' First, convert the strng to characters, by stripping out punctuation, and 
    converting upper case to lower case
    
    Base case: a string of length 0 or 1 is a palindrome
    Recursive case: 
        if first and last character matches, check 2nd and 2nd last
        if all matches, then it is a palindrome
'''


def isPalindrome(s):
   
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmopqrstuvwxyz':
                ans = ans + c
        return ans
        
    def isPal(s):
        if len(s) <= 1 :
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

print(isPalindrome('Able Was I, ere I saw elb'))

# =============================================================================
# Modularity
# =============================================================================
''' A module is .py file containing collection of Python definitions and statements
'''

import circle

pi = 3
print(pi)

print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))


# =============================================================================
# How to handle files
# =============================================================================

nameHandle = open('kids', 'w')

for i in range(2):
    name = input('Enter Name :')
    nameHandle.write(name + '\n')
nameHandle.close()


nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()    




















    