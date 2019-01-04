# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 00:33:54 2017

@author: Praneesh
"""

#find the secret number
x = int(input('Please think of a number between 0 and 100! : '))
high = 100
low = 0

guess = False
while not guess :
    # use // instead of / in (hi + lo)/2 to get the round of number
    ans = (high + low)//2
    print('Is your secret number' + str(ans)) 
    fb = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly"))
    if fb == 'h' :
        high = ans
        
    elif fb == 'l' :
        low = ans
        
    elif fb == 'c' :
       print('Game over. Your secret number was: ' +  str(ans))
       break
    else :
       print('Sorry, I did not understand your input.')
       
    