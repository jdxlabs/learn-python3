#!/usr/bin/env python3

# A list is a collection which is ordered and changeable,
# it allows duplicate members.

# Changeable means that, once a list is created :
# - you can change its values
# - you can add or remove items to it

# you can make a list like this
mylist = ["blue", "green", "yellow"]
print(mylist)

print(type(mylist))
#   <class 'list'>

# or using the constructor
mylist = list(("blue", "green", "yellow"))
print(mylist)

# access an item
print(mylist[0])

# change an item value
mylist[0] = "orange"
print(mylist[0])

# xxx loop

# add an item
mylist.append("red")
print(mylist)

# remove an item
mylist.remove("yellow")
print(mylist)
