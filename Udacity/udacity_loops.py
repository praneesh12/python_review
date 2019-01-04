#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 21:52:26 2019

@author: praneeshkhanna
"""

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), 
            ("machine", 120), ("cheeses", 5)]

cargo_list = []
cargo_weight = 0
for item, weight in manifest:
    if cargo_weight < 100 :
        if cargo_weight + weight < 100 :
            cargo_weight += weight
        else :
            continue
        cargo_list.append(item)
        print('item {} with weight {} added'.format(item, weight))

print(cargo_weight)
print(cargo_list)
        
    
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

for x in headlines:
    news_ticker += x + ' '
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        
        
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

 for num in check_prime:
    for x in range(2,num):
        if (x % num) == 0 :
            print(num,"is not a prime number")
            print(x, " is a factor of ", num)
            break
        else:
            print(num,"is a prime number")
            break
        
        
        
prime_numbers = 0

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True
	        

for i in range(int(raw_input("How many numbers you wish to check: "))):
    if is_prime_number(i):
        prime_numbers += 1
        print i

print "We found " + str(prime_numbers) + " prime numbers."
    

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for l,x,y,z in zip(labels,x_coord, y_coord, z_coord):
    point = l + ': ' + str(x) + ', ' + str(y) + ', ' + str(z)
    points.append(point)

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)


for point in points:
    print(point)
    
# =============================================================================
# Unzip tuples
# =============================================================================

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose) 
# ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    