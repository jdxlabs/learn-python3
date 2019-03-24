#!/usr/bin/env python3

# A tuple is a collection which is ordered and unchangeable,

# Unchangeable means that, once a tuple is created :
# - you cannot change its values
# - you cannot add or remove items to it

mytuple = ("john", "joe", "jenny")
print(mytuple)

print(type(mytuple))
#   <class 'tuple'>

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
