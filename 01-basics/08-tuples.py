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

# TODO

# you can select in item
print(mytuple[1])

# you can iterate the items
for item in mytuple:
    print(item)

# you can check if an item exists
if "joe" in mytuple:
    print("ok")

# you can retrieve the number of items
print(len(mytuple))

# you can delete the tuple
del mytuple
