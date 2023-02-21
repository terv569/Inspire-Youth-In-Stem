#!/usr/bin/env python3
 
# Python program to create lists
# Name : Tervil Moywaywa
# Email : tervilmoywaywa@gmail.com
# Date : 20th Feb 2023
# File : assignment.py
#create a list of empty  favourite musicians 
#using a for loop add new musicians 
#copy the list called celebrities
#sort the list 
#pop out two celebrities
#count the remaining celebrities 

favourite_musicians = ["Santan Dave", "Polo G", "Central Cee","A2 anti" ,"Burna Boy" ]
for musician in favourite_musicians:
    print(musician)
favourite_musicians.append ("CardiB")
favourite_musicians.append("Tems")
favourite_musicians.append("Mariah Carey")
favourite_musicians.append("Rihanna")
favourite_musicians.append("Beyonce")
for musician in favourite_musicians:

    print(musician)

celebs = favourite_musicians.copy()
print(celebs)
celebs.sort()
print(celebs)

celebs.pop()
celebs.pop()
print(celebs)


print(len(celebs))