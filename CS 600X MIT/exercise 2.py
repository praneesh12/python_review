# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = float(input('enter an integer :'))
if x%2 == 0 :
    print('')
    print('EVEN')
else : 
    print('')
    print('odd')

print('Done with conditional')    



x = float(input('Enter an integer :'))
if x%2 == 0:
    if x%3 == 0:
        print('divisible by 3')
    else :
        print('divisible by 2 and not 3')
elif x%3 == 0:
    print('divisible by 3 and not 2')

        
    

#square of a number
x = int(input('enter the integer you want to square :'))
y = x
z = 0
while y != 0 :
    z = z + x
    y = y - 1
print('the square of the number is' , z)
    



numberOfLoops = 0
numberOfApples = 2
while numberOfLoops > 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))


num = 10
while not False:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')



num = 10
while True:
     if num < 7:
        print('Breaking out of loop')
        break
print('Outside of loop')


end = int(input('enter an integer'))
s = 0
while end > 0 :
     s += end 
     end = end - 1
print(s)



x = 1
while x <= 10:
      if x % 2 == 0:
         print(x)
      x += 1
print('Goodbye!') 


x = 10
print('Hello!')
while x > 0 :
      print(x)
      x -= 2
      
      
      
s = 0
while end > 0 :
     s += end 
     end = end - 1
print(s)
      


print('Hello!')
for i in range(10,0,-2):
         print(i)
         
         
for i in range(2,11,2) :
       print(i)
print('Goodbye!')



s = 0
for end in range(end,0,-1):
           s += end
print(s)

x = int(input('Enter an integer'))
ans = 0
while ans**3 > abs(x):
    ans += 1
if ans**3 != abs(x) :
    print(str(x) + ' is not a perfect cube')
else :
    if x < 0 :
       ans = -ans 
    print(str(x) + ' is a perfect choice')
    



    