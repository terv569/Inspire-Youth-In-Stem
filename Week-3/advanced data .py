#!/usr/bin/env python3
 
# Python program to create lists
# Name : Tervil Moywaywa
# Email : tervilmoywaywa@gmail.com
# Date : 23rd Feb 2023
# File : advanced data.py
# Advanced data types
# mutable vs immutable


# Data types that can be changed during program life cycle
# Add / remove elements
# Immutable----> these are data types that cannot be edited during program life cycle
# 1) list (murtable)
friends = ["Terv","Max","Rita",]
# or friends =[]empty list
# add elements ----> append(), extend()
# remove elements -----> pop(), del()
students = ["Max","Sue","Chad",]
friends.extend
friends.append
friends.sort
friends.reverse


# 2)tuples(immutable)
#type of lists that are immutable
stationery = ("pens","ink","sharpener","stapler")
# replace the whole tupple
stationery = ("ruler","eraser","clipboard")
for station in stationery:
    print(station)
numbers = (1,2,3,4,5,6,7,8,9)
# 3)dictionaries aka dict
# uses key and value pair

student = {"name": "Terv", "age": 24 , "gend": "male"}

print(student["name"])
print(student["age"])
print(student["gend"])




friend = {"weight": 85 , "tribe": "kisii" , "course": "medicine" , "height": 176}
print(friend["weight"])
print(friend["tribe"])
print(friend["course"])
print(friend["height"])




#name(key) Terv(value)
# sets
# used 
my_fruits = ["banana","pear","apple","orange","pineapple"]
print(my_fruits)

for fruit in my_fruits:
    print(fruit)


print(type(my_fruits))
print(len(my_fruits))