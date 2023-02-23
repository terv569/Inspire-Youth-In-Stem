#!/usr/bin/env python3
 
# Python program to create lists
# Name : Tervil Moywaywa
# Email : tervilmoywaywa@gmail.com
# Date : 21st Feb 2023
# File : diamond 2.py
h = eval(input("enter diamond's height:"))

for x in range (h):
    print(" " *(h-x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " *(h-x), "x" * (2*x + 1))


import cmath
print("the general formula is a*x**2 + b*x + c =0 ")

a = int (input("enter a"))
b = int (input("enter b"))
c = int (input("enter c"))


Sn1  = (-b + cmath.sqrt(b**2 -(4*a*c))) / 2*a 
Sn2 = (-b - cmath.sqrt(b**2 -(4*a*c))) / 2*a

print ("answer one is :", Sn1)
print("answer two is :", Sn2)

