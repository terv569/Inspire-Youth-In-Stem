#!/usr/bin/env python3
 
# Python program to create lists
# Name : Tervil Moywaywa
# Email : tervilmoywaywa@gmail.com
# Date : 21st Feb 2023
# File : diamond.py
h = eval(input("enter diamond's height:"))

for x in range (h):
    print(" " *(h-x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " *(h-x), "x" * (2*x + 1))


import cmath

first_coefficient = int(input("enter the first coefficient:"))
second_coefficient = int(input("enter the second coefficient:"))
constant = int(input("enter the constant"))

ans1= -abs(second_coefficient) - cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/
(2*first_coefficient)
ans2= -abs(second_coefficient) - cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/
(2*first_coefficient)

print("the answers are"+str(ans1)+" and "+atr(ans2))


R = int(input("enter range:"))
#using for loop to draw a triangle
for diamond in range



print("the answers are" +str(ans1)+)