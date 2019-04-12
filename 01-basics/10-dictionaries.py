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

# loop directly on values
for value in mydict.values():
    print(value)

# loop on items
for key, val in mydict.items():
    print(key, val)

# check if key exists
if "name" in mydict:
    print("ok")

# get length
print(len(mydict))

# add item
mydict["job"] = "developer"
print(mydict["job"])

# remove item
mydict.pop('job')
print(mydict)

# or remove it like this
del mydict["birthyear"]
print(mydict)

# you can delete the dictionary
del mydict

# you can copy a dictionary like this
mydict = dict(name="Doe", firstname="John", birthyear=1984)
mydict2 = mydict.copy()
print(mydict2)

# or like this
mydict3 = dict(mydict)
print(mydict3)

# here are other methods than can be applied to dictionaries
# clear() : to remove all the items in the dictionary
# fromkeys(keys, value) : returns a dictionary from keys and value
# get(key) : to get value from key
