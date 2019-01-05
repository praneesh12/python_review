#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:10:26 2019

@author: praneeshkhanna
"""

from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(dot_product)

# =============================================================================
# Hackerank question: find average marks 
# =============================================================================

N = int(input())
fields = input().split()

total = 0

for i in range(N):
  students = namedtuple('student', fields)
  field1,field2,field3,field4 = input().split()
  #print('{} {} {} {}'.format(field1,field2,field3,field4))
  student = students(field1,field2,field3,field4)
  total += int(student.MARKS)

print('{:.2f}'.format(total/N))
