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