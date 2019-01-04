# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:26:06 2017

@author: Praneesh
"""

def f(x) :
    x = x + 1
    print("in f(x), x = " , x)
    return x
z = f(3)


def g(x):
    def h() :
        x = 'abc' 
    x = x + 1    
    print('x in g(x) is ', x)
    h()
    

x = 3
z = g(x)
print(z)
