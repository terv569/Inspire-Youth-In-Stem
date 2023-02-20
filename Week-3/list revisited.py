#!/usr/bin/env python3

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