# Advanced data types
# mutable vs immutable


# Data types that can be changed during program life cycle
# Add / remove elements
# Immutable----> these are data types that cannot be edited during program life cycle
# 1) list (murtable)
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
friends = ["Terv","Max","Rita",]
# or friends =[]empty list
# add elements ----> append(), extend()
# remove elements -----> pop(), del()
students = ["Max","Sue","Chad",]
friends.extend
friends.append
friends.sort
friends.reverse