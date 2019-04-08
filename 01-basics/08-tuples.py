#!/usr/bin/env python3

# A tuple is a collection which is ordered and unchangeable,
# it allows duplicate members.

# Unchangeable means that, once a tuple is created :
# - you cannot change its values
# - you cannot add or remove items to it

# you can make a tuple like this
mytuple = ("john", "joe", "jenny")
print(mytuple)

print(type(mytuple))
#   <class 'tuple'>

# or using the constructor
mytuple = tuple(("john", "joe", "jenny"))
print(mytuple)

# select an item
print(mytuple[1])

# iterate the items
for item in mytuple:
    print(item)

# check if an item exists
if "joe" in mytuple:
    print("ok")

# retrieve the number of items
print(len(mytuple))

# you cannot add, modify or delete items

# you can still delete the tuple
del mytuple

# here are other methods than can be applied to tuples
# count("value") : to get the nb of items with the specified value
# index("value") : to get the index of the item
