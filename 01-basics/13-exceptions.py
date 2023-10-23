#!/usr/bin/env python3

# An exception handling in python
try:
    x = 10 / 0
except:
    print("Something went wrong")

# or you can use the try/except/else/finally structure
try:
    x = 10 / 0
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")
