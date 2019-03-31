#!/usr/bin/env python3

# Lists are ...

# you can make a list like this
mylist = ["blue", "green", "yellow"]
print(mylist)

# or using the list constructor
mylist = list(("blue", "green", "yellow"))
print(mylist)

# access an item
print(mylist[0])

# add an item
mylist.append("red")
print(mylist)

# remove an item
mylist.remove("yellow")
print(mylist)
