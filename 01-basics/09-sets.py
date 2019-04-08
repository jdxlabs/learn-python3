#!/usr/bin/env python3

# A set is a collection which is unordered and unindexed,
# it doesn't allow duplicate members.

# you can make a set like this
# (note that the order isn't respected)
myset = {"one", "two", "three"}
print(myset)

print(type(myset))
#   <class 'set'>

# or using the constructor
myset = set(("one", "two", "three"))
print(myset)

# it's impossible to access an item directly,
# you have to make a loop
for x in myset:
    print(x)

# you can check if an item exists
if "one" in myset:
    print("ok")

# add an item
myset.add("four")
print(myset)

# add multiple items
myset.update(["five", "six", "seven"])
print(myset)

# get the length
print(len(myset))

# remove an item (with error catching)
myset.remove("seven")

# remove an item (without error catching)
myset.discard("seven")

# you can delete the set
del myset

# here are other methods than can be applied to sets
# clear() : to remove all the items in the set
# copy() : to get a copy of the set
