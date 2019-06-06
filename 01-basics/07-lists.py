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

# loop
for x in mylist:
    print(x)

# check if item exists
if "green" in mylist:
    print(True)

# length
print(len(mylist))

# add an item
mylist.append("red")
print(mylist)

# add an item at a specific index
mylist.insert(3, "blue")
print(mylist)

# remove an item
mylist.remove("yellow")
print(mylist)

# remove an item at a specific index
# (or last item if not specified)
mylist.pop(3)
print(mylist)

# or like this
del mylist[2]
print(mylist)

# you can delete the list
del mylist

# here are other methods than can be applied to lists
# clear() : to remove all the items in the list
# copy() : to get a copy of the list
# count("value") : to get the nb of items with the specified value
# extend(iterable) : to add a list (or any iterable) to the end of the list
# index("value") : to get the index of the item
# reverse() : to reverse the list
# sort() : to sort the list
