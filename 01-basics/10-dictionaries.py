#!/usr/bin/env python3

# A dictionary is a collection which is unordered, changeable and indexed,
# it doesn't allow duplicate members.

# you can make a dictionnary like this
mydict = {
    "name": "Doe",
    "firstname": "John",
    "birthyear": 1984
}
print(mydict)

print(type(mydict))
#   <class 'dict'>

# or using the constructor
mydict = dict(name="Doe", firstname="John", birthyear=1984)
print(mydict)

# access an item
print(mydict["name"])
print(mydict.get("name"))

# change value
mydict["name"] = "Bar"
print(mydict["name"])

# loop
for x in mydict:
    print(f"key : {x}, value : {mydict[x]}")
