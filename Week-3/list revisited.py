#!/usr/bin/env python3
 
# Python program to create lists
# Name : Tervil Moywaywa
# Email : tervilmoywaywa@gmail.com
# Date : 20th Feb 2023
# File : list revisited.py
#len
myFavouriteFruits = ['banana','apple','orange','pear','grape']


for fruit in myFavouriteFruits:
    print(fruit)

my_favourite_fruits = ['banana','apple','orange','pear','grape']
for fruit in myFavouriteFruits:

    print(len(my_favourite_fruits))

friends = ['Monica','Phoebe','Max','Pete','Terv']
print(friends)
friends[3]= "Max"
print(friends)




new_friends = friends.copy()
print(new_friends)





new_friends.pop()
print(new_friends)

new_friends.reverse()
print(new_friends)