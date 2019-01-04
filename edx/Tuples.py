#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:51:48 2018

@author: praneeshkhanna
"""

#https://docs.python.org/3/tutorial/datastructures.html

''' Tuples - an ordered sequence of elements, can mix element types. These are 
    immutable and cannot change element values.
    
    * Very convienient for swapping
'''
x = (1,'q')
y = (2,'g')
(x,y) = (y,x)

# =============================================================================
# very useful return more than one value from a function
# =============================================================================

def quotient_remainder(x,y):
    q = x//y
    r = x%y
    
    return (q,r)

(quot, rem) = quotient_remainder(1098,23)
    
# =============================================================================
# tuples are iterable 
# =============================================================================

def get_data(aTuple):
    num = ()
    words = ()
    
    for t in aTuple :
        num = num + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
        
    min_nums = min(num)
    max_nums = max(num)
    unique_words = len(words)
        
    return (min_nums, max_nums, unique_words)
    
(small, large, words) = get_data(((1, 'mine') , (2, 'yours'), (3, 'ours'), (4, 'mine')))
   

get_data(((1, 'mine') , (2, 'yours'), (3, 'ours'), (4, 'mine')))


# =============================================================================
# Lists - Operations
# =============================================================================
 
l = [1,2,3,4]
l.append(5)

''' dot notations 
    everything in python is an object. 
    objects have methods and functions
    access this information by object_name.do_something()
'''
   
'''  lists can be concatenated using + operator
     mutate lists using .extend(some_list)
     
     concatenation '+' operator adds two lists 
     mutate using .extend() changes the existing list
'''

l1 = [1,2,3]
l2 = [2,3,4]

l3 = l1 + l2   

l1.extend([0,6])  

# =============================================================================
# Removing elements from a list
# =============================================================================

''' delete element at a specific index with del (List_name[index])
    remove element at the end of a list with List_name.pop() - returns the removed element
    remove specific element from a list with List_name.remove(element)
    looks for the element and removes it
    if the element occurs multiple times, removes first occurence 
    if element not in list, gives an error
'''

L = [1,2,3,4,5,6,7,8,9]
L.remove(2)
del (L[1])
L.pop()    

# =============================================================================
# String operations
# =============================================================================
'''convert string to list with list(s)
   s.split() splits a string on a character parameter. Splits on spaces if 
   called without a parameter
   
   .join(List_name) to turn a list of characters into a string, can give a character in quotes
    to add char in every element 
'''

s = "I <3 cs"
list(s)
s.split('<')
''.join(s)
'_'.join(s)

# =============================================================================
# Functions as objects
# =============================================================================


def applyToEach(L,F):
    """ assumes L is a list, F is a function that mutates L by replacing 
        each element of L by f(e):
    """
    for i in range(len(L)):
       L[i] = F(L[i])
    return L   
        
L = [1,-2,3.4]
applyToEach(L, abs)
applyToEach(L, int)
applyToEach(L, fact)
applyToEach(L, fib)


''' Applying list of functions to a number 
'''

def applyFuns(L, x):
    for f in L:
        print(f(x))

applyFuns([abs, int], -4.3)        

# =============================================================================
# Maps
# =============================================================================
''' Higher order procedure
    simple form -a unary function and a collection of suitable arguments
    map(abs, [1,-2,2.3,5,-9])
    But we need to produce an iterable form
'''
for elt in map(abs, [1,-2,2.3,5,-9]):
    print(elt)

''' n-ary functions and collection of n arguments
    useful when we want to compare two variables 
'''
l1 = [1,22,3]
l2 = [5,6,7]

for elt in map(min, l1,l2):
    print(elt)
    
    
def applyEachTo(L,x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1    

applyEachTo([inc, square, halve, abs], -3)
applyEachTo([inc, square, halve, abs], 3.0)         
applyEachTo([inc, max, int], -3)





























