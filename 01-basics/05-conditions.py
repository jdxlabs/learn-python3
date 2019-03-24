#!/usr/bin/env python3

x = 10
y = 15
z = 24

# You can write conditions like this
# only "if" is mandatory
# and you can add multiple "elif"
if x > y:
    print("pass1")
elif x < y:
    print("pass2")
else:
    print("pass3")

# You can use logical operators
if x > y or x > z:
    print("At least one of the conditions is True")

if x > y and x > z:
    print("Both conditions are True")

# You can use parethesis, when necessary
if (x == y) and z:
    print("pass")

# It's technically possible to write conditions in one line
# if x > y: print("pass1")
# but it's not recommended, the PEP8 recommendation tells you
# "C0321: More than one statement on a single line (multiple-statements)"

# You can still make a "ternary operation"
i = 12 if x < y else 19
print(i)

# For booleans, you can write this condition
i = x < y
print(i)
# That is much more readable than this
# i = True if x < y else False
